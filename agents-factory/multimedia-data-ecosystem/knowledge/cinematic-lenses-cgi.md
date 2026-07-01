# WHO: Knowledge Base para Agentes de Antigravity
# WHAT: Lentes Cinematográficos y Conceptos de Fotografía para CGI
# WHEN: Al generar prompts para imágenes, videos o encuadres 3D que requieran hiperrealismo fotográfico.
# WHERE: multimedia-data-ecosystem/knowledge
# WHY: Para evitar el "Look CG" caracterizado por cámaras perfectas y distancias focales predeterminadas irrealistas.

## 1. Fundamentos Ópticos y Longitud Focal
La distancia focal (medida en milímetros) no solo afecta el campo de visión, sino que altera psicológicamente la percepción de la escena (Compresión espacial).
- **Gran Angular (14mm - 35mm)**: Abre el campo visual. Exagera la distancia entre el primer plano y el fondo. Acentúa la perspectiva y hace que los movimientos parezcan más rápidos. Usado para arquitecturas o sensación de aislamiento.
- **Lente Normal (50mm)**: Aproxima la visión natural del ojo humano. Libre de distorsiones extremas. Ideal para documentales narrativos.
- **Teleobjetivo (70mm - 200mm+)**: Comprime el espacio; el fondo parece abalanzarse sobre el sujeto. Aísla personajes del entorno. Favorece los retratos al no distorsionar las facciones faciales.

## 2. El Triángulo de Exposición Simulado
Aunque los motores CGI no necesitan capturar luz física, simular estos parámetros inyecta realismo:
- **Apertura (F-stop / F-number)**: Define qué tan grande es el diafragma. Valores bajos (ej. f/1.4, f/2.8) crean una **Profundidad de Campo Superficial (Shallow DOF)**, desenfocando fuertemente el fondo (efecto Bokeh). Valores altos (ej. f/11, f/16) mantienen toda la escena en foco (Deep Focus).
- **Velocidad de Obturación (Shutter Speed / Shutter Angle)**: En cine analógico se usa tradicionalmente un ángulo de obturación de 180 grados, lo que genera el nivel exacto de *Motion Blur* natural (ej. grabar a 24 fps con obturación de 1/48 seg).

## 3. Imperfecciones Ópticas Requeridas (Dirty Lens FX)
Las cámaras 3D predeterminadas son estériles matemáticamente. Para inyectar fotorealismo, el prompt debe solicitar sutilmente:
- **Aberración Cromática (Chromatic Aberration)**: Franjas de color rojo/azul en los bordes de alto contraste (donde la lente falla en enfocar todos los colores en el mismo punto).
- **Distorsión de Lente (Barrel/Pincushion)**: Curvatura de líneas rectas en los bordes del marco, típica en lentes gran angulares esféricos (Barrel) o en anamórficos.
- **Viñeteado (Vignetting)**: Oscurecimiento sutil en las esquinas del frame.
- **Lens Flare, Bloom & Halation**: Esparcimiento orgánico de la luz al golpear directamente el cristal de la lente, o el sangrado rojo/naranja en película analógica en zonas de alta luz (Halation).
