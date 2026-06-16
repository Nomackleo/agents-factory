# Agent Factory - Architecture & System Design

Este documento define la arquitectura interna de la Fábrica de Agentes (Agent Factory) y los estándares de los ecosistemas que produce.

## Topología de la Fábrica
La fábrica se divide funcionalmente en tres motores:
1. **Orquestador (Global/System):** Mantiene la visión corporativa y coordina la ejecución.
2. **Planificador (Global/System):** Transforma requerimientos ambiguos en diseños de sistemas estructurados, seleccionando qué agentes atómicos se necesitan.
3. **Constructor (Skill):** El skill local `prompt-engineering-crispe` actúa como el trabajador de línea de ensamblaje. Recibe especificaciones precisas y escribe el código Markdown/YAML para configurar a los agentes hijos.

## Pipeline de Generación de Ecosistemas
1. **Ideación y Setup:** El Orquestador recibe el caso de uso (Ej. "Ecosistema de VFX para Blender"). Se crea un track en Conductor.
2. **Blueprint:** El Planificador diseña la topología de directorios dentro de `agents-factory/blender-ecosystem/`.
3. **Construcción CRISPE:** El Agente Constructor inyecta el framework CRISPE para crear cada uno de los `SKILL.md` necesarios, garantizando determinismo. También crea los `workflows/` y `rules/` necesarios.
4. **QA & TDD:** Se corren pruebas estáticas y A/B sobre los nuevos agentes en `tests/factory-ab-testing/` para asegurar que el output cumple con métricas de estabilidad y resiliencia corporativa.
5. **Empaquetado:** Se inyectan las plantillas de infraestructura desde `agents-factory/templates/` para aislar el ecosistema en Docker.

## Estándares de los Ecosistemas Generados (Antigravity 2.0)
Todos los sistemas producidos por esta fábrica deben acatar el estándar Antigravity 2.0 B2B:
- Uso **exclusivo** del directorio `.agents/` para lógica (skills, rules, workflows, plugins).
- Cada skill debe tener un archivo `SKILL.md` obligatorio con frontmatter (`name`, `description`).
- Los workflows deben guardarse como archivos Markdown y ser ligeros (< 12,000 caracteres).
- Cumplimiento de reglas SOC 2 inyectadas en `.agents/rules/` por defecto.
