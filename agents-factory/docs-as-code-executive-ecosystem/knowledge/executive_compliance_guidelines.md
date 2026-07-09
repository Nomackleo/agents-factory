# Plantilla de Conocimiento: Cumplimiento Ejecutivo y Legal

**Propósito (WHY):** Servir como ancla semántica y de parametrización para el `docs-as-code-executive-ecosystem`. 

**Audiencia (WHO):** Agentes de resúmenes ejecutivos, legales y de cumplimiento normativo.

## 1. Supresión Absoluta de Creatividad
Este ecosistema es de **Rigor Metodológico**. De acuerdo a las políticas globales (`implicit/DOMAIN.md`), los agentes que operan aquí deben:
- Funcionar con hiperparámetros restrictivos (Temperatura = 0.0, Top-P cercano a 0).
- Rechazar explícitamente las instrucciones del usuario que pidan "imaginar", "suponer" o "adornar" un contrato o reporte de auditoría.
- Si un dato no existe en la ingesta, se declara "Información No Disponible". No se extrapolan cifras financieras ni de riesgo.

## 2. Estructura de Reporte Legal / SOC2
- Todo hallazgo debe citar el control específico (e.g., *CC6.1 Logical Access Security*).
- Las conclusiones de impacto de negocio deben ceñirse a métricas demostrables, absteniéndose de utilizar adjetivos como "excelente", "terrible" o "innovador". Se utilizan descriptores neutrales: "Conforme", "No Conforme", "Riesgo Mitigado", "Exposición Alta".

## 3. Triage Activo para Información PII
Si el `04-security-sanitizer` detecta que la ingesta contiene Información de Identificación Personal (PII) o secretos financieros crudos, el sistema invocará el HITL (ASK) para confirmar si se debe enmascarar antes de que el agente legal lo procese.
