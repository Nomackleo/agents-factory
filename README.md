# Agent Factory Ecosystem

**Workspace para la Construcción de Stacks de IA Empresariales.**

Este archivo mantiene el registro de la arquitectura de alto nivel. La fuente de verdad estricta para la memoria y navegación de los agentes está indexada relacionalmente vía **Codebase-Memory-MCP** (SQLite), garantizando precisión absoluta y máxima economía de tokens al evitar alucinaciones. Por su parte, la herramienta **graphify** opera como un ejecutable portable en la matriz de la fábrica, encargado del renderizado bidireccional de diagramas (C4/Mermaid) para el ecosistema humano (Docs-as-Code).

## Arquitectura (Universal Antigravity Template)
- `bin/`: Scripts ejecutables de validación e inicialización.
- `brain/`: Toma de decisiones del supervisor (`routing-matrix.json`, `models.yml`).
- `implicit/`: Reglas y contexto de negocio (ISO, SOC 2, DORA, `GEMINI.md`).
- `knowledge/`: Base de datos vectorial y bibliografía base para prompts de alto nivel.
- `mcp/`: Servidores de extracción de datos y actuadores.
- `plugins/`: Skills de ingeniería encapsulados (Supervisor, Gatherer, Architect, Crispe-Generator).
- `scratch/`: Archivos temporales y artefactos de sesión.

## Registro de Cambios (Change Log)
- **Fase 1 MVP:** Establecimiento de la arquitectura Universal Antigravity Template (sin Docker). Inicialización del enrutador y componentes implícitos.
- **Fase 2 MVP:** Integración del Motor de Prompts de Alto Rendimiento (Neo-CRISPE) en `03-crispe-generator`. Incorporación de heurísticas de *Token Economy* (Google 2025) y envoltura semántica XML (Claude).
- **Fase 3 Ecosystems:** Despliegue de arquitecturas RAG estandarizadas (`docs-as-code-ecosystem`, `cinema-ad-design-ecosystem`, `multimedia-data-ecosystem`) integrando NotebookLM. Implementación de guardián de calidad QA (`workflow-auditor-agent`) y motor estricto de JSON paramétrico para Gemini Flash Image y Nano Banana Pro.

## Topología y Flujo de Datos Global (Graphify ASCII Map)

```text
======================================================================================
                          ANTIGRAVITY AGENT FACTORY
======================================================================================

 [ INGESTA HUMANA / RAG ]                  [ CORE SYSTEM (Supervisión & Reglas) ]
 +----------------------+                  +------------------------------------+
 |                      |                  |  > workflow-auditor-agent          |
 |    NotebookLM (UI)   |                  |  > brain/ (Routing Matrix)         |
 |  - Source Grounding  |=================>|  > implicit/ (ISO 25010, SOC 2)    |
 |  - Data Triangulation|    JSON / MD     |  > knowledge/ (Neo-CRISPE Vector)  |
 |                      |   Strict Auth    +------------------------------------+
 +----------------------+                                  |
            ^                                              |
            | (Templates)                                  v
 +----------------------+                  +------------------------------------+
 | notebooklm-templates/|                  |   AGENTS FACTORY (Ecosistemas)     |
 |  > notebook-inst.    |                  |                                    |
 |  > chat-inst.        |                  |  [1] docs-as-code-ecosystem/       |
 |  > studio-inst.      |                  |      - sre-architect               |
 +----------------------+                  |      - legal-advisor               |
                                           |      - incident-responder          |
                                           |                                    |
                                           |  [2] cinema-ad-design-ecosystem/   |
                                           |      - aaa-visual-decoder          |
                                           |      - gemini-flash-image-creator  |
                                           |                                    |
                                           |  [3] multimedia-data-ecosystem/    |
                                           |      - audio-creator               |
                                           |      - video-creator (Omni)        |
                                           +------------------------------------+
                                                           |
                                                           v
                                         +------------------------------------+
                                         |         OUTPUT RENDERIZADO         |
                                         |  (Markdown, JSON PPTX, Media API)  |
                                         +------------------------------------+
```

## El Motor Interno de la Fábrica (Core Plugins Engine)

El núcleo constructor de *Antigravity Agent Factory* opera mediante un flujo de orquestación multi-agente (`plugins/`). El **patrón óptimo para la creación de ecosistemas** exige que ninguna arquitectura se levante de forma manual; todo debe atravesar la siguiente cadena de montaje (Hook-Chain) para garantizar el acoplamiento ISO, DORA y la taxonomía *kebab-case*.

### Flujo de Construcción de Ecosistemas (ASCII Build Pattern)

```text
 [ USUARIO / REQUERIMIENTO ]
             |
             v
 +-------------------------+     [ routing-matrix.json ]
 | 00-supervisor-router    | <== (Valida y Enruta)
 | (Puerta de Enlace)      |
 +-------------------------+
             |
      [ JSON Payload ] ======> (Handoff-Validator.py hook)
             |
             v
 +-------------------------+     [ vector-store local ]
 | 01-research-gatherer    | <== (Extracción de papers / manuales de prompting)
 | (Data Exegética)        |
 +-------------------------+
             |
             v
 +-------------------------+     [ brain/models.yml ]
 | 02-workflow-architect   | <== (Asignación de roles y métricas SPACE/DORA)
 | (Topología y Nodos)     |
 +-------------------------+
             |
             v
 +-------------------------+     [ Output a agents-factory/ ]
 | 03-crispe-generator     | ==> - SKILL.md (Neo-CRISPE XML)
 | (The Builder Agent)     |     - rules/ y workflows/
 +-------------------------+     - notebooklm-templates/
```

### Roles y Hooks del Sistema
1. **`00-supervisor-router`**: Analiza el requerimiento base y encapsula las directivas en un `JSON Payload`. Este payload actúa como un "contrato estricto" (verificado por `bin/handoff-validator.py`) que previene inyecciones o desvíos del marco de trabajo a lo largo del pipeline.
2. **`01-research-gatherer`**: Ingiere el payload y se conecta a `knowledge/` para fundamentar empíricamente la construcción. Por ejemplo, si se va a crear un agente de *Data Science*, este nodo extrae metodologías estadísticas comprobadas antes de que el agente siquiera sea diseñado.
3. **`02-workflow-architect`**: Diseña la estructura lógica (incluyendo diagramas Mermaid y flujos de estado). Si el usuario requiere usar **NotebookLM**, el Arquitecto reserva el espacio para la carpeta `notebooklm-playbooks/` o `notebooklm-templates/` y selecciona el LLM adecuado según `models.yml`.
4. **`03-crispe-generator`**: Es el eslabón final y físico. Transforma el plano arquitectónico en archivos `.md` utilizando el framework **Neo-CRISPE** (Capacity, Role, Instruction, Schema, Personality, Examples). Al escribir directamente en `agents-factory/`, sella el componente con las variables inmutables del sistema (ISO 25010, regla de los 5 interrogantes).
