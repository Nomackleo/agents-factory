# 🧩 El Framework CRISPE y Estructuras de Prompts

El framework **CRISPE** es un estándar de ingeniería de prompt diseñado para estructurar instrucciones de producción complejas de manera determinista, flexible y robusta. 

---

## 1. Desglose del Framework CRISPE

| Letra | Elemento | Descripción | Ejemplo Práctico (Español) |
| :---: | :--- | :--- | :--- |
| **C** | **Capacity & Role**<br>(Capacidad y Rol) | Define el personaje, perspectiva, rol o nivel de experiencia que adoptará la IA. | *"Actúa como un Consultor de Marketing Digital sénior con más de 15 años de experiencia..."* |
| **R** | **Receipt / Context**<br>(Contexto de Entrada) | Define los datos de entrada, la situación del negocio, la audiencia y la información de fondo. | *"Estamos diseñando una campaña de reactivación para un e-commerce que vende café artesanal..."* |
| **I** | **Instruction**<br>(Instrucción) | El mandato exacto, paso a paso o conjunto de reglas que el modelo debe ejecutar obligatoriamente. | *"Desarrolla tres estrategias específicas para recuperar clientes inactivos que no compran hace 90 días..."* |
| **S** | **Schema / Structure**<br>(Esquema o Formato) | Define la estructura exacta del output esperado (ej. JSON Schema, tabla Markdown, XML). | *"Presenta las estrategias en una tabla Markdown con las columnas: Estrategia, Lógica, y Ejemplo de Copiloto."* |
| **P** | **Personality & Style**<br>(Personalidad y Estilo) | El tono de voz, el estilo de escritura y la extensión esperada del resultado. | *"Usa un tono profesional, persuasivo pero cercano. Limita el análisis a un máximo de 300 palabras."* |
| **E** | **Examples / Experiment**<br>(Ejemplos y Experimento)| Demostraciones Few-Shot del formato esperado para calibrar la inferencia del modelo. | *"Ejemplo de formato:<br>- Estrategia: [Nombre]<br>- Lógica: [Explicación]<br>- Copiloto: [Texto]"* |

---

## 2. Fórmulas de Estructura de Prompts

Dependiendo de la complejidad de la tarea, puedes condensar o expandir el framework CRISPE en fórmulas estándar basadas en el *eBook Descubriendo la Ingeniería de Prompt*:

### 💎 Fórmula RTF (Role, Task, Format)
Ideal para tareas directas, rápidas y que requieren poca contextualización previa.
- **Rol (Role):** El rol que asume la IA usando la técnica "Actúa como...".
- **Tarea (Task):** La acción principal que debe ejecutarse de forma clara y directa.
- **Formato (Format):** La delineación de cómo estructurar la respuesta.

*Ejemplo:*
> *"Como especialista en nutrición (Rol), proporciona una lista de cinco alimentos ricos en proteínas (Tarea) en formato de lista numerada (Formato)."*

### 💎 Fórmula CTF (Context, Task, Format)
Especialmente útil cuando los antecedentes o la información del entorno son cruciales para el resultado, pero el rol del emisor es genérico.
- **Contexto (Context):** La información de fondo necesaria para encuadrar el problema.
- **Tarea (Task):** El mandato que la IA debe completar.
- **Formato (Format):** La estructura del output.

*Ejemplo:*
> *"Considerando las nuevas regulaciones de seguridad de datos (Contexto), crea una lista de verificación para que las pequeñas empresas se ajusten a la legislación (Tarea). La lista debe estar organizada por temas e incluir ejemplos prácticos en formato de viñetas Markdown (Formato)."*

### 💎 Fórmula GRADE (Goal, Request, Action, Detail, Examples)
Para prompts altamente detallados de nivel empresarial o campañas de marketing complejas.
- **Meta (Goal):** El objetivo final o propósito general que se espera lograr.
- **Solicitud (Request):** Lo que estás pidiendo específicamente que haga el modelo de lenguaje.
- **Acción (Action):** La acción o pasos específicos que la IA debe ejecutar en respuesta a tu solicitud.
- **Detalle (Detail):** Información complementaria que aclara las restricciones, límites u objetivos de audiencia.
- **Ejemplos (Examples):** Casos concretos que ilustran el comportamiento deseado.

*Ejemplo:*
> *"Desarrolla una estrategia de marketing digital eficaz para una pequeña empresa de comercio electrónico (Meta). Crea un plan de marketing digital completo (Solicitud), elaborando una lista de pasos y tácticas específicas (Acción). Enfócate en la conversión de ventas considerando un presupuesto limitado de $500 USD mensuales (Detalle). Proporciona ejemplos de publicaciones para redes sociales y una plantilla base de correo electrónico para guiar el estilo (Ejemplos)."*

---

## 3. Prácticas Avanzadas en CRISPE

1. **Definir Personas de Alta Fidelidad:** En lugar de decir *"Actúa como un programador"*, aporta contexto del perfil: *"Actúa como un programador especialista en TypeScript sénior, enfocado en código limpio, tipado estricto y patrones de diseño SOLID"*.
2. **Uso de Variables Interpolables:** Utiliza marcadores de posición tipo `{{VARIABLE}}` para separar las instrucciones del contenido de entrada.
3. **Preguntar antes de Responder (Interactive Setup):** Indica al modelo que no responda inmediatamente, sino que realice preguntas aclaratorias primero para afinar su contexto:
   > *"Antes de comenzar a diseñar el plan, hazme tres preguntas específicas sobre mi modelo de negocio para entender mejor el contexto actual."*
