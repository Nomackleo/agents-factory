# Integración y Control Agéntico de Herramientas Creativas (Blender, DaVinci Resolve, Affinity, Maxon Autograph, OTIO)

**Propósito:** Guía maestra para el control agéntico de software de creación de contenido 2D/3D, edición no lineal y postproducción mediante servidores Model Context Protocol (MCP) y APIs de scripting nativas.

---

## 1. Blender MCP: Automatización Headless con `bpy`

Blender incorpora un intérprete Python completo con el módulo nativo `bpy`.

### A. Capacidades Agénticas Vía MCP:
1. **Renderizado Headless:** Invocación de `blender --background scene.blend --python script.py` para renderizar fotogramas y secuencias con **Eevee Next** o **Cycles** sin cargar la interfaz gráfica.
2. **Generación Procedural de Geometría:** Creación algorítmica de terrenos, modificadores de deformación y distribución de instancias (*Geometry Nodes*).
3. **Exportación de Activos Web 3D:** Transpilación y compresión automática de modelos hacia `GLTF/GLB` con compresión Draco y materiales PBR listos para Three.js y HyperFrames.

---

## 2. DaVinci Resolve MCP: Scripting API de Postproducción y Color

DaVinci Resolve Studio expone una API de scripting nativa en Python/Lua a través del módulo `DaVinciResolveScript` (`fusionscript`).

### A. Capacidades Agénticas Vía MCP:
1. **Creación Automatizada de Proyectos y Timelines:** Carga de material en Media Pool, creación de pistas de video/audio y ensamble automático de secuencias.
2. **Intercambio OpenTimelineIO (OTIO) y EDL/XML:** Ingesta de listas de decisiones de edición (`edit_decisions.json`) y conversión a líneas de tiempo nativas.
3. **Etalonaje y Aplicación de LUTs:** Aplicación automática de tablas de color (LUTs `.cube`), corrección de balance de blancos y curvas de tono.
4. **Cola de Renderizado (*Render Queue*):** Configuración de trabajos de exportación H.264/ProRes y activación de renderizado por lotes.

---

## 3. Maxon Autograph & Compositores Node-Based (Natron / Synfig)

* **Maxon Autograph:** Renderizado por línea de comandos (`autograph-render`) e interpolación de parámetros en proyectos basados en capas y nodos.
* **Natron (Open Source Node-Based Compositor):** Motor de composición por nodos alternativo a Nuke/After Effects. Permite incrustación por croma (*chroma keying*), rotoscopia procedural y efectos ópticos mediante su API de Python y modo CLI.
* **Synfig Studio / OpenToonz:** Renderizado por lotes de animación vectorial tradicional y corte plano.

---

## 4. Affinity Suite, Inkscape CLI & ImageMagick

* **Affinity Suite (Designer, Photo, Publisher):** Flujos de trabajo basados en intercambio de formatos estándar (SVG, PDF, PSD, TIFF).
* **Inkscape CLI:** Renderizado vectorial hiperrápido de personajes y fondos SVG generados por `Ink Theater` hacia mapas de bits PNG de alta resolución.
* **ImageMagick:** Procesamiento por lotes de texturas, aplicación de filtros HALD CLUT y generación de canales alfa limpios.

---

## 5. Estándar de Intercambio Universal: OpenTimelineIO (OTIO)

OpenMontage genera líneas de tiempo en formato canónico **OpenTimelineIO (`.otio`)**, permitiendo que cualquier proyecto iniciado por un agente de IA pueda abrirse, editarse o finalizarse indistintamente en:
- DaVinci Resolve Studio
- Blender Video Sequence Editor (VSE)
- Adobe Premiere Pro / Final Cut Pro (vía convertidor FCPXML)
- HyperFrames / Remotion web runners
