/**
 * Three.js WebGPU & TSL Pipeline Reference Module
 * 
 * Implementa:
 * - Inicialización de WebGPURenderer
 * - Custom TSL Node Materials (Shading Language)
 * - Compute Shaders para simulación masiva de partículas en GPU
 */

import * as THREE from 'three/webgpu';
import {
  Fn,
  uv,
  color,
  float,
  vec3,
  sin,
  cos,
  time,
  mix,
  storage,
  instanceIndex,
  positionLocal,
  MeshStandardNodeMaterial,
} from 'three/tsl';

export interface WebGPUSceneSetup {
  renderer: THREE.WebGPURenderer;
  scene: THREE.Scene;
  camera: THREE.PerspectiveCamera;
  computeNode: any;
}

export async function initWebGPUPipeline(container: HTMLElement): Promise<WebGPUSceneSetup> {
  // 1. Inicializar WebGPURenderer
  const renderer = new THREE.WebGPURenderer({ antialias: true, powerPreference: 'high-performance' });
  await renderer.init();
  renderer.setSize(container.clientWidth, container.clientHeight);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  container.appendChild(renderer.domElement);

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(60, container.clientWidth / container.clientHeight, 0.1, 1000);
  camera.position.set(0, 5, 15);

  // 2. Luz de entorno IBL y direccional
  const dirLight = new THREE.DirectionalLight(0xffffff, 2.0);
  dirLight.position.set(5, 10, 7);
  scene.add(dirLight);
  scene.add(new THREE.AmbientLight(0x0b3752, 1.0));

  // 3. Sistema de partículas por Compute Shader en GPU (100,000 partículas)
  const particleCount = 100000;
  const positionArray = new Float32Array(particleCount * 3);
  for (let i = 0; i < particleCount * 3; i += 3) {
    positionArray[i] = (Math.random() - 0.5) * 20;
    positionArray[i + 1] = Math.random() * 10;
    positionArray[i + 2] = (Math.random() - 0.5) * 20;
  }

  const positionBuffer = new THREE.StorageBufferAttribute(positionArray, 3);
  const positionStorage = storage(positionBuffer, 'vec3', particleCount);

  // Kernel de Cómputo TSL
  const computeParticles = Fn(() => {
    const idx = instanceIndex;
    const pos = positionStorage.element(idx);
    const waveY = sin(pos.x.mul(0.5).add(time.mul(2.0))).mul(0.02);
    const updatedPos = pos.add(vec3(0.0, waveY, 0.0));
    positionStorage.element(idx).assign(updatedPos);
  })().compute(particleCount);

  // 4. Malla de prueba con Material Nodal TSL
  const sphereGeo = new THREE.SphereGeometry(2, 64, 64);
  const nodeMaterial = new MeshStandardNodeMaterial();

  const dynamicPBR = Fn(([pos]) => {
    return mix(color(0x07283d), color(0xffd231), sin(pos.y.mul(2.0).add(time)).mul(0.5).add(0.5));
  });

  nodeMaterial.colorNode = dynamicPBR(positionLocal);
  nodeMaterial.roughnessNode = float(0.2);
  nodeMaterial.metalnessNode = float(0.8);

  const heroMesh = new THREE.Mesh(sphereGeo, nodeMaterial);
  scene.add(heroMesh);

  return { renderer, scene, camera, computeNode: computeParticles };
}
