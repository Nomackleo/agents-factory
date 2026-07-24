# NotebookLM 2026: Manual de Playbooks y Algoritmos (RAG & Studio)

Este documento contiene el contexto rector para el `03-crispe-generator`. Describe las capacidades de la plataforma NotebookLM (versión 2026) y las directrices para la creación de "Algoritmos de Chat" y "Prompts de Studio" manuales.

## 1. Algoritmos de Chat RAG (Razonamiento y Triangulación)

NotebookLM 2026 ahora incluye **Secure Cloud Code Execution** (ejecución de código en la nube para procesar datos locales) y **Chat-driven Source Discovery**.

### Directrices para el Prompt Generator

- **Triangulación Exegética:** Los prompts generados deben instruir al usuario para que pida a NotebookLM cruzar información entre sus documentos subidos ("Sources") y la búsqueda en tiempo real, exigiendo citación estricta en línea.
- **Data Normalization:** El algoritmo de chat debe incluir pasos para pedir a NotebookLM que ejecute código interno para limpiar y normalizar datos desestructurados antes de su análisis cualitativo.
- **Exportación de Datos:** Los prompts deben especificar salidas en formatos soportados: `JSON`, `CSV`, `XLSX` (Excel).

## 2. Prompts de Studio (Generación Multimedia y Visualización)

NotebookLM Studio 2026 es el motor de reportes y gráficas.

### Directrices para Dirección de Arte Visual

- **Grids y Layouts:** Los prompts deben instruir al usuario para generar assets gráficos usando los estilos nativos de Studio: `Bento Grid`, `Scientific`, o `Instructional`.
- **Representación Gráfica de Datos:** Instruir explícitamente qué tipo de gráfica solicitar al Studio (ej. "Genera un gráfico de dispersión en SVG sobre la tendencia X"). Formatos de imagen exportables: `PNG`, `SVG`, `GIF`, `JPG`.
- **Estilo Tipográfico y Color:** Los prompts de Studio deben contener una sección explícita donde el usuario defina:
  - Paleta cromática (códigos HEX / RGB).
  - Tipografía (Fuentes Sans-Serif / Serif corporativas).
  - Tono visual general (ej. Minimalista, Corporativo, Dark Mode).

## 3. Arquitectura de Salida (`notebooklm-playbooks/`)

Cuando el usuario indique el flujo NotebookLM, los generadores no escribirán `SKILL.md` ejecutables localmente, sino que generarán una carpeta `notebooklm-playbooks/` conteniendo:

- `01-rag-algorithms.md` (Prompts para el chat de NotebookLM).
- `02-studio-design.md` (Prompts para el panel Studio y visualización).
