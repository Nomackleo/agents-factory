# Plantilla de Conocimiento: Libre Creatividad Multimedia

**Propósito (WHY):** Servir como *Ground Truth* para habilitar la capacidad de ideación y creatividad (Top-P relajado) en tareas de diseño gráfico, personajes de videojuegos, campañas de marketing y lluvias de ideas, contrarrestando la rigidez de los entornos de auditoría.

**Audiencia (WHO):** Agentes de ideación visual, generadores de contenido y decodificadores multimedia (`image-creator-agent`, `video-creator-agent`, etc.).

## 1. Flexibilidad Semántica Activada
De acuerdo a las reglas globales (`implicit/DOMAIN.md`), este ecosistema **requiere** de la creatividad del modelo:
- Se promueve la exploración de metáforas visuales, iluminación dramática o narrativas arriesgadas (Lluvia de Ideas).
- El vocabulario y el Top-P no están penalizados. El agente debe usar descriptores ricos y atmosféricos.

## 2. Equilibrio con Spatial Reasoning (DwT)
Aunque la creatividad temática es libre, la *composición espacial* sigue anclada al paradigma **Drawing-with-Thought (DwT)**:
- La idea de un personaje o el guion de marketing puede ser altamente abstracto y libre.
- Sin embargo, las proporciones (ej. regla de los tercios), los códigos hexadecimales (JSON) y las dimensiones en píxeles no se alucinan; se calculan lógicamente.

## 3. Ejemplos de Output Híbrido
- **Creatividad:** "El personaje es un ciber-mago atormentado, vistiendo una túnica de hilos de fibra óptica deshilachados bajo la lluvia de neón."
- **Estructura DwT:** `{"character": {"hex_primary": "#0F172A", "lighting": "chiaroscuro", "bounding_box": [100, 50, 400, 800]}}`
