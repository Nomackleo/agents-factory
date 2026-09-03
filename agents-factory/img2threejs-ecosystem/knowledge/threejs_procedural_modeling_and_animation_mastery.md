# Three.js Procedural Modeling & Runtime Animation Mastery

**Propósito:** Guía de ingeniería para la síntesis de mallas procedurales avanzadas en Three.js, técnicas de modelado constructivo, texturas sintéticas en Canvas2D, sombreadores PBR y bucles de animación a 60–120 FPS sin caída de frames.  
**Cumplimiento Normativo:** ISO 25010 (Eficiencia de Rendimiento), W3C WebGL 2.0.

---

## 1. Técnicas Avanzadas de Geometría Procedural

1. **Extrusión de Rutas 2D (`THREE.ExtrudeGeometry`):**
   - Empleo de `THREE.Shape` con curvas Bézier (`bezierCurveTo`) y arcos para crear perfiles aerodinámicos, letras, logotipos y carcasas curvas que no pueden representarse con cajas simples.
2. **Geometría de Revolución (`THREE.LatheGeometry`):**
   - Definición de una spline 2D en el plano XY revolucionada en 360° para crear botellas, copas, turbinas, conos de propulsión y columnas torneadas con costo computacional mínimo.
3. **Fusión de Geometrías para Reducción de Draw Calls:**
   - En objetos complejos con más de 20 partes estáticas que comparten el mismo material, agruparlas mediante `BufferGeometryUtils.mergeGeometries`:

     ```typescript
     import * as BufferGeometryUtils from 'three/examples/jsm/utils/BufferGeometryUtils.js';
     const mergedGeo = BufferGeometryUtils.mergeGeometries([geo1, geo2, geo3]);
     const singleMesh = new THREE.Mesh(mergedGeo, sharedMaterial);
     ```

---

## 2. Texturizado Procedural Autónomo (Zero External Assets)

Para simular paneles metálicos, rejillas, líneas de circuito o patrones de fibra de carbono sin descargar imágenes externas:

```typescript
function createCircuitGridTexture(): THREE.CanvasTexture {
  const canvas = document.createElement('canvas');
  canvas.width = 512;
  canvas.height = 512;
  const ctx = canvas.getContext('2d')!;
  
  ctx.fillStyle = '#0a192f';
  ctx.fillRect(0, 0, 512, 512);
  
  ctx.strokeStyle = '#ffd231';
  ctx.lineWidth = 2;
  // Dibujar rejillas y pistas de circuito procedurales
  for (let i = 0; i < 512; i += 32) {
    ctx.beginPath();
    ctx.moveTo(i, 0); ctx.lineTo(i, 512);
    ctx.moveTo(0, i); ctx.lineTo(512, i);
    ctx.stroke();
  }
  
  const texture = new THREE.CanvasTexture(canvas);
  texture.wrapS = THREE.RepeatWrapping;
  texture.wrapT = THREE.RepeatWrapping;
  return texture;
}
```

---

## 3. Arquitectura del Bucle de Animación (`update(delta, elapsed)`)

```typescript
// Patrón de actualización suave basado en tiempo delta
root.update = (delta: number, elapsed: number) => {
  // 1. Flotación senoidal
  chassis.position.y = Math.sin(elapsed * 2.0) * 0.15;
  
  // 2. Rotación continua de aspas/hélices
  rotors.forEach(r => r.rotation.y += delta * 12.0);
  
  // 3. Pulso lumínico en material emisivo
  const pulse = (Math.sin(elapsed * 4.0) + 1.0) * 0.5;
  emissiveMaterial.emissiveIntensity = 0.4 + pulse * 0.8;
};
```
