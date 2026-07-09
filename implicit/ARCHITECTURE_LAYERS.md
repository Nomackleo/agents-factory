# Las 5 Capas de Arquitectura de la Fábrica

Todo ecosistema generado o ejecutado dentro de la Fábrica de Antigravity debe estructurarse y validarse a través de estas cinco capas fundamentales para garantizar seguridad (Zero Trust), determinismo y calidad a nivel empresarial.

## 1. Capa de Identidad
Define de manera unívoca el "Quién" (Roles estrictos). Cada subagente en el ecosistema debe poseer una firma (`SKILL.md`) con un propósito inmutable. El modelo no debe asumir roles múltiples que crucen dominios (ej. un auditor de código no puede compilar y ejecutar simultáneamente).

## 2. Capa de Entrada (Ingesta)
Define el "Qué" y valida la pureza del contexto. 
- **Sanitización Obligatoria:** Todo documento externo, fragmento de código de repositorios o input humano debe pasar por el `04-security-sanitizer`.
- **Prevención de Inyecciones:** Se bloquean y escanean activamente textos ofuscados (Base64, Unicode oculto) e intentos de redirección de datos (ej. variables enviando logs a correos electrónicos no verificados).

## 3. Capa de Ejecución
Define el "Dónde" y "Cómo" bajo estricto aislamiento.
- **Sandboxing:** Todo código generado o ejecutado debe limitarse al directorio `agents-factory/` o al `scratch/`.
- **Validación de Conexiones Web (HITL):** Cualquier conexión saliente de la Capa de Ejecución (ej. API calls a GitHub, Google Cloud, DeepResearch, scraping web) invoca un bloqueo asíncrono requiriendo confirmación del humano mediante el sistema de triaje (Ask, Allow, Deny).

## 4. Capa de Control
Mecanismos preventivos y reactivos que gestionan la soberanía humana sobre el loop algorítmico.
- **Sistema de Triaje (Ask, Allow, Deny):** Todo requerimiento de permisos debe utilizar este patrón.
- **Dead-man Switch:** Si un agente entra en bucle, excede el `max_turns`, o pierde conexión de red durante una tarea crítica, el switch aborta la operación revirtiendo el estado y devolviendo el control al operador.

## 5. Capa de Observabilidad
- Trazabilidad y Logging determinista. Cada salto entre capas debe dejar rastro en el `corporate_context` (XML) u otras bases vectoriales del ecosistema.
