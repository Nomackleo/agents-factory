# WHO: Knowledge Base para Agentes de Antigravity
# WHAT: Arquitecturas Generativas de Google (Gemini Omni, Flash, Veo, Nano Banana 2)
# WHEN: Para comprender cómo funcionan internamente los motores a los que el ecosistema Antigravity envía los prompts.
# WHERE: multimedia-data-ecosystem/knowledge
# WHY: Para estructurar arquitectónicamente los Prompts y el JSON según los mecanismos cognitivos nativos de estos modelos.

## 1. Gemini Omni & Gemini Flash
**Arquitectura Unificada (Any-to-Any)**
A diferencia de los pipelines antiguos que concatenaban modelos especializados (uno para texto, otro separado para imagen), Gemini (especialmente las variantes Flash 1.5/2.0 y Omni) posee una arquitectura Transformer **multimodal nativa**.
- Puede razonar simultáneamente sobre video, audio, texto e imágenes sin pérdida de contexto en la conversión.
- Permite "Ingestas Masivas" (context windows de 1M a 2M tokens), lo que facilita analizar horas de video o bases de datos enteras antes de generar una sola imagen o fotograma.

## 2. Motor VEO (Video Generation)
Veo es el motor de generación de píxeles y video temporal de Google, que se integra bajo el paraguas cognitivo de Gemini.
- **Modelado Físico (World Modeling)**: Veo no solo pinta fotogramas, simula cinemática. Entiende la física de fluidos, la gravedad y la consistencia espacial 3D de los objetos, evitando artefactos de "morphing".
- **Temporal Consistency**: Garantiza que un objeto en el frame 1 siga siendo lógicamente el mismo en el frame 200, fundamental para cinemáticas largas.

## 3. Nano Banana 2 (Framework de Control)
En el contexto de Antigravity, **Nano Banana 2** se documenta como el paradigma arquitectónico de *Prompt Engineering Estructurado*.
- Consiste en aislar la lógica y la estética en arreglos JSON rígidos, previniendo la "alucinación" de los modelos fundacionales.
- Al interactuar con Gemini/Veo, los agentes no utilizan "prompts libres", sino que inyectan el *storyline*, los metadatos fotográficos (lentes, F-stop) y las variables de diseño (colores, proporciones) a través de estructuras Nano Banana 2.
- Esto fuerza al modelo "Omni" a acoplar su profundo entendimiento multimodal a un raíl lógico inquebrantable, produciendo assets de calidad corporativa (AAA).
