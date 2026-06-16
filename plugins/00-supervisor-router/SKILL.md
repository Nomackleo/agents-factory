---
description: "Meta-Skill del Supervisor. Enruta la ejecución hacia los plugins especializados según el payload JSON."
argument-hint: "[payload_json]"
name: supervisor-router
---

# Supervisor Meta-Skill

Analiza la petición y, basándose en la matriz de enrutamiento (`brain/routing-matrix.json`), determina y transfiere el control al skill adecuado, generando un payload JSON válido validable por `bin/handoff-validator.py`.
