# Workspace Rules & Governance — Génesis Legal (`genesislegal.co`)

> **Propósito**: Reglas persistentes de comportamiento del agente, estándares de maquetación UI y protocolo de autocuración de herramientas.

---

## 1. Protocolo Watchdog & Autocuración de Herramientas

- **Auditoría de Herramientas**: Antes de interactuar con Google Drive o Gemini Notebooks, ejecuta `python bin/watchdog_health_check.py`.
- **Auto-Healing de Google Drive**: Si el token de Google Drive expira (HTTP 401/403), el Watchdog automáticamente renovará el `access_token` usando el `refresh_token` almacenado en `C:\Users\Nomack\.gemini\antigravity-ide\mcp_oauth_tokens.json`.
- **Gemini Notebook (NotebookLM)**: Si la sesión de `nlm` indica *Authentication Expired*, ejecuta `python authenticate_notebooklm.py` para abrir la instancia de navegación y refrescar las galletas de sesión.

---

## 2. Estándares de Estilo y UI Documental

- **Autoría Oficial**: **Daniel Moncada y Leonel Salcedo — Consultoría Tecnológica e Innovación**.
- **Ejecutor Lead en Sitio**: **Leonel Salcedo**.
- **Prohibición de Alias**: Cero menciones del alias *Nomack* en cualquier entregable.
- **Portadas Institucionales**: Aplicar estrictamente la jerarquía definida en [manual_estetica_y_ui_documental.md](file:///c:/Users/Nomack/Documents/workspace/agents/antigravity/dev/prompt-generator/projects/genesis-legal/docs/01_gobernanza/manual_estetica_y_ui_documental.md):
  - Subtítulo Superior: 12pt (Ej. `REQUERIMIENTOS GÉNESIS`).
  - Título Principal (H1): 22pt **Calibri Bold** en color Azul Corporativo (`#1a3a5c`).
  - Subtítulo Inferior: 14pt.
  - Bloque `PRESENTADO A`: En Dorado (`#b8842a`) 10pt MAYÚSCULAS.
  - Entidad `GÉNESIS LEGAL`: En Azul (`#1a3a5c`) 18pt MAYÚSCULAS.
  - Bloque `Presentado por:`: Etiqueta `Presentado por:` en **Bold** y Dorado (`#b8842a`).
- **Encabezados & Pies**: Encabezado en gris con línea separadora Dorado (`#b8842a`). Pie de página en gris con línea separadora Gris (`#cccccc`).
- **Estructura Documental**: Archivos organizados exclusivamente en `projects/genesis-legal/docs/` en las carpetas `01_gobernanza/`, `02_planes_y_actas_iso/` y `03_cuestionarios/`.
