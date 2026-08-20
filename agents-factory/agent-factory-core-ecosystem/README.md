# Agent Factory Core Ecosystem — Google ADK Meta-Orchestration Architecture

**Autoría Oficial:** Leonel Salcedo (Nomack Studio)  
**WHAT**: Ecosistema Agéntico Maestro de Creación, Administración y Meta-Orquestación de Sistemas de Agentes y Workflows Multi-Agente basado en **Google Agent Development Kit (ADK)** (`google/adk-docs`).  
**Principios Rectores:** Acoplamiento No Invasivo, Optimización Continua, Tipado Estricto de Herramientas, Workflows Deterministas/Dinámicos y Evaluación Sistemática.  
**Cumplimiento Normativo:** ISO 9001:2015, ISO 42001 (AIMS - Artificial Intelligence Management System), ISO 25010 (Calidad y Fiabilidad de Software), ISO 27001 (ISMS), DORA & `implicit/`.

---

## 1. Misión y Alcance del Ecosistema

El **Agent Factory Core Ecosystem** funciona como la capa de ingeniería agéntica de élite de Antigravity. Su propósito no es sustituir ni alterar los flujos funcionales existentes, sino **optimizar, gobernar y potenciar** a todos los demás ecosistemas (`software-engineering`, `minimal-coding`, `cybersecurity`, `frontend-angular`, `cgi-web`, `ui-ux-design`, etc.):

1. **Arquitectura de Agentes de Alto Rendimiento:** Diseño estandarizado de `LlmAgent` con instrucciones Neo-CRISPE v2.0, definición de roles, prompts de sistema y gestión de subagentes.
2. **Orquestación de Workflows Multi-Agente:** Implementación de patrones deterministas y dinámicos:
   - **`SequentialAgent`:** Flujos lineales paso a paso sin pérdida de contexto.
   - **`ParallelAgent`:** Ejecución concurrente (*Scatter-Gather*) para procesamiento masivo de datos.
   - **`LoopAgent` (Evaluator-Optimizer):** Ciclos iterativos de generación y crítica contra rúbricas de calidad.
   - **`StateGraph`:** Grafos de estado con bifurcaciones condicionales y puntos de control *Human-in-the-Loop* (HITL).
3. **Integración Tipada de Herramientas y Servidores MCP:** Estandarización de contratos de datos con JSON Schema y Pydantic, reintentos exponenciales y tolerancia a fallos.
4. **Evaluación Automatizada & Benchmarking (LLM-as-a-Judge):** Auditoría sistemática de fidelidad, tiempos de respuesta y optimización continua de prompts.

---

## 2. Topología del Ecosistema

```
agents-factory/agent-factory-core-ecosystem/
├── README.md
├── .agents/
│   ├── rules/
│   │   └── adk-core-rules.md
│   └── skills/
│       ├── adk-agent-architect/
│       ├── adk-evaluator-and-optimizer/
│       ├── adk-tool-and-mcp-integrator/
│       └── adk-workflow-orchestrator/
├── brain/
└── knowledge/
    ├── adk_workflow_templates_reference.py
    └── google_adk_multiagent_architecture_mastery.md
```

---

## 3. Matriz de Delegación de Subagentes

| Tarea Requerida | Subagente Especializado | Entrada / Salida |
| :--- | :--- | :--- |
| Diseño y configuración de nuevos agentes o subagentes LLM | `adk-agent-architect` | Requerimiento funcional -> Definición `LlmAgent` + Prompt Neo-CRISPE |
| Orquestación de pipelines (Secuencial, Paralelo, Loop, Grafo) | `adk-workflow-orchestrator` | Topología de tareas -> Código de Workflow ADK ejecutable |
| Tipado estricto de herramientas, reintentos y binding MCP | `adk-tool-and-mcp-integrator` | Esquemas de API/Funciones -> Contratos tipados y Tool handlers |
| Auditoría de calidad, benchmarking y optimización de prompts | `adk-evaluator-and-optimizer` | Trazas/Respuestas de agentes -> Informe de evaluación + Prompts refinados |
