#!/usr/bin/env python3
"""
Antigravity 2.0 - Google Drive Gemini & Ecosystem Navigation Enhancer
1. Applies canonical color codes to all 9 macro-domains in Google Drive UI.
2. Creates structured `_README_GEMINI_INDEX.md` files in each root path and a Master Workspace Index for Gemini & Agent discovery.
"""

import sys
import os
import json
import time
import io
from typing import Dict, Any, List

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from workspace_client import WorkspaceClient

# Canonical Color Palette for Google Drive
FOLDER_COLOR_PALETTE = {
    "00_GOVERNANCE_MY_BUSINESS": "#1c4587",      # Azul Ejecutivo Oscuro
    "01_FINANCIAL_OPS": "#16a766",               # Verde Esmeralda Financiero
    "02_CLIENT_SERVICE_DELIVERY": "#056c5c",     # Verde Azulado Corporativo (Génesis Legal & Clientes)
    "03_KNOWLEDGE_BASE_RND": "#ffad47",          # Ámbar / Naranja Académico (Libros & Cursos)
    "04_PROJECTS_AI_AND_DEV": "#a479e2",         # Púrpura IA (Google AI Studio & Prompts)
    "05_PROJECTS_3D_CGI_VFX": "#3c78d8",         # Azul Técnico (3ds Max, Maya, Animación, 3D)
    "06_PERSONAL_LEGAL_DOCS": "#43d692",         # Verde Menta (Personal, CV, Salud, Familia)
    "07_MEDIA_CREATIVE_ASSETS": "#fb4c2f",       # Rojo / Coral Creativo (Audio, Video, Renders)
    "08_ARCHIVE_HISTORICAL": "#666666"          # Gris Técnico (Backups & Archivos Históricos)
}

DOMAIN_DOCUMENTATION = {
    "00_GOVERNANCE_MY_BUSINESS": """# 00_GOVERNANCE_MY_BUSINESS - Índice de Navegación

**Macro-Dominio:** Gobernanza, Identidad Ejecutiva y Contratos Marco  
**Propietario:** Leonel Salcedo (`nomackleo@gmail.com`)  
**Ecosistema:** `google-workspace-ecosystem`  
**Directiva de Acceso:** 🔒 Confidencial / Administrativo  

## 📂 Subdirectorios
- `01_Identidad_y_Bio/`: Perfiles ejecutivos maestros, extractos biográficos, semblanzas profesionales, CVs en español e inglés, certificaciones clave.
- `02_Contratos_Marco_y_NDAs/`: Acuerdos de confidencialidad (NDA), acuerdos marco de prestación de servicios, minutas legales y estatutos empresariales.

## 🎯 Directrices para Gemini y Agentes
- Consultar esta ruta para obtener la versión oficial del perfil profesional de Leonel Salcedo o cuando se redacten propuestas comerciales formales que requieran bio corporativa o firmas contractuales.
""",

    "01_FINANCIAL_OPS": """# 01_FINANCIAL_OPS - Índice de Navegación

**Macro-Dominio:** Operaciones Financieras, Bancarias, Facturación e Impuestos  
**Propietario:** Leonel Salcedo (`nomackleo@gmail.com`)  
**Ecosistema:** `google-workspace-ecosystem`  
**Directiva de Acceso:** 🔒 Confidencial / Financiero  

## 📂 Subdirectorios
- `01_Bancos_y_Extractos/`: Certificaciones bancarias, extractos de cuentas de ahorro y crédito (Davivienda, Banco Falabella, Nu Bank, etc.).
- `02_Facturas_y_Comprobantes/`: Cuentas de cobro emitidas, facturas de compras de software/hardware, comprobantes de transferencias y pagos PSE.
- `03_Impuestos_y_DIAN/`: Declaraciones de renta, RUT actualizado, certificados de retención en la fuente y certificados tributarios.
- `04_Inversiones_y_Trading/`: Informes de trading, operaciones en mercados bursátiles, Golden Wolf Trading 2019 y portafolios de inversión.
- `05_Produccion_y_Finanzas/`: Modelos de costos de producción, presupuestos operativos y balances de proyectos.

## 🎯 Directrices para Gemini y Agentes
- Utilizar esta carpeta para reconciliación de ingresos, consultas de facturación electrónica y trazabilidad tributaria.
""",

    "02_CLIENT_SERVICE_DELIVERY": """# 02_CLIENT_SERVICE_DELIVERY - Índice de Navegación

**Macro-Dominio:** Entrega de Servicios a Clientes, Consultorías y Alianzas Comerciales  
**Propietario:** Leonel Salcedo (`nomackleo@gmail.com`)  
**Ecosistema:** `google-workspace-ecosystem`  
**Directiva de Acceso:** 🤝 Corporativo / Operativo  

## 📂 Subdirectorios
- `01_Genesis_Legal/`: **Hub Central de Génesis Legal**.
  - `01_Capacitaciones_e_IA_Corporativa/`: Talleres prácticos, capacitación corporativa de Gemini, guías de adopción tecnológica y metodologías formativas.
  - `02_Propuestas_y_Contratos/`: Formatos de propuestas comerciales, minutas de consultoría y acuerdos de servicio.
  - `03_Cronogramas_e_Informes/`: Cronogramas oficiales (`GEN_CAP`), informes de culminación de transformación digital e informes de migración Dropbox.
  - `04_Presentaciones_Ejecutivas/`: Presentaciones maestras (`GEN_CAP_Presentacion_Completa_v2.0_Final`), decks ejecutivos y presentaciones multimedia `genesis_AI`.
  - `05_Prompts_y_Arquitectura_Modelos/`: Banco de Prompts CRISPE para Marketing Legal (`06_BANCO_PROMPTS_CRISPE_Marketing_Legal.md`) y Arquitectura de Instrucciones Gemini Pro.
- `02_Kodland_Academy/`: Materiales pedagógicos, clases, currículos formativos y fondos virtuales corporativos.
- `03_Otros_Clientes_y_Propuestas/`: Propuestas comerciales y entregables para Certicamara, Academia IA Pharma 30X, PRAXIA Habilidades IA y licitaciones.

## 🎯 Directrices para Gemini y Agentes
- Esta carpeta concentra todo el material entregable de clientes. Toda consulta sobre Génesis Legal debe resolverse dentro de `01_Genesis_Legal/`.
""",

    "03_KNOWLEDGE_BASE_RND": """# 03_KNOWLEDGE_BASE_RND - Índice de Navegación

**Macro-Dominio:** Base de Conocimiento, Libros, Papers, Formación y Cursos  
**Propietario:** Leonel Salcedo (`nomackleo@gmail.com`)  
**Ecosistema:** `google-workspace-ecosystem`  
**Directiva de Acceso:** 📚 Estudio / Referencia Técnica  

## 📂 Subdirectorios
- `01_Libros_Comics_y_Papers/`: Libros técnicos en PDF/ePub, manuales de programación, papers de inteligencia artificial, anatomía y narrativa gráfica (`.cbr`/`.cbz`).
- `02_Academias_y_Cursos/`: `VFXLearning FX Masters Program`, `VFXLearning FX Power User Archives`, `VFXLearning Movie of the week Archives`, clases maestras de 3D/VFX y bootcamps.
- `03_Becas_y_Convocatorias/`: Documentación de postulación a becas (ART-TOY BECA, Galería Doble Sentido, convocatorias culturales).
- `04_Notas_y_Manuales/`: Blocs de notas, One Note, guías rápidas, cheat sheets y apuntes de investigación técnica.

## 🎯 Directrices para Gemini y Agentes
- Utilizar esta carpeta como biblioteca de referencia conceptual, estándares de efectos visuales y literatura especializada.
""",

    "04_PROJECTS_AI_AND_DEV": """# 04_PROJECTS_AI_AND_DEV - Índice de Navegación

**Macro-Dominio:** Proyectos de Inteligencia Artificial, Agentes Autónomos, Software y Dev  
**Propietario:** Leonel Salcedo (`nomackleo@gmail.com`)  
**Ecosistema:** `google-workspace-ecosystem`  
**Directiva de Acceso:** 🤖 Desarrollo / Innovación  

## 📂 Subdirectorios
- `01_Agentes_e_IA_Generativa/`: Integraciones con `Google AI Studio`, Gemini Gems, prompts maestros, benchmarks de LLMs y prototipos del AI Boost Challenge.
- `02_Herramientas_y_Software/`: Herramientas auxiliares, scripts de automatización, `OpenToolBox2`, `SeriousGame` y utilidades de software.
- `03_Estrategia_y_Negocio/`: Planes de negocio de base tecnológica, proyectos académicos R&D y carpetas de ideación compartida.

## 🎯 Directrices para Gemini y Agentes
- Consultar esta ruta para activos de desarrollo, prompts de sistema, código de agentes y herramientas analíticas.
""",

    "05_PROJECTS_3D_CGI_VFX": """# 05_PROJECTS_3D_CGI_VFX - Índice de Navegación

**Macro-Dominio:** Producción 3D, Animación, Simulación CGI, Shading e Impresión 3D  
**Propietario:** Leonel Salcedo (`nomackleo@gmail.com`)  
**Ecosistema:** `google-workspace-ecosystem`  
**Directiva de Acceso:** 🎨 Arte / Producción 3D  

## 📂 Subdirectorios
- `01_Software_3ds_Max/`: Escenas, proyectos y modelos nativos de Autodesk 3ds Max.
- `02_Animacion_y_Crowds/`: Proyectos de animación de personajes (`Animacion Huevoman`) y simulaciones de multitudes con `1 Miarmy Software`.
- `03_Impresion_3D_y_Assets/`: Archivos para impresión 3D (`Formlabs`), sprites y assets 2D/3D (`Polytopia Sprites`).
- `04_Escenas_y_Modelos_High/`: Modelos 3D de alta densidad poligonal (High-Poly), texturas PBR, riggings y layouts de producción.

## 🎯 Directrices para Gemini y Agentes
- Dominio técnico especializado en pipelines 3D y VFX. Mantiene total independencia de los repositorios de software e IA.
""",

    "06_PERSONAL_LEGAL_DOCS": """# 06_PERSONAL_LEGAL_DOCS - Índice de Navegación

**Macro-Dominio:** Documentación Personal, Legal, Médica, Familiar y Comunitaria  
**Propietario:** Leonel Salcedo (`nomackleo@gmail.com`)  
**Ecosistema:** `google-workspace-ecosystem`  
**Directiva de Acceso:** 🔒 Privado / Personal  

## 📂 Subdirectorios
- `01_CV_y_Perfiles/`: Versiones personales de Hojas de Vida, perfiles curriculares y soportes de experiencia.
- `02_Salud_y_EPS/`: Certificaciones de afiliación (Famisanar EPS), exámenes médicos, fórmulas y carnés de vacunación.
- `03_Familia_y_Hogar/`: Documentación personal, archivos de Angélica, gestiones del hogar y trámites personales.
- `04_Comunidad_y_Eventos/`: Archivos de eventos comunitarios y sociales (`Asado UFC 17 enero 26`, listados de integrantes, PQRs personales).

## 🎯 Directrices para Gemini y Agentes
- Acceso restringido para trámites personales y referencias de identidad no comerciales.
""",

    "07_MEDIA_CREATIVE_ASSETS": """# 07_MEDIA_CREATIVE_ASSETS - Índice de Navegación

**Macro-Dominio:** Recursos Multimedia, Banco de Fotografías, Renders, Música y Video  
**Propietario:** Leonel Salcedo (`nomackleo@gmail.com`)  
**Ecosistema:** `google-workspace-ecosystem`  
**Directiva de Acceso:** 🎬 Multimedia / Creativo  

## 📂 Subdirectorios
- `01_Fotografia_y_Renders/`: Banco de imágenes de alta resolución, backgrounds virtuales, texturas, renders de prueba y elementos gráficos.
- `02_Audio_y_Musica/`: Grabaciones de audio (`Radio tanguita`), colecciones musicales públicas e instrumentales, partituras para piano (`Piano Sheet Music Collection`), MIDIs y ambientación musical (PABGM).
- `03_Video_y_Cine/`: Proyectos de cine, grabaciones audiovisuales, tomas de cámara y material de video para edición.

## 🎯 Directrices para Gemini y Agentes
- Banco multimedia para composición, diseño visual y musicalización de proyectos.
""",

    "08_ARCHIVE_HISTORICAL": """# 08_ARCHIVE_HISTORICAL - Índice de Navegación

**Macro-Dominio:** Archivos Históricos, Respaldos de Migración y Proyectos Concluidos  
**Propietario:** Leonel Salcedo (`nomackleo@gmail.com`)  
**Ecosistema:** `google-workspace-ecosystem`  
**Directiva de Acceso:** 📦 Solo Lectura / Histórico  

## 📂 Subdirectorios
- `01_Backups_Dropbox_y_Sistemas/`: Copias de respaldo completas de migraciones anteriores (Dropbox a Workspace), archivos comprimidos (.zip/.tar.gz) y volcados de bases de datos.
- `02_Archivos_Historicos_VFXLearning/`: Archivos de cursos y programas antiguos de VFXLearning preservados para consulta histórica.

## 🎯 Directrices para Gemini y Agentes
- Carpeta de preservación histórica inmutable. Los archivos en esta ubicación no deben ser modificados.
"""
}

MASTER_WORKSPACE_INDEX = """# MASTER INDEX: GOOGLE WORKSPACE DRIVE REPOSITORY

**Propietario:** Leonel Salcedo (`nomackleo@gmail.com`)  
**Tenant Ecosistema:** `google-workspace-ecosystem`  
**Arquitectura:** Estándar Canónico POSIX & ISO 8601  
**Última Actualización:** 2026-08-31  

---

## 🗺️ Mapa de Macro-Dominios Canónicos

| # | Macro-Dominio | Color Visual | Propósito y Contenido Principal |
| :-: | :--- | :---: | :--- |
| **00** | [`00_GOVERNANCE_MY_BUSINESS`](file:///c:/Users/Nomack/Documents/workspace/agents/antigravity/dev/prompt-generator/mcp/google-workspace/drive_manifest_nomackleo.json) | 🔵 Azul Oscuro | Bio ejecutiva, identidad profesional, CVs maestros y contratos marco / NDAs. |
| **01** | [`01_FINANCIAL_OPS`](file:///c:/Users/Nomack/Documents/workspace/agents/antigravity/dev/prompt-generator/mcp/google-workspace/drive_manifest_nomackleo.json) | 🟢 Verde Esmeralda | Bancos, extractos Davivienda/Falabella, facturas, DIAN/impuestos y trading. |
| **02** | [`02_CLIENT_SERVICE_DELIVERY`](file:///c:/Users/Nomack/Documents/workspace/agents/antigravity/dev/prompt-generator/mcp/google-workspace/drive_manifest_nomackleo.json) | 🟢 Verde Azulado | **Hub Central Génesis Legal** (Capacitaciones, Prompts CRISPE, Cronogramas, Decks) y Kodland. |
| **03** | [`03_KNOWLEDGE_BASE_RND`](file:///c:/Users/Nomack/Documents/workspace/agents/antigravity/dev/prompt-generator/mcp/google-workspace/drive_manifest_nomackleo.json) | 🟠 Ámbar / Naranja | Libros, ePubs, papers de IA, cursos VFXLearning, becas ART-TOY y manuales. |
| **04** | [`04_PROJECTS_AI_AND_DEV`](file:///c:/Users/Nomack/Documents/workspace/agents/antigravity/dev/prompt-generator/mcp/google-workspace/drive_manifest_nomackleo.json) | 🟣 Púrpura IA | Google AI Studio, Gemini Gems, prompts, herramientas de software y estrategia. |
| **05** | [`05_PROJECTS_3D_CGI_VFX`](file:///c:/Users/Nomack/Documents/workspace/agents/antigravity/dev/prompt-generator/mcp/google-workspace/drive_manifest_nomackleo.json) | 🔵 Azul Técnico | 3ds Max, animación Huevoman, multitudes Miarmy, Formlabs y modelos 3D. |
| **06** | [`06_PERSONAL_LEGAL_DOCS`](file:///c:/Users/Nomack/Documents/workspace/agents/antigravity/dev/prompt-generator/mcp/google-workspace/drive_manifest_nomackleo.json) | 🟢 Verde Menta | CV personal, salud/Famisanar, trámites familiares y eventos comunitarios (UFC). |
| **07** | [`07_MEDIA_CREATIVE_ASSETS`](file:///c:/Users/Nomack/Documents/workspace/agents/antigravity/dev/prompt-generator/mcp/google-workspace/drive_manifest_nomackleo.json) | 🔴 Rojo / Coral | Fotografía, renders, música (Radio Tanguita, piano, partituras) y video/cine. |
| **08** | [`08_ARCHIVE_HISTORICAL`](file:///c:/Users/Nomack/Documents/workspace/agents/antigravity/dev/prompt-generator/mcp/google-workspace/drive_manifest_nomackleo.json) | ⚪ Gris Técnico | Backups de migración Dropbox y archivos legados de programas concluidos. |

---

## 🤖 Guía de Interacción para Gemini & Agentes de IA
1. Cada macro-dominio contiene un archivo `_README_GEMINI_INDEX.md` con la descripción detallada de sus subdirectorios y directrices de acceso.
2. Los activos de clientes no deben dispersarse fuera de `02_CLIENT_SERVICE_DELIVERY/`.
3. Todos los nombres de archivos deben cumplir con el estándar POSIX (sin caracteres especiales no válidos, guiones bajos en lugar de espacios accidentales).
"""

def enhance_drive_navigation(account_alias: str = "nomackleo"):
    client = WorkspaceClient(account_alias)
    print(f"\n==================================================================")
    print(f" MEJORA DE NAVEGACIÓN GEMINI Y COLOREADO DE DRIVE: [{account_alias}]")
    print(f"==================================================================")

    manifest_path = os.path.join(os.path.dirname(__file__), f"drive_manifest_{account_alias}.json")
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    folder_manifest = manifest.get("folders", {})

    # 1. Apply Colors to Root Folders
    print(f"\n==> [1/2] Aplicando Paleta Canónica de Colores en Google Drive...")
    for root_name, color_hex in FOLDER_COLOR_PALETTE.items():
        if root_name in folder_manifest:
            folder_id = folder_manifest[root_name]["id"]
            print(f"  🎨 Coloreando '{root_name}' con {color_hex}...")
            try:
                res = client.set_drive_folder_color(folder_id, color_hex)
                actual_color = res.get("folderColorRgb", color_hex)
                print(f"     [OK] Color aplicado ({actual_color}).")
            except Exception as e:
                print(f"     [ERROR] Falló asignación de color a {root_name}: {e}")
            time.sleep(0.2)

    # 2. Upload _README_GEMINI_INDEX.md into each Canonical Root Folder
    print(f"\n==> [2/2] Creando Archivos de Índice y Navegación para Gemini & Agentes...")
    for root_name, doc_content in DOMAIN_DOCUMENTATION.items():
        if root_name in folder_manifest:
            folder_id = folder_manifest[root_name]["id"]
            doc_name = f"_README_GEMINI_INDEX.md"
            print(f"  📄 Creando índice en '{root_name}' (ID: {folder_id})...")
            try:
                res_up = client.upload_drive_file_content(
                    name=doc_name,
                    content=doc_content,
                    mime_type="text/markdown",
                    parent_id=folder_id,
                    description=f"Índice semántico y directivas de navegación para Gemini en {root_name}"
                )
                print(f"     [OK] Índice creado exitosamente. ID: {res_up.get('id')}")
            except Exception as e:
                print(f"     [ERROR] Falló creación de índice en {root_name}: {e}")
            time.sleep(0.2)

    # 3. Create Master Index in Root
    print(f"\n==> [3/3] Creando Master Index en la Raíz de Mi Unidad...")
    try:
        res_master = client.upload_drive_file_content(
            name="_MASTER_WORKSPACE_INDEX_GEMINI.md",
            content=MASTER_WORKSPACE_INDEX,
            mime_type="text/markdown",
            parent_id=None,
            description="Índice Maestro de Gobernanza y Navegación para Gemini y Agentes de Google Workspace"
        )
        print(f"  [OK] Master Index creado exitosamente en Raíz. ID: {res_master.get('id')}")
    except Exception as e:
        print(f"  [ERROR] Falló creación de Master Index: {e}")

    print(f"\n==================================================================")
    print(f" [ÉXITO TOTAL] PROCESO DE COLOR Y NAVEGACIÓN GEMINI FINALIZADO")
    print(f"==================================================================\n")

if __name__ == "__main__":
    alias = sys.argv[1] if len(sys.argv) > 1 else "nomackleo"
    enhance_drive_navigation(alias)
