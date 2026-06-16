# Quality Gates & Compliance

Este documento establece las métricas de aceptación universales para el código y comportamiento de los agentes, basado en ISO 25010 y SOC 2.

## 1. Calidad del Software (ISO 25010 adaptado)
- **Eficiencia de Desempeño:** Los scripts y prompts generados (`03-crispe-generator`) deben optimizar el consumo de tokens y latencia.
- **Fiabilidad y Seguridad (ISO 27001 / SOC 2):** Cero comandos de escritura destructivos sin aprobación. Validación estricta de esquemas.

## 2. Métricas de Entrega (DORA & SPACE)
- **Deployment Frequency:** Alta agilidad en la creación de ecosistemas.
- **Lead Time for Changes:** Mínimo tiempo desde el requerimiento hasta el ecosistema funcional.
- **Change Failure Rate:** Minimizado a través del script `handoff-validator` y TDD.
