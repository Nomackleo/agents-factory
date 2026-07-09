# Plantilla de Documentación: Calidad del Producto (ISO 25010)

**Propósito (WHY):** Servir como *Ground Truth* y ejemplo estructurado (Zero-Shot Template) para el `api-documenter` y el `sre-architect` al generar documentación de componentes.

**Audiencia (WHO):** Human-in-the-Loop y Auditores Técnicos.

## Estructura Exegética Obligatoria (WHAT)

Todo documento generado por el ecosistema *Docs-as-Code* debe adherirse al siguiente esquema para asegurar la característica de **Mantenibilidad** y **Portabilidad** de la ISO 25010:

```markdown
# [Nombre del Componente o API]

## 1. Definición Funcional (Functional Suitability)
- **Objetivo Exacto:** ¿Qué problema resuelve este componente de forma aislada?
- **Restricciones:** Entradas inválidas y fronteras del sistema.

## 2. Eficiencia de Desempeño (Performance Efficiency)
- **Complejidad de Tiempo:** (Ej. O(1), O(n log n)).
- **Umbrales de Latencia (DORA):** Tiempo máximo de respuesta esperado.

## 3. Confiabilidad (Reliability)
- **Tolerancia a Fallos:** ¿Cómo se recupera si falla la dependencia X?
- **Mecanismos de Retoque (Fallback/Retry):** Describir el circuito.

## 4. Mantenibilidad (Maintainability)
- **Acoplamiento:** Lista de dependencias rígidas.
- **Trazabilidad:** Formato de logs generados por este componente.
```

## Prevención de Ruido (Heurística de Redacción)
- **Estilo:** Directo, declarativo, en voz activa.
- **Creatividad:** Apagada. No usar metáforas. Emplear términos técnicos puros.
- **Ejemplo Correcto:** "El validador de Handoff rechaza cargas útiles sin la clave `target_agent`."
- **Ejemplo Incorrecto (Ruido):** "Nuestro increíble validador es como un guardia de seguridad que amablemente revisa si la caja contiene el destino."
