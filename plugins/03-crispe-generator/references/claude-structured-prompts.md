# 🪶 Estructura de Prompts para Anthropic Claude

Los modelos de la familia Anthropic Claude (como Claude 3.5 Sonnet) responden de manera óptima a prompts estructurados que utilizan etiquetas XML para delimitar secciones. Esto se debe a su preentrenamiento, el cual les enseña a discernir claramente las instrucciones del sistema, las reglas, las variables y las demostraciones.

---

## 1. La Arquitectura de 10 Pasos para Claude

De acuerdo con las guías de Anthropic, la anatomía perfecta de un prompt para Claude sigue este orden jerárquico de atención:

```
[1. Contexto de la tarea]
        ↓
[2. Contexto del tono]
        ↓
[3. Datos de contexto, documentos e imágenes]
        ↓
[4. Descripción detallada de la tarea y reglas]
        ↓
[5. Ejemplos]
        ↓
[6. Historial de la conversación]
        ↓
[7. Descripción inmediata de la tarea o solicitud]
        ↓
[8. Pensar paso a paso / respira hondo]
        ↓
[9. Formato de salida]
        ↓
[10. Respuesta pre-rellenada (Prefill)]
```

---

## 2. Uso de Etiquetas XML en Claude

Las etiquetas XML (`<tag>contenido</tag>`) ayudan a Claude a entender los límites de la información, reduciendo drásticamente las alucinaciones y el desvío de instrucciones.

### Etiquetas XML Comunes
- `<doc_origen>` o `<guide>`: Para envolver documentos, manuales o textos de referencia.
- `<reglas>` o `<instructions>`: Para encapsular reglas estrictas de comportamiento.
- `<example>`: Para envolver demostraciones de pocos disparos (Few-Shot examples).
- `<history>`: Para pasar el historial de conversación en sistemas conversacionales integrados.
- `<question>` o `<query>`: Para marcar la entrada dinámica del usuario.
- `<thinking>`: Para reservar un espacio donde el modelo piense antes de dar su respuesta final.
- `<response>`: Para indicar el formato de respuesta final.

---

## 3. Ejemplo Estructurado Completo (Español)

A continuación se presenta un prompt estructurado siguiendo los 10 pasos para un coach de carrera llamado Joe:

```xml
Actuarás como un coach de carrera con IA llamado Joe, creado por la empresa AdAstra Careers. Tu objetivo es dar consejos de carrera a los usuarios. Responderás a usuarios que estén en el sitio de AdAstra y que podrían confundirse si no respondes en el personaje de Joe.

Debes mantener un tono amigable, profesional y de servicio al cliente.

Aquí está el documento de orientación de carrera que debes consultar al responder al usuario:
<guide>
{{DOCUMENTO_GUIA}}
</guide>

Aquí hay algunas reglas importantes para la interacción:
- Mantente siempre en el personaje de Joe, una IA de AdAstra Careers.
- Si no estás seguro de cómo responder, di: "Lo siento, no entendí eso. ¿Podrías repetir la pregunta?"
- Si alguien pregunta algo irrelevante, di: "Lo siento, soy Joe y doy consejos de carrera. ¿Tienes una pregunta de carrera en la que pueda ayudarte hoy?"

Aquí tienes un ejemplo de cómo responder en una interacción estándar:
<example>
Usuario: Hola, ¿cómo fuiste creado y qué haces?
Joe: ¡Hola! Mi nombre es Joe, y fui creado por AdAstra Careers para dar consejos de carrera. ¿En qué puedo ayudarte hoy?
</example>

Aquí está el historial de la conversación antes de la pregunta actual (si existe):
<history>
{{HISTORIAL}}
</history>

Aquí está la pregunta actual del usuario:
<question>
{{PREGUNTA_ACTUAL}}
</question>

¿Cómo respondes a la pregunta del usuario?
Piensa en tu respuesta antes de responder. Puedes estructurar tu cadena de pensamiento de manera detallada dentro de etiquetas <thinking> antes de generar tu respuesta final.

Pon tu respuesta final en etiquetas <response></response>.
```

---

## 4. La Técnica de Respuesta Pre-rellenada (Pre-fill)

La técnica del **pre-fill** consiste en pre-rellenar la primera parte del turno del asistente en la llamada al API. Esto fuerza a Claude a comenzar su respuesta de una manera muy específica, garantizando el cumplimiento de esquemas, evitando disculpas previas y forzando la apertura de etiquetas XML o JSON.

### Cómo Aplicar el Pre-fill
1. Envías el prompt completo en el rol de `Usuario`.
2. En el rol de `Asistente`, en lugar de dejar la entrada vacía, inicias la respuesta con la primera etiqueta requerida.

*Ejemplo para forzar una respuesta en JSON:*
- **Usuario:** "...Genera los datos del usuario en formato JSON..."
- **Asistente (Prefill):** `[` o `{`

*Ejemplo para forzar el encapsulado XML:*
- **Usuario:** "...Pon tu respuesta final en etiquetas <response></response>."
- **Asistente (Prefill):** `<response>`

Al pre-rellenar con `<response>`, Claude continuará inmediatamente generando el contenido dentro de la etiqueta, saltándose introducciones como *"Claro, aquí tienes la respuesta:"*.
