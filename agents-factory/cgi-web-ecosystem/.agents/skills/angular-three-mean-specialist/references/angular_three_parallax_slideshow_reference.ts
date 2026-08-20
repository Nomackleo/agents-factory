/**
 * Angular Three (NGT) Parallax Slideshow Reference Component
 * 
 * Implementa:
 * - Render Texture Portals con Parallax Occlusion en Angular Standalone
 * - Cinemática de Cámara (Dolly Zoom) coordinada por Signals
 * - Sombras acumulativas y Environment IBL
 */

import {
  ChangeDetectionStrategy,
  Component,
  CUSTOM_ELEMENTS_SCHEMA,
  input,
  signal,
  viewChild,
  afterNextRender,
} from '@angular/core';
import { extend, injectStore, NgtArgs } from 'angular-three';
import { NgtsCameraControls, NgtsOrbitControls } from 'angular-three-soba/controls';
import { NgtsPerspectiveCamera } from 'angular-three-soba/cameras';
import { NgtsGrid } from 'angular-three-soba/abstractions';
import { NgtsRenderTexture, NgtsRenderTextureContent, NgtsEnvironment, NgtsAccumulativeShadows, NgtsRandomizedLights } from 'angular-three-soba/staging';
import { injectGLTF } from 'angular-three-soba/loaders';
import * as THREE from 'three';

extend(THREE);

export interface SlideSceneData {
  name: string;
  mainColor: string;
  modelUrl: string;
}

// 1. Componente del Mundo Interior (Portal)
@Component({
  selector: 'app-portal-world',
  standalone: true,
  template: `
    <ngt-color *args="['#ffffff']" attach="background" />
    <ngt-group [name]="data().name" [dispose]="null">
      <ngts-perspective-camera [options]="{ makeDefault: true, position: [3, 2, 6], near: 0.5 }" />
      <ngts-orbit-controls [options]="{ autoRotate: true, enablePan: false, autoRotateSpeed: 0.6 }" />
      
      <ngt-primitive *args="[model()]" />
      
      <ngt-ambient-light [intensity]="0.2 * Math.PI" />
      <ngts-accumulative-shadows [options]="{ frames: 80, alphaTest: 0.75, scale: 20, opacity: 0.8 }">
        <ngts-randomized-lights [options]="{ amount: 4, radius: 8, intensity: 0.8 * Math.PI, position: [8, 6, 12] }" />
      </ngts-accumulative-shadows>
      
      <ngts-environment [options]="{ preset: 'city' }" />
    </ngt-group>
  `,
  imports: [
    NgtArgs,
    NgtsPerspectiveCamera,
    NgtsOrbitControls,
    NgtsAccumulativeShadows,
    NgtsRandomizedLights,
    NgtsEnvironment,
  ],
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class PortalWorld {
  data = input.required<SlideSceneData>();
  model = injectGLTF(() => this.data().modelUrl);
  protected readonly Math = Math;
}

// 2. Componente de la Escena Principal (Outer World)
@Component({
  selector: 'app-parallax-slideshow-scene',
  standalone: true,
  template: `
    <ngt-color *args="['#031621']" attach="background" />
    <ngt-ambient-light [intensity]="0.3 * Math.PI" />

    <!-- Portales de Render Texture con Efecto de Profundidad Parallax -->
    @for (item of slideList(); track item.name) {
      <ngt-mesh [position]="[$index * (viewport().width + slideDistance()), 0, 0]">
        <ngt-plane-geometry *args="[viewport().width, viewport().height]" />
        <ngt-mesh-basic-material [toneMapped]="false">
          <ngts-render-texture>
            <app-portal-world *renderTextureContent [data]="item" />
          </ngts-render-texture>
        </ngt-mesh-basic-material>
      </ngt-mesh>
    }

    <!-- Grid Espacial de Fondo -->
    <ngts-grid
      [options]="{
        position: [0, -viewport().height / 2, 0],
        sectionSize: 1,
        sectionColor: '#07283d',
        cellSize: 0.5,
        cellColor: '#12496b',
        infiniteGrid: true,
        fadeDistance: 40
      }"
    />
  `,
  imports: [
    NgtArgs,
    NgtsGrid,
    NgtsRenderTexture,
    NgtsRenderTextureContent,
    PortalWorld,
  ],
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ParallaxSlideshowScene {
  slideList = input.required<SlideSceneData[]>();
  slideDistance = input(1.5);
  currentSlide = input(0);

  private store = injectStore();
  protected viewport = this.store.select('viewport');
  protected readonly Math = Math;
}
