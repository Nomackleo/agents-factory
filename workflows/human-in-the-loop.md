# Workflow: Human-in-the-loop (HITL)

Para evitar acciones destructivas y confirmar decisiones de diseño de alto nivel, la Fábrica requiere la autorización expresa del humano bajo circunstancias predefinidas.

## Puntos de Control Obligatorios (Checkpoints)

### 1. Aprobación del Blueprint Arquitectónico
- **Cuándo:** Después de que el `02-workflow-architect` genere el diseño final (Topología, stack de plugins, flujos de datos) y antes de invocar al `03-crispe-generator`.
- **Acción del Agente:** El Supervisor debe detener la ejecución, presentar el blueprint resumido o el `implementation_plan.md`, y solicitar explícitamente feedback o la directiva para continuar.

### 2. Aprobación de Instalación de Dependencias y Conexiones Web (Capa de Ejecución)
- **Cuándo:** 
  1. Si el nuevo ecosistema requiere que la fábrica corra un script local para bajar dependencias (ej. `npm install`, `pip install`).
  2. Si el ecosistema necesita conectarse a la WEB a servicios externos (GitHub, Google Cloud, DeepResearch, etc.).
- **Acción del Agente:** Emplear la herramienta de confirmación o detenerse antes de ejecutar el comando bash o la llamada a red, disparando el sistema de Triaje.

### 3. Finalización del Ecosistema
- **Cuándo:** Al completar la generación física del proyecto en `agents-factory/<nombre>/`.
- **Acción del Agente:** Generar un reporte final (`walkthrough.md`) documentando el árbol de directorios creado y solicitar validación humana.

## Sistema de Triaje de Permisos (Capa de Control)
Todo Puntos de Control HITL debe expresarse bajo el modelo de Triaje:
- **ASK (Preguntar):** El agente detecta una necesidad sensible (conexión web, ingesta de código) e interrumpe la ejecución con una pregunta explícita al usuario.
- **ALLOW (Permitir):** El usuario otorga un token de autorización temporal (ej. aprobar la solicitud a GitHub de manera local).
- **DENY (Denegar):** El usuario rechaza la acción; el agente debe generar una ruta de contingencia o fallar gracefulmente sin dañar el ecosistema.

## Dead-man Switch
Es un mecanismo de seguridad estricto que revierte el estado del ecosistema o detiene incondicionalmente a los agentes si:
1. Pasan más de N minutos sin respuesta del humano tras un `ASK`.
2. Se detecta un bucle algorítmico (Infinite Iteration Traps).
3. Hay una violación en la **Capa de Entrada** (Ej. el Sanitizador detecta un script oculto o redirección de correo tras la ingesta de un repositorio externo y el usuario deniega la confianza).
