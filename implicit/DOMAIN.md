# Contexto de Negocio: Fábrica de Agentes Corporativos

Este workspace es el núcleo de orquestación y construcción de ecosistemas de agentes de Inteligencia Artificial (Agentic Stacks) orientados de forma exclusiva al sector **Tech, Datos y Startups**.

## 1. Naturaleza de la Salida (Outputs)
- **Calidad de Producción:** Todo ecosistema, código, prompt o flujo generado aquí se considera "código de producción". No hay lugar para prototipos frágiles. Se exige eficiencia algorítmica y alta cohesión.
- **Flexibilidad Semántica y Temperatura (Creatividad vs Lógica):** El rigor absoluto (Temperatura/Top-P en valores cercanos a 0) se reserva ESTRICTAMENTE para: auditorías, TDD/Testing, documentos legales, y cumplimiento de normas/frameworks (ISO, SOC2, DORA). Para la gran mayoría de ecosistemas (ej. creación de campañas de marketing, diseño de personajes, lluvia de ideas, y *coding* exploratorio) se **debe mantener una creatividad paramétrica y temperatura fluida**. Restringir el vocabulario de manera dogmática vuelve a los agentes rígidos e incapaces de innovar o resolver problemas laterales.
- **Tono y Argumentación:** Las comunicaciones de los agentes y la documentación generada deben mantener un tono exegético (explicativo, profundo) y la máxima calidad argumentativa. El rigor es innegociable.
- **Empaquetamiento:** Los ecosistemas generados deben ser agnósticos a la plataforma final y empaquetables de manera aislada (ej. Docker), preservando la seguridad y portabilidad.

## 2. Restricciones del Dominio (Principios Normativos)
Aunque no se mencione explícitamente la nomenclatura en el código generado, todos los sistemas deben adherirse a:
- **Seguridad y Privacidad de la Información:** Manejo estricto de secretos, cero hardcoding de credenciales, y aislamiento en entornos de ejecución (Sandboxing). Las salidas de los agentes externos no son confiables por defecto (Prevención de Prompt Injection Indirecto).
- **Gestión de la Calidad del Software:** Las instrucciones de los agentes (`SKILL.md`) deben optimizar latencia, reducir consumo de tokens, y definir esquemas deterministas que garanticen mantenibilidad a escala.
- **Confianza en la IA:** El comportamiento de los agentes debe ser auditable y transparente. Cada ecosistema debe incluir un registro de por qué tomó ciertas decisiones y prever sesgos.

## 3. Topología Obligatoria
Todo ecosistema de agentes generado en `agents-factory/` debe poseer obligatoriamente su propio enrutamiento, base de conocimiento y reglas de validación en formato JSON Schema/XML. La comunicación entre agentes (Handoffs) requiere validación estricta de esquema en el origen y destino.
