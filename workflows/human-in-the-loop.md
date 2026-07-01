# Workflow: Human-in-the-loop (HITL)

Para evitar acciones destructivas y confirmar decisiones de diseño de alto nivel, la Fábrica requiere la autorización expresa del humano bajo circunstancias predefinidas.

## Puntos de Control Obligatorios (Checkpoints)

### 1. Aprobación del Blueprint Arquitectónico
- **Cuándo:** Después de que el `02-workflow-architect` genere el diseño final (Topología, stack de plugins, flujos de datos) y antes de invocar al `03-crispe-generator`.
- **Acción del Agente:** El Supervisor debe detener la ejecución, presentar el blueprint resumido o el `implementation_plan.md`, y solicitar explícitamente feedback o la directiva para continuar.

### 2. Aprobación de Instalación de Dependencias
- **Cuándo:** Si el nuevo ecosistema requiere que la fábrica corra un script local para bajar dependencias (ej. `npm install`, `pip install`).
- **Acción del Agente:** Emplear la herramienta de confirmación o detenerse antes de ejecutar el comando bash.

### 3. Finalización del Ecosistema
- **Cuándo:** Al completar la generación física del proyecto en `agents-factory/<nombre>/`.
- **Acción del Agente:** Generar un reporte final (`walkthrough.md`) documentando el árbol de directorios creado y solicitar validación humana.
