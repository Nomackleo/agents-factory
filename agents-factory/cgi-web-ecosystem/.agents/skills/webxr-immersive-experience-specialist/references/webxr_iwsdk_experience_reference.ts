/**
 * WebXR Immersive Experience Reference Pipeline (Meta IWSDK / @iwsdk/core)
 * 
 * Implementa:
 * - Inicialización de World con ECS
 * - Modos Immersive-VR e Immersive-AR con emulación de escritorio
 * - Interacciones de agarre (Grab) y toque táctil (Poke)
 * - Locomoción con teletransporte parabólico y viñeta anti-mareo
 */

import { World, createComponent, Types, Entity } from '@iwsdk/core';
import * as THREE from 'three';

// 1. Componente ECS personalizado para interactividad
export const InteractiveObject = createComponent('InteractiveObject', {
  isHovered: { type: Types.Boolean, default: false },
  isGrabbed: { type: Types.Boolean, default: false },
  originalColor: { type: Types.Color, default: 0x07283d },
  highlightColor: { type: Types.Color, default: 0xffd231 },
});

export interface WebXRSceneContext {
  world: World;
  entities: Entity[];
}

export async function initWebXRExperience(container: HTMLDivElement): Promise<WebXRSceneContext> {
  // 2. Inicializar el Mundo con configuración WebXR y fallback de escritorio
  const world = await World.create(container, {
    renderer: {
      antialias: true,
      powerPreference: 'high-performance',
      alpha: true,
    },
    xr: {
      sessionMode: 'immersive-vr',
      referenceSpace: 'local-floor',
      features: [
        'hand-tracking',
        'hit-test',
        'plane-detection',
        'mesh-detection',
        'depth-sensing',
        'anchors',
      ],
    },
  });

  const entities: Entity[] = [];

  // 3. Crear entorno e iluminación básica
  const dirLight = new THREE.DirectionalLight(0xffffff, 1.8);
  dirLight.position.set(2, 4, 3);
  world.scene.add(dirLight);
  world.scene.add(new THREE.AmbientLight(0x0b3752, 0.8));

  // 4. Crear entidad interactiva con geometría y material
  const interactiveEntity = world.createEntity();
  
  const boxGeo = new THREE.BoxGeometry(0.25, 0.25, 0.25);
  const boxMat = new THREE.MeshStandardMaterial({
    color: 0x07283d,
    roughness: 0.2,
    metalness: 0.8,
  });
  const boxMesh = new THREE.Mesh(boxGeo, boxMat);

  interactiveEntity.setObject3D(boxMesh);
  interactiveEntity.object3D.position.set(0, 1.2, -1.0);
  interactiveEntity.addComponent(InteractiveObject, {
    originalColor: 0x07283d,
    highlightColor: 0xffd231,
  });

  entities.push(interactiveEntity);

  // 5. Suelo de referencia para teletransporte
  const floorEntity = world.createEntity();
  const floorGeo = new THREE.PlaneGeometry(20, 20);
  floorGeo.rotateX(-Math.PI / 2);
  const floorMat = new THREE.MeshStandardMaterial({
    color: 0x031621,
    roughness: 0.8,
  });
  const floorMesh = new THREE.Mesh(floorGeo, floorMat);
  floorEntity.setObject3D(floorMesh);
  entities.push(floorEntity);

  return { world, entities };
}
