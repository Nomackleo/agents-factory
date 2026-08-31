# Reglas Operativas y Estándares de Diseño: CADAM Parametric CAD Ecosystem

**Propósito:** Definir los principios inmutables de modelado CAD paramétrico, geometría sólida constructiva (CSG), diseño para fabricación aditiva (DfAM / Impresión 3D) y arquitectura WebAssembly.  
**Cumplimiento Normativo:** ISO 17296 / ASTM 52900 (Fabricación Aditiva), ISO 25010 (Calidad y Robustez de Software), ISO 9001:2015.

---

## 1. Reglas de Modelado Paramétrico OpenSCAD

1. **Variables y Parámetros Expuestos Obligatorios:**
   - Todo modelo debe declarar sus dimensiones clave como variables al inicio del script con comentarios descriptivos para que la interfaz de CADAM pueda generar automáticamente los *sliders* interactivos:
     ```openscad
     // [Dimensiones Principales]
     outer_diameter = 50; // [20:1:100]
     wall_thickness = 2.4; // [1.2:0.2:5.0]
     height = 30; // [10:1:80]
     ```
2. **Geometría Sólida Estanca (*Watertight / 2-Manifold*):**
   - Prohibido generar caras superpuestas en operaciones booleanas (*Z-fighting*).
   - En operaciones de diferencia (`difference()`), la herramienta de corte debe sobrepasar siempre las caras del sólido base por al menos `$fn` o un delta infinitesimal (`+ 0.02mm` o `+ 0.1mm`):
     ```openscad
     difference() {
         cube([20, 20, 20], center=true);
         translate([0, 0, -1])
             cylinder(r=5, h=22, center=true, $fn=64); // Sobrepasa para corte limpio
     }
     ```
3. **Resolución de Curvas (`$fn`, `$fa`, `$fs`):**
   - Utilizar `$fn` calibrado: `$fn = 32` para previsualización rápida y `$fn = 64` a `$fn = 128` para exportación final a STL/3MF.

---

## 2. Reglas de Diseño para Impresión 3D (DfAM)

1. **Espesores Mínimos de Pared:**
   - Para tecnología **FDM**: Espesor mínimo de pared $\ge 1.2\text{mm}$ (equivalente a 3 perímetros de boquilla estándar de 0.4mm).
   - Para tecnología **SLA / Resina**: Espesor mínimo $\ge 1.0\text{mm}$ con orificios de drenaje si el modelo es hueco.
2. **Ángulos de Voladizo (*Overhangs*):**
   - Las superficies en voladizo no deben exceder los $45^\circ$ respecto a la vertical sin soportes de impresión. Si el ángulo es mayor, aplicar chaflanes (*chamfers*) progresivos.
3. **Holguras y Tolerancias de Ensamble (*Clearances*):**
   - Encaje a presión (*Press-fit / Interference fit*): Holgura de $0.1\text{mm} - 0.15\text{mm}$.
   - Encaje deslizante (*Slip / Sliding fit*): Holgura de $0.2\text{mm} - 0.3\text{mm}$.
   - Mecanismos articulados impresos en una sola pieza (*Print-in-Place*): Holgura mínima de $0.4\text{mm}$.

---

## 3. Integración y Gobernanza WebAssembly

1. **Compilación Desatendida en Web Workers:**
   - Ninguna compilación de OpenSCAD debe ejecutarse en el hilo principal de JavaScript para evitar congelamientos de la interfaz gráfica ($INP < 16\text{ms}$).
2. **Transferencia de Buffers por Referencia (`Transferable Objects`):**
   - Los datos de geometría (vértices, normales, índices) generados en C++/WASM deben transferirse hacia Three.js mediante `ArrayBuffer` transferibles para lograr rendimiento $O(1)$ sin duplicar memoria.
