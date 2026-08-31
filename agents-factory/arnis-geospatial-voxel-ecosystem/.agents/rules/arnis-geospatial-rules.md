# Reglas Operativas y Estándares de Diseño: Arnis Geospatial Voxel Ecosystem

**Propósito:** Definir los estándares inmutables para la ingesta geoespacial (OpenStreetMap), modelos digitales de elevación (DEM), voxelización a escala 1:1 ($1\text{ bloque} = 1\text{ metro}$) y exportación de gemelos digitales 3D en Arnis.  
**Cumplimiento Normativo:** OGC (Open Geospatial Consortium Standards), ISO 19115 (Metadatos Geográficos), ISO 25010 (Calidad y Rendimiento de Software).

---

## 1. Reglas de Ingesta Geoespacial y Coordenadas

1. **Definición Estricta de Cuadro Delimitador (*Bounding Box - BBox*):**
   - Toda generación debe definir un BBox en formato WGS 84 (`[min_lat, min_lon, max_lat, max_lon]`).
   - Para evitar saturación de memoria y tiempos de espera excesivos en la API de Overpass, el área máxima por lote no debe exceder $4.0\text{ km}^2$ ($2\text{km} \times 2\text{km}$) en entornos urbanos densos.
2. **Escala Voxel Métrica Determinista:**
   - La conversión espacial debe mantener estrictamente la escala $1:1$: $1\text{ bloque voxel} = 1.0\text{ metro cúbico real}$.
3. **Mapeo de Alturas y Niveles de Edificios:**
   - Si una edificación en OpenStreetMap carece del tag `height`, la altura debe derivarse deterministamente del tag `building:levels` multiplicando por $3.5\text{ metros}$ por piso (residencial) o $4.0\text{ metros}$ (comercial).

---

## 2. Reglas de Terreno y Modelos de Elevación (DEM)

1. **Interpolación Bilineal de Elevación:**
   - Las muestras de elevación (Copernicus / SRTM / ALOS) deben interpolarse bilinealmente para evitar saltos escalonados o terrazas artificiales en laderas continuas.
2. **Nivel del Mar y Cuerpos de Agua:**
   - Todo polígono con tag `natural=water` o `waterway=riverbank` debe aplanarse a la cota hidrográfica local con profundidad mínima de 2 a 3 bloques de agua.

---

## 3. Reglas de Exportación e Interoperabilidad 3D

1. **Integridad de Formatos:**
   - Los mundos voxel deben ser compatibles con el formato de región Anvil (`.mca`) para Minecraft Java, LevelDB para Bedrock, y mallas optimizadas OBJ/GLB para Three.js / Blender.
2. **Optimización de Mallas (*Greedy Meshing*):**
   - En la exportación a OBJ/GLB, las caras coplanares de vóxeles contiguos del mismo material deben fusionarse (*greedy meshing*) para reducir la cantidad de polígonos en un $80\%-90\%$.
