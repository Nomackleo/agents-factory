# Design Tooling MCP Integration (Figma & Google Stitch)

**WHAT**: Servidores MCP para integración de herramientas de diseño en la nube (Figma y Google Stitch) con los ecosistemas de Antigravity.

---

## 1. Servidores MCP Incluidos

### A. Figma MCP (`figma`)
* **Paquete:** `@modelcontextprotocol/server-figma`
* **Variables de Entorno:**
  - `FIGMA_ACCESS_TOKEN`: Token de acceso personal generado en la configuración de cuenta de Figma (*Settings -> Personal access tokens*).
* **Capacidades:** Extracción de tokens de diseño, lectura de árboles de nodos, inspección de propiedades Auto Layout y exportación de assets.

### B. Google Stitch MCP (`stitch`)
* **Paquete:** `@google/stitch-mcp-server`
* **Variables de Entorno:**
  - `STITCH_API_KEY`: Clave de API de Google Stitch.
  - `STITCH_PROJECT_ID`: Identificador del proyecto de Stitch.
* **Capacidades:** Síntesis visual rápida, generación de prototipos y validación de componentes de UI.

---

## 2. Activación en el IDE o Global

Para activar estos servidores en tu entorno de Antigravity, copia las entradas de `mcp_config_snippet.json` dentro de tu configuración de MCP (`mcp_config.json` o configuración de Antigravity IDE) y define las variables de entorno correspondientes.
