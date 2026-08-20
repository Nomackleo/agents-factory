# Google Agent Development Kit (ADK) — Arquitectura y Patrones de Orquestación Multi-Agente

**Referencia Oficial:** Google DeepMind / Google ADK Team (`google/adk-docs`)  
**Propósito:** Marco técnico de referencia para el diseño, orquestación, integración de herramientas, ejecución y evaluación de sistemas de agentes de inteligencia artificial de nivel empresarial.  
**Cumplimiento Normativo:** ISO 42001 (AIMS), ISO 25010 (Fiabilidad y Mantenibilidad), DORA.

---

## 1. Tipología de Agentes Fundacionales en Google ADK

```
                               ┌─────────────────────────────┐
                               │       BaseAgent (Core)      │
                               └──────────────┬──────────────┘
                                              │
         ┌─────────────────────┬──────────────┴─────┬─────────────────────┐
         ▼                     ▼                    ▼                     ▼
   [ LlmAgent ]       [ SequentialAgent ]   [ ParallelAgent ]      [ LoopAgent ]
   - Generación LLM   - Pipeline lineal     - Scatter-Gather       - Evaluator-
   - Tools & Callbacks- Paso a paso         - Concurrente            Optimizer
   - Sub-agents       - Preserva contexto   - Agregación           - Hasta score >= umbral
```

### A. `LlmAgent`
El componente atómico inteligente. Encapsula:
* `model`: Nombre o identificador del modelo (ej. `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-flash-latest`).
* `instruction`: Directiva de sistema / prompt estructurado en Neo-CRISPE v2.0.
* `description`: Resumen semántico conciso de capacidades para permitir enrutamiento automático desde coordinadores padres.
* `tools`: Lista de herramientas ejecutables, funciones tipadas o `AgentTool` para delegación explícita.
* `sub_agents`: Lista de agentes especialistas subordinados.

---

## 2. Los 4 Patrones Maestros de Workflows Multi-Agente

### Patrón 1: Coordinador y Despachador (Coordinator & Dispatcher)
Un agente central recibe la solicitud del usuario, analiza la intención semántica y delega al subagente especialista adecuado mediante `transfer_to_agent`:

```python
from google.adk.agents import LlmAgent

# Especialistas subordinados
code_specialist = LlmAgent(name="CodeSpecialist", description="Experto en refactorización y depuración de código.")
security_specialist = LlmAgent(name="SecuritySpecialist", description="Experto en auditoría de vulnerabilidades e ISO 27001.")

# Agente Coordinador Maestro
coordinator = LlmAgent(
    name="MasterDispatcher",
    model="gemini-1.5-pro",
    instruction="Analiza la solicitud y enruta al especialista correspondiente.",
    description="Coordinador general del sistema.",
    sub_agents=[code_specialist, security_specialist]
)
```

### Patrón 2: Pipeline Secuencial (Sequential Pipeline / Chain)
Encadena múltiples agentes donde la salida de uno es la entrada enriquecida del siguiente:

```python
from google.adk.agents import SequentialAgent, LlmAgent

researcher = LlmAgent(name="Researcher", instruction="Investiga a fondo y extrae datos clave.")
writer = LlmAgent(name="Writer", instruction="Redacta un informe ejecutivo con los datos obtenidos.")
formatter = LlmAgent(name="Formatter", instruction="Formatea en Markdown limpio con tablas y alertas.")

editorial_pipeline = SequentialAgent(
    name="EditorialChain",
    agents=[researcher, writer, formatter]
)
```

### Patrón 3: Colaboración Paralela (Parallel / Scatter-Gather)
Ejecuta múltiples agentes en paralelo para analizar diferentes dimensiones de un problema y luego consolida los resultados:

```python
from google.adk.agents import ParallelAgent, LlmAgent

accessibility_auditor = LlmAgent(name="AccessibilityAuditor", description="Audita contraste WCAG 2.1.")
security_auditor = LlmAgent(name="SecurityAuditor", description="Audita dependencias y permisos.")
performance_auditor = LlmAgent(name="PerformanceAuditor", description="Audita tiempo de carga y FPS.")

parallel_audit_workflow = ParallelAgent(
    name="ComprehensiveAudit",
    agents=[accessibility_auditor, security_auditor, performance_auditor]
)
```

### Patrón 4: Bucle de Refinamiento Iterativo (Loop / Evaluator-Optimizer)
Un generador produce una solución y un evaluador la califica contra una rúbrica estricta. El bucle se repite hasta que la solución alcance el umbral de calidad definido:

```python
from google.adk.agents import LoopAgent, LlmAgent

generator = LlmAgent(name="DraftGenerator", instruction="Genera la primera versión del código o documento.")
evaluator = LlmAgent(name="CriticEvaluator", instruction="Evalúa el código contra la ISO 25010 y emite score de 0 a 1.0.")

iterative_refinement = LoopAgent(
    name="EvaluatorOptimizerLoop",
    agents=[generator, evaluator],
    max_iterations=5
)
```

---

## 3. Callbacks de Ciclo de Vida y Políticas de Seguridad

Google ADK permite registrar interceptores en puntos críticos del ciclo de vida del agente:

1. `before_model_callback`: Permite inyectar contexto en tiempo real, filtrar entradas maliciosas (Prompt Injection) o truncar tokens antes de enviar al LLM.
2. `after_tool_callback`: Audita la salida de las herramientas, valida el esquema de respuesta y sanitiza datos sensibles antes de que el agente continúe.
3. `on_step`: Emite eventos de telemetría para observabilidad y trazabilidad completa de la ejecución.

---

## 4. Evaluación Sistemática con LLM-as-a-Judge

La evaluación en ADK mide 4 dimensiones clave:
* **Fidelidad Semántica:** ¿Cumple con la totalidad de los requerimientos del usuario?
* **Adherencia a Restricciones:** ¿Respeta los formatos, estructuras y normas de seguridad exigidas?
* **Eficiencia de Ejecución:** ¿Cuántos pasos y tokens utilizó para resolver la tarea?
* **Tasa de Éxito de Herramientas:** ¿Las llamadas a herramientas fueron precisas y libres de errores sintácticos?
