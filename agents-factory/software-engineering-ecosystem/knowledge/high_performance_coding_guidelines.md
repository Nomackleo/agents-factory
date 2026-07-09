# Plantilla de Conocimiento: Alto Rendimiento y TDD

**Propósito (WHY):** Servir como *Ground Truth* para los Gremios de Desarrollo (Frontend, Backend, Mobile, QA). Este documento rige el balance entre creatividad semántica y rigor lógico.

**Audiencia (WHO):** Agentes *Builders* (`software-engineering-ecosystem`).

## 1. Flexibilidad Cognitiva en Desarrollo
A diferencia de los ecosistemas de auditoría, en la construcción de código **NO** se restringe agresivamente el hiperparámetro de vocabulario. 
- Los agentes tienen libertad para proponer algoritmos novedosos, aplicar patrones de diseño no convencionales si la eficiencia lo amerita, y explorar soluciones arquitectónicas complejas.
- **Prohibido el Bucle de Depuración Ciego:** Si un test falla 2 veces con el mismo enfoque, el agente debe cambiar su estrategia algorítmica y no iterar sobre un parche microscópico.

## 2. Rigor Desplazado a la Capa de Validación (TDD)
La creatividad de generación se compensa con una **rigidez extrema** en la fase de pruebas (`qa-tdd-guild`).
- **Red-Green-Refactor:** El ciclo es inmutable.
  1. Se escribe el Test que debe fallar.
  2. Se escribe la implementación (con flexibilidad creativa).
  3. Se refactoriza enfocándose en O(1) o O(n log n) de complejidad si es posible.
- **Calidad de Producción:** El output es final. No se generan prototipos frágiles ni *mocks* vacíos.

## 3. Sandboxing y Triage (Capa de Ejecución)
Cualquier intento de conexión externa (instalar NPMs, llamar APIs cloud) para probar el código debe invocar el triaje humano (ASK/ALLOW/DENY). El código no ejecutará peticiones reales no autorizadas.
