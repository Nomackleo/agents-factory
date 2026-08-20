# Meta Immersive Web SDK (`@iwsdk/core`) — Arquitectura de Computación Espacial, WebXR y AR/VR

**Referencia Oficial:** Meta Open Source (`facebook/immersive-web-sdk` / `@iwsdk/core`)  
**Fundamento:** Three.js + Entity Component System (ECS) de alto rendimiento (`elics` + Preact Signals)  
**Alcance:** Experiencias web inmersivas unificadas (Meta Quest 3/Pro, Apple Vision Pro, Android AR, iOS WebXR y Emulación Desktop con ratón/teclado).  
**Cumplimiento Normativo:** ISO 25010 (Eficiencia de Rendimiento & Accesibilidad), DORA (Garantía de 72/90/120 FPS estables).

---

## 1. Filosofía Arquitectural: "Same Code, Two Experiences"

El **Meta Immersive Web SDK (IWSDK)** resuelve la principal barrera del desarrollo XR: la necesidad de visores físicos para iterar.
* **Modo Inmersivo:** En visores WebXR (Meta Quest Browser / Safari VisionOS), habilita controladores 6DoF, hand-tracking, oclusión por hardware y capas de proyección Quad/Cylinder.
* **Modo Emulación Desktop:** En navegadores de escritorio sin visor, proporciona controles automáticos FPS (WASD + Mouse Look) con simulación de puntero y manos virtuales sin necesidad de extensiones de navegador.

```
                  ┌────────────────────────────────────────┐
                  │          @iwsdk/core (World)           │
                  └───────────────────┬────────────────────┘
                                      │
               ┌──────────────────────┴──────────────────────┐
               ▼                                             ▼
    [ WebXR Device API ]                           [ Desktop Fallback ]
  - Headset 6DoF Tracking                       - WASD + Mouse Look
  - Hand Tracking Joints                        - Virtual Controller Rays
  - Hardware Depth Occlusion                    - Emulated Grabs & Pokes
  - Scene Planes / Meshes                       - Screen Space Hit-Test
```

---

## 2. Arquitectura ECS (Entity Component System)

El SDK organiza la lógica mediante un ECS puro desacoplado, combinando Three.js con reactividad de señales (`@preact/signals-core`):

### A. Inicialización del Mundo (`World.create`)
```typescript
import { World, Entity, Component } from '@iwsdk/core';

const container = document.getElementById('scene-container') as HTMLDivElement;

const world = await World.create(container, {
  renderer: { antialias: true, alpha: true },
  xr: {
    referenceSpace: 'local-floor',
    features: ['hit-test', 'plane-detection', 'mesh-detection', 'depth-sensing', 'hand-tracking']
  }
});
```

### B. Creación de Entidades y Componentes Personalizados
```typescript
import { createComponent, Types } from '@iwsdk/core';

// Definición de componente reactivo
export const HoverEffect = createComponent('HoverEffect', {
  highlightColor: { type: Types.Color, default: 0xffd231 },
  scaleFactor: { type: Types.Number, default: 1.1 },
  isHovered: { type: Types.Boolean, default: false }
});

// Creación de una entidad en el espacio 3D
const cubeEntity = world.createEntity();
cubeEntity.addComponent(HoverEffect, { highlightColor: 0x3fbfa8 });
cubeEntity.object3D.position.set(0, 1.2, -1.5);
```

---

## 3. Módulos Centrales de Producción

### A. Interacción Espacial (`@iwsdk/core/grab` y `poke`)
* **Grab System:** Soporta agarre directo de 1 mano, agarre bimanual con escalado/rotación libre y agarre por rayo a distancia (*distance grab*).
* **Poke System:** Detección de contacto de la punta del dedo índice sobre interfaces 3D flotantes con retroalimentación háptica.
* **Hand Tracking:** Mapeo automático de las 26 articulaciones de la mano (*joints*) con detección de gestos (pellizco, puño, palma abierta).

### B. Motor de Locomoción (`@iwsdk/locomotor`)
* **Teletransporte Parabólico:** Curva física balística con validación de áreas transitables (*navmesh*).
* **Smooth Locomotion & Snap Turn:** Movimiento continuo por joystick con rotación angular por pasos (ej. 30° o 45°).
* **Tunneling Vignette (Anti-Mareo):** Atenuación visual periférica dinámica proporcional a la velocidad angular para prevenir la cinetosis (motion sickness).

### C. Scene Understanding & Realidad Aumentada (AR)
* **Plane Detection:** Detección en tiempo real de superficies planas del mundo real (suelos, paredes, mesas, techos).
* **Environment Meshing:** Reconstrucción de la malla tridimensional del entorno circundante para colisiones físicas reales.
* **Depth Occlusion:** Oclusión de objetos 3D virtuales detrás de las manos y el mobiliario del usuario mediante buffers de profundidad de hardware.
* **Persistent Anchors:** Creación de anclajes espaciales que persisten entre sesiones.

### D. Física Havok en Web Workers
* Simulación de cuerpos rígidos (*rigid bodies*) y articulaciones (*constraints*) ejecutada en un Web Worker independiente para no bloquear el hilo principal de renderizado (garantizando 90 FPS estables).

---

## 4. Herramientas MCP y Automatización para Agentes de IA

El SDK incluye internamente un servidor **Model Context Protocol (MCP)** en `@iwsdk/core/mcp`:
* **`ecs-debug-tools.ts`**: Permite a agentes autónomos listar, inspeccionar y modificar componentes de cualquier entidad en tiempo real.
* **`scene-tools.ts`**: Herramientas para que el agente inspeccione la jerarquía de Three.js, transforme objetos, ejecute raycasts y valide estados de física en sesiones de prueba *headless*.
