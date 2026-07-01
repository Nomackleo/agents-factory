# Quality Gates & Compliance Metrics

Este documento establece las barreras de aceptación universales para todos los componentes (prompts, código, esquemas) generados por los agentes dentro de la Fábrica. 

## 1. Criterios de Rendimiento y Estabilidad (DORA Metrics)
El pipeline de generación y los ecosistemas resultantes serán evaluados bajo:
- **Deployment Frequency (Frecuencia de Despliegue):** La arquitectura de subagentes y la paralelización de tareas (Research -> Architect -> Builder) debe estar diseñada para entregar stacks en tiempo mínimo.
- **Lead Time for Changes:** Alta agilidad de respuesta ante modificaciones. Re-generación de flujos sin pérdida de contexto.
- **Change Failure Rate (Tasa de Fallos):** Se exige minimizar los fallos mediante TDD (Test-Driven Development) y validadores estrictos antes de escribir en disco.
- **Time to Restore Service:** En caso de fallos de handoff (errores de formato JSON/XML), el agente responsable debe auto-corregir inmediatamente utilizando el feedback del loop de auditoría.

## 2. Eficiencia y Flujo de Trabajo (SPACE Framework)
- **Satisfacción y Bienestar:** La documentación para el *Human-in-the-loop* debe ser prístina. Reducción drástica del "ruido" en logs y mensajes.
- **Rendimiento Algorítmico:** Optimización del consumo de tokens. Regla innegociable: no pasar contextos redundantes. Utilizar resúmenes y extracción focalizada.
- **Flujo de Ejecución:** Los agentes no deben quedarse bloqueados. Se debe aplicar un esquema claro de timeout y fallback si una herramienta externa o base de datos falla.

## 3. Barreras de Seguridad (Security Gates)
- **Validación Estricta:** Cero confianza. Todo input o resultado de herramienta web se debe sanitizar antes de inyectarse al contexto del Supervisor.
- **Non-Destructive Enforcement:** Bloqueo absoluto de operaciones de escritura destructivas fuera del directorio aislado `agents-factory/` o `scratch/` sin aprobación explícita del Human-in-the-loop.
- **Interoperabilidad:** Todo intercambio de datos entre subagentes requiere la definición de la estructura `<schema>` en el output y un validador que compruebe la coincidencia de llaves antes de avanzar.
