# Declaración Implícita de Herramientas MCP para UI/UX Design Ecosystem

**Alcance:** Ecosistema `ui-ux-design-ecosystem`  
**Herramientas MCP Implícitas:** `@mcp:figma`, `@mcp:stitch`  
**Normativa:** ISO 27001 (Seguridad en APIs y Tokens), ISO 9241-210 (Diseño Centrado en el Humano), DORA.

---

## 1. Conexión Implícita a Figma MCP (`@mcp:figma`)

Todos los subagentes del gremio de diseño (`design-tokens-architect`, `design-system-architect`, `figma-stitch-integrator`, `ux-flow-designer`) tienen permiso implícito para consultar e interactuar con el servidor MCP de Figma:

### Herramientas Disponibles:
1. `mcp_figma_get_file`: Descarga y recorre el árbol de nodos de un archivo de Figma (`file_key`).
2. `mcp_figma_get_node`: Extrae un componente, frame o variante específico (`node_id`).
3. `mcp_figma_extract_tokens`: Extrae variables locales de color, tipografía y espaciado para convertirlas en `DESIGN.md`.
4. `mcp_figma_inspect_autolayout`: Inspecciona propiedades de Auto Layout (dirección, padding, gap, alignment) para transpilación exacta a Flexbox/CSS Grid.

---

## 2. Conexión Implícita a Google Stitch MCP (`@mcp:stitch`)

Los subagentes utilizan `@mcp:stitch` para la síntesis visual rápida, ensamblaje de prototipos y validación estructural de interfaces:

### Herramientas Disponibles:
1. `mcp_stitch_generate_ui`: Sintetiza código de componentes o wireframes interactivos a partir de descripciones semánticas.
2. `mcp_stitch_validate_layout`: Verifica la consistencia de layout y jerarquía visual entre componentes.
3. `mcp_stitch_stitch_prototype`: Ensambla múltiples pantallas y define transiciones de navegación.

---

## 3. Protocolo de Flujo de Trabajo

```mermaid
graph LR
    A[Figma File / Node] -->|@mcp:figma| B[figma-stitch-integrator]
    B -->|Extrae Tokens| C[design-tokens-architect]
    C -->|Compila DESIGN.md| D[design-system-architect]
    D -->|Prototipado Rápido| E[@mcp:stitch]
    E -->|Valida Layout & Componentes| F[Frontend Guild / Angular]
```
