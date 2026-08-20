# Reglas Operacionales de Integración MCP (Figma & Stitch)

**Alcance:** Invocación de herramientas `@mcp:figma` y `@mcp:stitch` en `ui-ux-design-ecosystem`  
**Normativa:** ISO 27001 (Protección de Credenciales), ISO 25010 (Eficiencia y Confiabilidad), DORA.

---

## 1. Reglas de Invocación de Figma MCP

1. **Extracción Quirúrgica por Nodos:**
   - Evitar llamadas a `get_file` sobre documentos masivos de cientos de páginas. Priorizar siempre `get_node` especificando el `node_id` exacto del componente o frame requerido para evitar saturación de memoria.
2. **Normalización Automática a DESIGN.md:**
   - Todos los colores extraídos de Figma deben convertirse a formato HEX de 6 dígitos (`#RRGGBB`) y evaluarse contra la fórmula de contraste WCAG 2.1 AA/AAA antes de integrarse en la especificación del proyecto.
3. **Caché Local de Estructura:**
   - Los árboles de nodos descargados deben ser cacheados en memoria durante la sesión para evitar llamadas repetidas a la API de Figma.

---

## 2. Reglas de Invocación de Stitch MCP

1. **Validación Semántica Previa:**
   - Antes de sintetizar componentes con `mcp_stitch_generate_ui`, los tokens de color y tipografía deben ser validados contra el `DESIGN.md` activo.
2. **Reversibilidad y Verificación Humana (HITL):**
   - Cualquier operación que modifique pantallas existentes o genere prototipos de producción debe generar un resumen visual estructurado para revisión del usuario.
