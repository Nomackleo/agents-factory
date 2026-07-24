# Contexto de Negocio: Fábrica de Agentes Corporativos

Este workspace es el núcleo de orquestación y construcción de ecosistemas de agentes de Inteligencia Artificial (Agentic Stacks) orientados de forma exclusiva al sector **Tech, Datos, Startups y Empresas Corporativas**.

---

## 1. Naturaleza de la Salida (Outputs)

- **Calidad de Producción:** Todo ecosistema, código, prompt o flujo generado aquí se considera "código de producción". No hay lugar para prototipos frágiles. Se exige eficiencia algorítmica, alta cohesión y alineación con los marcos **NIST CSF 2.0, ISO 42001 (AIMS), ISO 27001 (ISMS) y DORA**.
- **Flexibilidad Semántica y Temperatura (Creatividad vs Lógica):** El rigor absoluto (Temperatura/Top-P en valores cercanos a 0 o `thinking_level: low`) se reserva ESTRICTAMENTE para auditorías, TDD/Testing, documentos legales, y cumplimiento normativo. Para la ideación, diseño visual, y *coding* exploratorio se mantiene una creatividad paramétrica y temperatura fluida con `thinking_level: medium/high`.
- **Tono y Argumentación:** Las comunicaciones de los agentes y la documentación generada deben mantener un tono exegético (explicativo, profundo) y la máxima calidad argumentativa. El rigor es innegociable.
- **Empaquetamiento e Aislamiento:** Los ecosistemas en `agents-factory/` son agnósticos a la plataforma final. Cada entregable de cliente se aísla en `projects/<nombre-proyecto>/` como un repositorio Git independiente.

---

## 2. Restricciones del Dominio (Principios Normativos)

Todos los sistemas deben adherirse rigurosamente a:

- **NIST CSF 2.0 & ISO 27001 (Seguridad y Privacidad):** Manejo estricto de secretos en `PreToolUse`, cero hardcoding de credenciales, y aislamiento en entornos de ejecución (Sandboxing). Las salidas externas no son confiables por defecto (Sanitización contra Prompt Injection Indirecto).
- **ISO 42001 (Gobernanza y Confianza en IA):** El comportamiento de los agentes debe ser auditable y transparente. Cada handoff entre agentes exige un contrato de datos XML (`<corporate_context>`, `<reasoning_trace>`) y registro de decisiones.
- **DORA (Resiliencia Digital):** Optimización de latencia, reducción drástica del consumo de tokens (Token Economy vía `Codebase-Memory-MCP` SQLite), y tolerancia a fallos mediante conmutación automática de modelos (`gemini-3.6-flash`).

---

## 3. Topología Obligatoria

Todo ecosistema agéntico generado en `agents-factory/` debe poseer obligatoriamente su propio enrutamiento, base de conocimiento y reglas de validación en formato JSON Schema/XML. Los entregables finales de proyecto se compilan en `projects/` garantizando un aislamiento total del código core de la fábrica.
