# Reglas Operativas y Estándares de Renderizado: Archify Diagrams Ecosystem

**Propósito:** Definir los principios de compilación de diagramas de arquitectura interactivos en HTML/SVG mediante especificación de JSON IR tipado (Archify Standard), integración con la habilidad estética *Taste Skill* (Tipografía Suiza, Modo Presentación) y trazabilidad determinista de rutas.  
**Cumplimiento Normativo:** ISO 25010 (Calidad y Usabilidad de Software), ISO 9001:2015 (Documentación Técnica Verificable), TOGAF 10 (Arquitectura Empresarial).

---

## 1. Principios Inmutables de Diseño y Estructura Archify

1. **Topología Clara y Jerárquica (8–12 Nodos Centrales):**
   - Evitar el desorden visual y la saturación de conexiones. Los diagramas de nivel macro deben contener entre 8 y 12 componentes principales. El detalle secundario debe residir en tarjetas descriptivas (*node cards*) o vistas nombradas (*named views*).
2. **Tipado Estricto de JSON IR:**
   - Todo diagrama debe generarse a partir de un JSON IR válido con `nodes`, `edges`, `boundaries` (perímetros de seguridad o dominios) y `routes` explícitas.
3. **Cero Dependencia de Red en Runtime:**
   - Los archivos HTML generados deben ser 100% autocontenidos (*self-contained*), con SVGs vectoriales nítidos, soporte para modo oscuro/claro y controles de exportación (PNG, SVG, 1200×630 share card).

---

## 2. Fusión con Taste Skill (Diseño Suizo & Modo Presentación)

1. **Sistemas de Color Armónicos y Semánticos:**
   - Aplicar paletas corporativas bien estructuradas (ej. para Génesis Legal: `Deep Navy` `#07283d`, `Gold Accent` `#ffd231`, `Verde Cumplimiento` `#056c5c`, `Carmesí Alerta` `#ba1650`).
2. **Tipografía Ejecutiva:**
   - Utilizar combinaciones tipográficas modernas de Google Fonts (`Archivo` para titulares, `Spectral` para lectura editorial, `Chivo Mono` para identificadores técnicos y rutas).
3. **Dual Mode (Lectura Continua vs. Presentación Fullscreen):**
   - Incorporar navegación por diapositivas/vistas con atajos de teclado (`F`, `P`, `Flechas`), animaciones fluidas con aceleración GPU y paneles colapsables de metadatos.

---

## 3. Matriz Transversal de Casos de Uso

* **Google Workspace Architecture:** Topología de Shared Drives, flujo de correo, Gemini Extensions y seguridad perimetral.
* **Sistemas Multiagente (Antigravity):** Mapeo de orquestación, agentes especialistas, protocolos MCP y bus de eventos.
* **Infraestructura Cloud & Backend:** Microservicios, bases de datos, caché Redis, balanceadores y pasarelas API.
