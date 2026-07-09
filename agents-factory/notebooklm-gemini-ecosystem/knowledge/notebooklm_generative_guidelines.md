# Plantilla de Conocimiento: Sinergia RAG y Creatividad Generativa

**Propósito (WHY):** Establecer el límite claro entre la extracción determinista (NotebookLM) y la iteración creativa (Gemini Gems), cumpliendo la heurística global de flexibilización del Top-P.

**Audiencia (WHO):** Motores de RAG (NotebookLM) y Agentes Generativos (Gemini Gems).

## 1. La Ingesta (NotebookLM) - Temperatura 0
El uso de NotebookLM actúa como el ancla de *Ground Truth*. La extracción de datos sociopolíticos, estadísticos o documentales **NO admite creatividad**.
- Los resúmenes deben apegarse estrictamente a las fuentes.
- **Top-P:** 0.

## 2. La Generación (Gemini Gems) - Creatividad Paramétrica
Una vez que NotebookLM entrega el JSON estadístico o el *Creative Brief*, el relevo pasa a los Gems de Gemini (ej. `visual-decoder`, `image-creator`).
- **Flexibilidad Semántica Activada:** De acuerdo a la directriz `implicit/DOMAIN.md`, para diseño gráfico, conceptualización y creación audiovisual, se **eleva la Temperatura/Top-P**.
- Se espera que el Gem proponga metáforas visuales, estilos artísticos atrevidos (ej. "Cyberpunk acuarela", "Hiperrealismo cinemático") basándose en el brief. No debe limitarse a descripciones planas.
- **Rigor en la Salida (El Contenedor):** Aunque la idea es libre, el output final debe empaquetarse rígidamente en JSON o Markdown estructurado para que el `00-supervisor-router` pueda parsearlo y enviarlo al API de renderizado sin errores de sintaxis.
