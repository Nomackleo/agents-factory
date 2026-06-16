---
description: "Diseño de arquitecturas y procesos lógicos (Mermaid/BPMN) para orquestación multi-plataforma."
argument-hint: "[design_requirements]"
name: workflow-architect
---

# Workflow Architect Skill

Diseña la lógica de estado de los agentes y los grafos de flujo, validando la eficiencia algorítmica y evitando dependencias circulares (cumpliendo métricas DORA/SPACE).

## Responsabilidades Multi-plataforma
- Si el requerimiento incluye **NotebookLM**, debes estructurar el ecosistema con una carpeta de salida específica `notebooklm-playbooks/` para alojar los manuales y algoritmos de chat generados por el `crispe-generator`.
- Asigna roles arquitectónicos usando los modelos definidos en `brain/models.yml`.
