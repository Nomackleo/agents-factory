# Workflow: Documentación Visual y Branded Docs

Este workflow complementa el ciclo estándar de Docs-as-Code para abarcar formatos de presentación visual, dashboards y documentos ejecutivos (ej. `.pptx`, `.docx`, `SVG`). Aplica cuando la salida trasciende el estándar `.md` y requiere integraciones con motores de difusión (Nano Banana Pro 2) y librerías de compilación visual.

## Fases del Loop Visual

### 1. Ingesta y Recolección de Marca (Brand Requirements)
- **Agente:** `brand-requirements-gatherer`
- **Acción:** Escanea el chat (Media, Mentions) o la ruta `assets/branding/` del proyecto.
- **Proceso:** Extrae el Logo, Sujeto, Acción, Paleta de Colores, Entorno y Composición. Si la información es ambigua, inyecta el **Template por Defecto** (ej. Estilo Corporativo Limpio para `.pptx`).

### 2. Estructuración del Payload API (Decoding)
- **Agente:** `multimedia-payload-structurer`
- **Acción:** Recibe el *Brand Checklist* y los datos de contexto (Knowledge/RAG).
- **Proceso:** Construye el JSON estricto (`GenerateContentConfig` y `ImageConfig`) para invocar el API del modelo de imagen (ej. Gemini 3 Pro Image / Nano Banana). 
- **Restricciones inyectadas:** `aspect_ratio` (16:9/4:3), `image_size` (2K/4K), `thinking_config: HIGH`, y `temperature: 1.0` de forma estricta. Aplica técnicas de *Exact Text Rendering* para tipografías incrustadas.

### 3. Sanitización y Renderizado Final (Compilation)
- **Agente:** `visual-data-renderer`
- **Acción:** Analiza la data extraída y las imágenes devueltas por la API generativa.
- **Proceso:** 
  - Realiza la **Sanitización de Datos** para evitar solapamientos visuales (ruido en grids).
  - Ejecuta código de compilación utilizando librerías Open Source aprobadas (`PptxGenJS`, `python-pptx`, `Typst`, `Pandoc`, `AntV`, o `Mermaid.js`).
- **Verificación:** Produce el archivo físico `.pptx`, `.docx` o `.svg` en el *workspace* de salida.

## Interacción con el Auditing Loop General
Este flujo opera íntegramente bajo las directrices del [auditing-loop.md](../workflows/auditing-loop.md):
- El **Supervisor** coordina los handoffs entre el *Gatherer*, el *Structurer* y el *Renderer*.
- Se mantiene el *Turn-Based Execution* y los límites de *Max Budget* para evitar bucles infinitos intentando renderizar una imagen fallida.
