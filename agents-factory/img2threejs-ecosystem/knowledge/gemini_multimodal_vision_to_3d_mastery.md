# Gemini 3.8 Flash Vision to 3D Mastery: Multimodal Deconstruction

**Propósito:** Especificación de los prompts de visión multimodal, razonamiento espacial y técnicas de descomposición volumétrica con **Gemini 3.8 Flash** para convertir imágenes 2D en geometrías Three.js jerárquicas y materiales PBR físicamente precisos.  
**Cumplimiento Normativo:** ISO 42001 (AIMS), ISO 25010 (Calidad de Software).

---

## 1. Capacidades de Razonamiento Espacial en Gemini 3.8 Flash

Gemini 3.8 Flash ofrece capacidades multimodales avanzadas para entender imágenes técnicas, siluetas y fotografías tridimensionales:

1. **Estimación de Profundidad Relativa y Oclusión:**
   - Detecta qué partes están en primer plano, cuáles en plano medio y cuáles en el fondo, calculando offsets en el eje $Z$.
2. **Descomposición Constructiva (CSG Inversa):**
   - En lugar de ver una sola superficie amorfa, Gemini 3.8 Flash fragmenta el objeto en volúmenes geométricos elementales (cilindro para el eje, caja biselada para el cuerpo, esfera achatada para el domo).
3. **Inferencia de Propiedades Físicas de Superficie (PBR Estimation):**
   - Discrimina entre metal pulido (`metalness: 0.9, roughness: 0.15`), plástico mate (`metalness: 0.0, roughness: 0.6`), vidrio/acrílico transparente (`transmission: 0.9, roughness: 0.1`) o fuentes emisivas (`emissive: #00ffff`).

---

## 2. Prompt Template para Invocación Multimodal de Gemini 3.8 Flash

```text
SYSTEM:
Eres un Ingeniero Senior de Computación Gráfica y Modelado 3D Procedural en Three.js. Tu misión es analizar la imagen suministrada y deconstruirla en una especificación tridimensional JSON estructurada siguiendo el esquema 'ObjectSculptSpec'.

INSTRUCCIONES DE ANÁLISIS:
1. Divide el objeto en componentes principales y sub-ensamblajes jerárquicos.
2. Para cada componente, determina la primitiva Three.js más eficiente (BoxGeometry, CylinderGeometry, SphereGeometry, etc.) y sus parámetros [ancho, alto, profundidad, segmentos].
3. Estima las posiciones locales [x, y, z] y rotaciones [rx, ry, rz] en radianes, asegurando que los pivotes permitan animación coherente.
4. Define los materiales PBR necesarios con colores hexadecimales precisos extraídos de la imagen, niveles de roughness, metalness y propiedades emisivas.
5. Propón animaciones procedurales en tiempo de ejecución (ej. rotación de aspas, flotación gravitacional, pulsos de luz).

OUTPUT:
Retorna EXCLUSIVAMENTE el bloque JSON 'ObjectSculptSpec' válido sin texto introductorio ni explicaciones fuera del JSON.
```

---

## 3. Manejo de Múltiples Vistas y Visual Hull

Cuando el usuario suministre más de una perspectiva (frente, lateral, superior):
- Gemini 3.8 Flash triangula las siluetas ortogonales para calcular un envolvente (*Visual Hull*) más fidedigno.
- Corrige discrepancias de escala entre ejes $[X, Y, Z]$ preservando proporciones realistas.
