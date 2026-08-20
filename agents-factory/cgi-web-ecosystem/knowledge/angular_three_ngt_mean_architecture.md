# Angular Three (NGT) & MEAN Stack 3D Architecture — Parallax Occlusion & Render Texture Portals

**Referencia Oficial:** Angular Three (`angular-threejs/angular-three`) & NGT 3D Slideshow (`nartc/ngt-3d-slideshow`) por Chau Tran  
**Stack de Destino:** MEAN (MongoDB, Express, Angular 17/18/19/20+, Node.js) con Angular Three (`@angular-three/core`, `angular-three-soba`)  
**Técnica Destacada:** Portales 3D por `NgtsRenderTexture` con Ilusión de Profundidad Infinita / Parallax Occlusion  
**Cumplimiento Normativo:** ISO 25010 (Eficiencia de Rendimiento, Mantenibilidad), DORA (60+ FPS estables).

---

## 1. Arquitectura Angular Three (NGT) en el Stack MEAN

Angular Three (NGT) proporciona un puente declarativo y fuertemente tipado entre **Angular Signals** y el grafo de escena imperativo de **Three.js**:

```
 ┌─────────────────────────────────────────────────────────────┐
 │                      MEAN Architecture                      │
 │   MongoDB  <──>  Express / Node.js API  <──>  Angular SSR   │
 └──────────────────────────────┬──────────────────────────────┘
                                │
 ┌──────────────────────────────▼──────────────────────────────┐
 │                  Angular Three (NGT Core)                   │
 │  - Angular Signals: signal(), computed(), input()           │
 │  - OnPush ChangeDetection (Zero Zone.js overhead)           │
 │  - Declarative Three.js Elements: <ngt-mesh>, <ngt-color>   │
 │  - Life-cycle Hooks: injectBeforeRender(), injectStore()    │
 └──────────────────────────────┬──────────────────────────────┘
                                │
 ┌──────────────────────────────▼──────────────────────────────┐
 │                     Angular Three Soba                      │
 │  - <ngts-render-texture>: Portales 3D & Parallax Windows   │
 │  - <ngts-camera-controls>: Dolly Zoom cinemático            │
 │  - <ngts-accumulative-shadows>: Sombras de estudio suaves   │
 │  - <ngts-environment> & <ngts-lightformer>: IBL dinámico   │
 └─────────────────────────────────────────────────────────────┘
```

---

## 2. Técnica de Parallax Occlusion & Render Texture Portals

La técnica de **Render Texture Portals** crea la ilusión de una ventana o portal tridimensional con profundidad infinita (Parallax Occlusion) proyectada sobre un plano 2D:

### A. Escena Principal (Outer World)
En la escena exterior, se posicionan quads (`<ngt-plane-geometry>`) que actúan como "pantallas" o "ventanas":

```html
@for (scene of scenes; track scene.name) {
  <ngt-mesh [position]="[$index * (viewport().width + slideDistance), 0, 0]">
    <ngt-plane-geometry *args="[viewport().width, viewport().height]" />
    <ngt-mesh-basic-material [toneMapped]="false">
      <!-- Mapea automáticamente al canal 'map' del material -->
      <ngts-render-texture>
        <app-render-texture-scene *renderTextureContent [scene]="scene" />
      </ngts-render-texture>
    </ngt-mesh-basic-material>
  </ngt-mesh>
}
```

### B. Escena Interior Aislada (Inner World)
Cada portal contiene su propia cámara (`<ngts-perspective-camera>`), controles orbitales con autorotación, modelo 3D GLB, iluminación IBL y sombras acumulativas:

```html
<ngt-color *args="['#ffffff']" attach="background" />
<ngt-group [name]="name" [dispose]="null">
  <ngts-perspective-camera [options]="{ makeDefault: true, position: [3, 3, 8], near: 0.5 }" />
  <ngts-orbit-controls [options]="{ autoRotate: true, enablePan: false, autoRotateSpeed: 0.5 }" />
  <ngt-primitive *args="[model()]" [parameters]="{ scale: ratioScale }" />
  
  <!-- Sombras Acumulativas de Estudio -->
  <ngts-accumulative-shadows [options]="{ frames: 100, alphaTest: 0.75, scale: 30, opacity: 0.8 }">
    <ngts-randomized-lights [options]="{ amount: 4, radius: 9, intensity: 0.8 * Math.PI, position: [10, 5, 15] }" />
  </ngts-accumulative-shadows>
  
  <!-- Iluminación IBL con Lightformers -->
  <ngts-environment [options]="{ blur: 0.8, background: true }">
    <ng-template>
      <ngt-mesh [scale]="15">
        <ngt-sphere-geometry />
        <ngt-mesh-basic-material [color]="mainColor" [side]="BackSide" />
      </ngt-mesh>
      <ngts-lightformer [options]="{ position: [5, 0, -5], form: 'rect', intensity: 1, scale: [3, 5] }" />
    </ng-template>
  </ngts-environment>
</ngt-group>
```

---

## 3. Cinemática de Cámara con Dolly Zoom (`CameraHandler`)

Para navegar entre las diapositivas con una sensación cinemática fluida, la cámara ejecuta una transición en 3 pasos:

1. **Retroceso (Dolly Out):** La cámara se aleja a `dollyDistance = 20` mientras mantiene el foco en el slide actual.
2. **Traslación Lateral (Pan):** Se desplaza el objetivo al siguiente slide.
3. **Aproximación (Dolly In):** La cámara se acerca suavemente a la posición de visualización óptima ($z=5$).

```typescript
private async moveToSlide() {
  const cameraControls = this.cameraControlsRef().controls();
  const currentX = this.lastSlide * (this.viewport().width + this.slideDistance());
  const targetX = slide() * (this.viewport().width + this.slideDistance());

  // 1. Alejar
  await cameraControls.setLookAt(currentX, 3, this.dollyDistance, currentX, 0, 0, true);
  // 2. Trasladar
  await cameraControls.setLookAt(targetX, 1, this.dollyDistance, targetX, 0, 0, true);
  // 3. Enfocar
  await cameraControls.setLookAt(targetX, 0, 5, targetX, 0, 0, true);
}
```

---

## 4. Mejores Prácticas para MEAN & Angular Three

* **Precarga de Modelos GLTF:** Usar `injectGLTF.preload(() => [...])` a nivel de módulo para evitar bloqueos en el hilo principal durante la navegación.
* **Desconexión Fuera de Zone.js:** Usar `injectBeforeRender()` para animaciones a 60 FPS sin disparar ciclos de detección de cambios de Angular.
* **Limpieza de Recursos (`[dispose]="null"`):** En componentes que se reciclan con `@for`, usar `[dispose]="null"` en los grupos para reutilizar las geometrías y texturas en VRAM.
