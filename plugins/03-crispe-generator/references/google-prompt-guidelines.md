# 🌐 Directrices de Ingeniería de Prompt de Google 2025

Los modelos de lenguaje modernos (como Gemini 1.5/2.0/3.5 Pro y Flash) operan bajo parámetros específicos de decodificación y metodologías cognitivas avanzadas que guían su capacidad de predicción lógica.

---

## 1. Parámetros de Decodificación y Configuración de Salida

El prompt es solo una parte de la ecuación; la correcta configuración de los parámetros del LLM define el balance entre el determinismo lógico y la creatividad.

| Parámetro | Definición | Efecto en la Salida | Configuración Recomendada |
| :--- | :--- | :--- | :--- |
| **Temperatura** | Controla el grado de aleatoriedad en la selección de tokens. | **0:** Totalmente determinista (greedy decoding).<br>**1:** Creatividad máxima. | **0.0:** Tareas de código, matemáticas y CoT.<br>**0.2:** Clasificación y extracción de datos.<br>**0.7 - 0.9:** Redacción creativa. |
| **Top-P** | Filtra los tokens acumulados hasta un umbral de probabilidad $P$. | **Bajo (0.1):** Selecciona solo tokens de altísima confianza.<br>**Alto (1.0):** Considera todos los tokens del vocabulario. | **0.95:** Valor estándar para mantener coherencia en Gemini.<br>**0.9:** Para mayor precisión factual. |
| **Top-K** | Limita la selección de palabras a las $K$ opciones más probables. | **Bajo (1):** Equivalente a greedy decoding.<br>**Alto (40+):** Permite mayor variedad de palabras en la salida. | **30:** Para resultados estándar equilibrados.<br>**20:** Para menor variabilidad. |
| **Límite de Tokens** | Restringe la longitud física de la generación. | Corta la generación una vez alcanzado el límite (no hace que sea más conciso). | Ajustar para prevenir bucles de repetición y sobrecostos. |

---

## 2. Técnicas Avanzadas de Razonamiento Cognitivo

### 🧠 Step-Back Prompting (Retroceder un Paso)
Consiste en pedirle al LLM que identifique un principio o concepto general (un paso atrás) antes de intentar responder a la pregunta del usuario. Esto pre-activa la memoria semántica del modelo.
- **Paso 1 (Abstracción):** *"Antes de resolver esta pregunta física del motor, explica los principios de la termodinámica que rigen el rendimiento del combustible."*
- **Paso 2 (Resolución):** *"Con base en los principios descritos anteriormente, resuelve el siguiente problema: [Problema específico]."*

### 🧠 Chain-of-Thought (CoT - Cadena de Pensamiento)
Estructura el proceso de pensamiento de forma secuencial.
- **Mejor Práctica:** Forzar a que la respuesta final se ubique *después* del razonamiento para que la generación previa condicione y mejore la predicción de la solución.
- **Temperatura:** Ajustar siempre a `0` para garantizar un razonamiento lógico y determinista.

### 🧠 Self-Consistency (Autoconsistencia)
Generar múltiples cadenas de pensamiento paralelas de forma independiente (ejecutando el prompt con una temperatura de `0.7` varias veces) y seleccionar el resultado final por votación de mayoría. Ideal para clasificaciones complejas o decisiones críticas.

### 🧠 Tree of Thoughts (ToT - Árbol de Pensamientos)
Generaliza CoT permitiendo al modelo explorar múltiples caminos de pensamiento simultáneamente, evaluar el progreso de cada rama mediante autocrítica y retroceder si una rama es inviable.

### 🧠 ReAct (Reason & Act - Pensar y Actuar)
Loop cognitivo para agentes que interactúan con herramientas externas:
```
Pregunta → Pensamiento (Razonamiento) → Acción (Ejecución de herramienta) → Observación (Resultado) → Pensamiento → ... → Respuesta Final
```

---

## 3. Integración con Esquemas de Datos (Schemas)

Para aplicaciones empresariales y flujos automatizados, es vital estructurar tanto la **entrada** como la **salida** mediante JSON Schemas.
1. **Esquema de Entrada (Input Schema):** Aporta al modelo una estructura clara y unificada de las variables para que entienda las relaciones y los tipos de datos (evita malentendidos de contexto temporal o numérico).
2. **Esquema de Salida (Output Schema):** Indica el formato exacto en el que el modelo debe serializar su respuesta (ej. forzar un JSON estructurado).

---

## 4. Patrón de JSON Repair

Una limitación común de la serialización JSON en LLMs es el truncamiento debido al límite de tokens o interrupciones de red, lo que daña el JSON y rompe el flujo del código.
- **Mitigación Programática:** Incorporar en los scripts bibliotecas como `json-repair` en Python para intentar cerrar llaves, corchetes y comillas faltantes antes de descartar la respuesta.
- **Instrucciones Positivas en el Prompt:** Siempre privilegiar instrucciones directas (*"Qué hacer"*) sobre restricciones (*"Qué no hacer"*). En lugar de *"No incluyas markdown"* usa *"Devuelve únicamente el contenido del JSON plano"*.
