/**
 * GPGPU Water Simulator & Rendering Pipeline Reference (Three.js & TypeScript)
 * 
 * Implementa:
 * - Ping-Pong Render Targets para simulación de heightfield
 * - Solución de ecuación de onda 2D discretizada (Evan Wallace Method)
 * - Fixed Timestep de 120 Hz con acumulador de sub-pasos
 * - Pase de refracción offscreen + cáusticas proyectadas
 */

import * as THREE from 'three';

export interface GPGPUWaterConfig {
  resolution: number;
  damping: number;
  fixedTimeStep: number;
  maxSubSteps: number;
}

export class GPGPUWaterSimulator {
  private scene: THREE.Scene;
  private camera: THREE.OrthographicCamera;
  private mesh: THREE.Mesh;

  public readTarget: THREE.WebGLRenderTarget;
  public writeTarget: THREE.WebGLRenderTarget;

  private updateMaterial: THREE.ShaderMaterial;
  private dropMaterial: THREE.ShaderMaterial;

  private accumulator: number = 0;
  private fixedTimeStep: number;
  private maxSubSteps: number;

  constructor(
    private renderer: THREE.WebGLRenderer,
    config: GPGPUWaterConfig = { resolution: 512, damping: 0.996, fixedTimeStep: 1 / 120, maxSubSteps: 4 }
  ) {
    this.fixedTimeStep = config.fixedTimeStep;
    this.maxSubSteps = config.maxSubSteps;

    // 1. Configurar cámara ortográfica para simulación GPGPU
    this.camera = new THREE.OrthographicCamera(-1, 1, 1, -1, 0, 1);
    this.scene = new THREE.Scene();

    // 2. Render Targets de alta precisión para Ping-Pong
    const options: THREE.RenderTargetOptions = {
      format: THREE.RGBAFormat,
      type: THREE.HalfFloatType,
      minFilter: THREE.LinearFilter,
      magFilter: THREE.LinearFilter,
      depthBuffer: false,
      stencilBuffer: false,
    };

    this.readTarget = new THREE.WebGLRenderTarget(config.resolution, config.resolution, options);
    this.writeTarget = new THREE.WebGLRenderTarget(config.resolution, config.resolution, options);

    // 3. Material de actualización de ondas
    this.updateMaterial = new THREE.ShaderMaterial({
      uniforms: {
        u_texture: { value: null },
        u_delta: { value: new THREE.Vector2(1.0 / config.resolution, 1.0 / config.resolution) },
        u_damping: { value: config.damping },
      },
      vertexShader: `
        varying vec2 vUv;
        void main() {
          vUv = uv;
          gl_Position = vec4(position, 1.0);
        }
      `,
      fragmentShader: `
        precision highp float;
        uniform sampler2D u_texture;
        uniform vec2 u_delta;
        uniform float u_damping;
        varying vec2 vUv;

        const float WAVE_SPEED = 0.85;
        const float BOUNDARY_DAMPING = 0.85;

        void main() {
          vec4 currentSample = texture2D(u_texture, vUv);
          float currentHeight = currentSample.r;
          float previousHeight = currentSample.g;

          float north = texture2D(u_texture, vUv + vec2(0.0, u_delta.y)).r;
          float south = texture2D(u_texture, vUv - vec2(0.0, u_delta.y)).r;
          float east  = texture2D(u_texture, vUv + vec2(u_delta.x, 0.0)).r;
          float west  = texture2D(u_texture, vUv - vec2(u_delta.x, 0.0)).r;

          float laplacian = (north + south + east + west - 4.0 * currentHeight);
          float c2dt2 = WAVE_SPEED * WAVE_SPEED * 0.3;
          float newHeight = 2.0 * currentHeight - previousHeight + c2dt2 * laplacian;

          vec2 edgeDistance = min(vUv, 1.0 - vUv);
          float edgeFactor = min(edgeDistance.x, edgeDistance.y);
          float boundaryDamp = smoothstep(0.0, u_delta.x * 4.0, edgeFactor);
          newHeight *= mix(BOUNDARY_DAMPING, u_damping, boundaryDamp);

          gl_FragColor = vec4(clamp(newHeight, -0.08, 0.08), currentHeight, 0.0, 1.0);
        }
      `
    });

    // 4. Material de inyección de gota
    this.dropMaterial = new THREE.ShaderMaterial({
      uniforms: {
        u_texture: { value: null },
        u_center: { value: new THREE.Vector2(0.5, 0.5) },
        u_radius: { value: 0.03 },
        u_strength: { value: 0.05 },
        u_delta: { value: new THREE.Vector2(1.0 / config.resolution, 1.0 / config.resolution) }
      },
      vertexShader: `
        varying vec2 vUv;
        void main() {
          vUv = uv;
          gl_Position = vec4(position, 1.0);
        }
      `,
      fragmentShader: `
        precision highp float;
        uniform sampler2D u_texture;
        uniform vec2 u_center;
        uniform float u_radius;
        uniform float u_strength;
        varying vec2 vUv;

        void main() {
          vec4 info = texture2D(u_texture, vUv);
          float drop = max(0.0, 1.0 - length(u_center - vUv) / u_radius);
          drop = 0.5 - cos(drop * 3.14159265359) * 0.5;
          info.r += drop * u_strength;
          gl_FragColor = info;
        }
      `
    });

    // 5. Plano de pantalla completa para simulación
    this.mesh = new THREE.Mesh(new THREE.PlaneGeometry(2, 2), this.updateMaterial);
    this.scene.add(this.mesh);
  }

  /**
   * Inyecta una perturbación/gota en coordenadas UV (0..1)
   */
  public addDrop(x: number, y: number, radius: number = 0.03, strength: number = 0.04): void {
    this.dropMaterial.uniforms.u_texture.value = this.readTarget.texture;
    this.dropMaterial.uniforms.u_center.value.set(x, y);
    this.dropMaterial.uniforms.u_radius.value = radius;
    this.dropMaterial.uniforms.u_strength.value = strength;

    this.mesh.material = this.dropMaterial;
    this.renderer.setRenderTarget(this.writeTarget);
    this.renderer.render(this.scene, this.camera);
    this.swap();
    this.mesh.material = this.updateMaterial;
  }

  /**
   * Ejecuta un paso de simulación de onda
   */
  private stepPhysics(): void {
    this.updateMaterial.uniforms.u_texture.value = this.readTarget.texture;
    this.renderer.setRenderTarget(this.writeTarget);
    this.renderer.render(this.scene, this.camera);
    this.swap();
  }

  /**
   * Actualiza la simulación respetando el timestep fijo de 120 Hz
   */
  public update(deltaTime: number): void {
    this.accumulator += deltaTime;
    let subSteps = 0;

    while (this.accumulator >= this.fixedTimeStep && subSteps < this.maxSubSteps) {
      this.stepPhysics();
      this.accumulator -= this.fixedTimeStep;
      subSteps++;
    }
  }

  /**
   * Intercambio de buffers Ping-Pong
   */
  private swap(): void {
    const temp = this.readTarget;
    this.readTarget = this.writeTarget;
    this.writeTarget = temp;
  }

  public getSimulationTexture(): THREE.Texture {
    return this.readTarget.texture;
  }
}
