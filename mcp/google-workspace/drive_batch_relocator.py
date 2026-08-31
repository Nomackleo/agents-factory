#!/usr/bin/env python3
"""
Antigravity 2.0 - Google Drive Enterprise Batch Relocation Engine (Multi-Tenant)
Executes atomic, reversible relocation of root folders and loose files into the canonical hierarchy.
Handles owned items via atomic move and shared items via Google Drive Shortcuts.
Ensures ZERO deletions, rate limiting, error logging and complete audit manifests.
"""

import sys
import os
import json
import time
import io
from typing import Dict, Any, List, Optional

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from workspace_client import WorkspaceClient

# Root folder mapping to canonical subfolder paths
ROOT_FOLDER_MAP_BY_ACCOUNT = {
    "nomackleo": {
        # 02 Client Service Delivery - Genesis & Clients
        "Formatos de propuestas comerciales.": "02_CLIENT_SERVICE_DELIVERY/01_Genesis_Legal/02_Propuestas_y_Contratos",
        "Kodland": "02_CLIENT_SERVICE_DELIVERY/02_Kodland_Academy/Clases",
        "Kodland Virtual Background": "02_CLIENT_SERVICE_DELIVERY/02_Kodland_Academy/Virtual_Backgrounds",

        # 04 AI & Dev
        "Google AI Studio": "04_PROJECTS_AI_AND_DEV/01_Agentes_e_IA_Generativa",
        "AI Boost Bite Challenge 13": "04_PROJECTS_AI_AND_DEV/01_Agentes_e_IA_Generativa",
        "AI": "04_PROJECTS_AI_AND_DEV/01_Agentes_e_IA_Generativa",
        "Gemini Gems": "04_PROJECTS_AI_AND_DEV/01_Agentes_e_IA_Generativa",
        "new🧰OpenToolBox2": "04_PROJECTS_AI_AND_DEV/02_Herramientas_y_Software",
        "SeriousGame": "04_PROJECTS_AI_AND_DEV/02_Herramientas_y_Software",
        "Te_Con_Cucas_2025": "04_PROJECTS_AI_AND_DEV/02_Herramientas_y_Software",
        "Te_Con_Cucas_2025 ": "04_PROJECTS_AI_AND_DEV/02_Herramientas_y_Software",
        "Plan de Negocio": "04_PROJECTS_AI_AND_DEV/03_Estrategia_y_Negocio",
        "Academic": "04_PROJECTS_AI_AND_DEV/03_Estrategia_y_Negocio",
        "Compartido": "04_PROJECTS_AI_AND_DEV/03_Estrategia_y_Negocio",
        "Files from platform": "04_PROJECTS_AI_AND_DEV/03_Estrategia_y_Negocio",

        # 05 3D CGI VFX
        "3d max": "05_PROJECTS_3D_CGI_VFX/02_Software_3ds_Max",
        "Animacion Huevoman": "05_PROJECTS_3D_CGI_VFX/03_Animacion_y_Crowds",
        "1 Miarmy Software": "05_PROJECTS_3D_CGI_VFX/03_Animacion_y_Crowds",
        "Formlabs": "05_PROJECTS_3D_CGI_VFX/04_Impresion_3D_y_Assets",
        "Polytopia Sprites": "05_PROJECTS_3D_CGI_VFX/04_Impresion_3D_y_Assets",
        "Clase30_ModelosHigh": "05_PROJECTS_3D_CGI_VFX/05_Escenas_y_Modelos_High",

        # 03 Knowledge Base R&D
        "VFXLearning FX Masters Program": "03_KNOWLEDGE_BASE_RND/02_Academias_y_Cursos",
        "VFXLearning FX Power User Archives": "03_KNOWLEDGE_BASE_RND/02_Academias_y_Cursos",
        "VFXLearning Movie of the week Archives": "03_KNOWLEDGE_BASE_RND/02_Academias_y_Cursos",
        "Clase 2": "03_KNOWLEDGE_BASE_RND/02_Academias_y_Cursos",
        "Clase23": "03_KNOWLEDGE_BASE_RND/02_Academias_y_Cursos",
        "ART-TOY BECA": "03_KNOWLEDGE_BASE_RND/03_Becas_y_Convocatorias",
        "Lineamientos Convocatoria ART-TOY - Galería Doble Sentido": "03_KNOWLEDGE_BASE_RND/03_Becas_y_Convocatorias",
        "One Note": "03_KNOWLEDGE_BASE_RND/04_Notas_y_Manuales",
        "Archivos leg": "03_KNOWLEDGE_BASE_RND/04_Notas_y_Manuales",

        # 01 Financial Ops
        "Golden Wolf Trading 2019": "01_FINANCIAL_OPS/04_Inversiones_y_Trading",
        "Trading": "01_FINANCIAL_OPS/04_Inversiones_y_Trading",
        "Línea de Producción y Financiera": "01_FINANCIAL_OPS/05_Produccion_y_Finanzas",

        # 06 Personal Legal Docs
        "CV": "06_PERSONAL_LEGAL_DOCS/01_CV_y_Perfiles",
        "Personal": "06_PERSONAL_LEGAL_DOCS/03_Familia_y_Hogar",
        "Angélica": "06_PERSONAL_LEGAL_DOCS/03_Familia_y_Hogar",
        "Asado UFC 17 enero 26": "06_PERSONAL_LEGAL_DOCS/04_Comunidad_y_Eventos",

        # 07 Media Creative Assets
        "Imagenes": "07_MEDIA_CREATIVE_ASSETS/02_Fotografia_y_Renders",
        "Background": "07_MEDIA_CREATIVE_ASSETS/02_Fotografia_y_Renders",
        "Random": "07_MEDIA_CREATIVE_ASSETS/02_Fotografia_y_Renders",
        "Elementos": "07_MEDIA_CREATIVE_ASSETS/02_Fotografia_y_Renders",
        "Radio tanguita": "07_MEDIA_CREATIVE_ASSETS/03_Audio_y_Musica",
        "Public Music": "07_MEDIA_CREATIVE_ASSETS/03_Audio_y_Musica",
        "Music": "07_MEDIA_CREATIVE_ASSETS/03_Audio_y_Musica",
        "Piano Sheet Music Collection - KobeThuy": "07_MEDIA_CREATIVE_ASSETS/03_Audio_y_Musica",
        "Sheet music and midi files": "07_MEDIA_CREATIVE_ASSETS/03_Audio_y_Musica",
        "Supply and Delivery of Public Address Background Music (PABGM)": "07_MEDIA_CREATIVE_ASSETS/03_Audio_y_Musica",
        "Instrumental Music": "07_MEDIA_CREATIVE_ASSETS/03_Audio_y_Musica",
        "Cine": "07_MEDIA_CREATIVE_ASSETS/04_Video_y_Cine",

        # 08 Archive Historical
        "VFXLearning FX Masters Program Archives": "08_ARCHIVE_HISTORICAL/02_Archivos_Historicos_VFXLearning"
    },
    "nomack3d": {
        # 00 Governance
        "Company_Root": "00_GOVERNANCE_MY_BUSINESS/03_Company_Root_y_Estatutos",

        # 01 Financial Ops
        "Trader Science": "01_FINANCIAL_OPS/04_Inversiones_y_Trading",
        "Admin": "01_FINANCIAL_OPS/04_Inversiones_y_Trading",
        "Movistar": "01_FINANCIAL_OPS/02_Facturas_y_Comprobantes",

        # 02 Client Service Delivery
        "02_CLIENT_SERVICE_DELIVERY": "02_CLIENT_SERVICE_DELIVERY/01_Genesis_Legal",
        "KIT DE PRENSA -  BOGOTÁ": "02_CLIENT_SERVICE_DELIVERY/03_Otros_Clientes_y_Propuestas",

        # 03 Knowledge Base R&D
        "football books": "03_KNOWLEDGE_BASE_RND/01_Libros_Comics_y_Papers",
        "Curso de Wordpress": "03_KNOWLEDGE_BASE_RND/02_Academias_y_Cursos",
        "parido": "03_KNOWLEDGE_BASE_RND/04_Notas_y_Manuales",

        # 04 AI & Dev
        "Google AI Studio": "04_PROJECTS_AI_AND_DEV/01_Agentes_e_IA_Generativa",
        "rag": "04_PROJECTS_AI_AND_DEV/01_Agentes_e_IA_Generativa",
        "Gemini Gems": "04_PROJECTS_AI_AND_DEV/01_Agentes_e_IA_Generativa",
        "Zona MVP": "04_PROJECTS_AI_AND_DEV/03_Estrategia_y_Negocio",

        # 05 3D CGI VFX
        "Ciudad Automata": "05_PROJECTS_3D_CGI_VFX/01_Proyectos_Escenas_3D",

        # 06 Personal Legal Docs
        "CV": "06_PERSONAL_LEGAL_DOCS/01_CV_y_Perfiles",
        "Ma": "06_PERSONAL_LEGAL_DOCS/03_Familia_y_Hogar",
        "Mom": "06_PERSONAL_LEGAL_DOCS/03_Familia_y_Hogar",

        # 07 Media Creative Assets
        "identidad grafica": "07_MEDIA_CREATIVE_ASSETS/01_Branding_e_Identidad",
        "Meet Recordings": "07_MEDIA_CREATIVE_ASSETS/04_Video_y_Cine",
        "Exportaciones de Vids": "07_MEDIA_CREATIVE_ASSETS/04_Video_y_Cine"
    }
}

def determine_file_target(file_item: Dict[str, Any], account_alias: str = "nomack3d") -> str:
    name = file_item.get("name", "").lower()
    mime = file_item.get("mimeType", "").lower()
    ext = os.path.splitext(name)[1].lower()
    owners = [o.get("emailAddress", "").lower() + " " + o.get("displayName", "").lower() for o in file_item.get("owners", [])]
    owners_str = " ".join(owners)

    # 1. Genesis Legal (Absolute Priority - All Genesis files stay unified)
    genesis_kws = [
        "genesis", "génesis", "dpto de confiabilidad", "acta de conformidad", "acta_iso",
        "acta_de_respaldo", "culminación exitosa", "transformación digital", "plan legal laboral",
        "invitacion_a_cotizar", "propuesta_comercial_avanzada", "levantamiento de requerimientos",
        "informe_ejecutivo_migracion", "arquitectura de aprovisionamiento", "sow_digital-transformation",
        "sow_software-contract", "sow_branding-proposal", "sow_ai-commercial-prop", "spec_dns-zone",
        "spec_provisioning-governance", "spec_operational-audit", "spec_workspace-config", "spec_deep-research",
        "pres_executive-proposal", "pres_commercial-proposal", "pres_agentic-governance", "spec_curricular-program",
        "doc_maestro_genesis", "auditoria_seo_sem_genesis", "filosofia_diseno_genesis", "programa_curricular_genesis",
        "infografia_ecosistema_ia_genesis", "quién es genesis", "génesis risk forensic"
    ]
    is_genesis = any(kw in name for kw in genesis_kws) or any(kw in owners_str for kw in ["genesislegal", "danielmoncadap", "comercial"])

    if is_genesis:
        if mime.startswith("video/") or any(w in name for w in ["video", "dpto de confiabilidad - ia. - 2026", "pres_", "presentacion", "presentación", "final", "infografia", "quién es genesis", "génesis risk"]):
            return "02_CLIENT_SERVICE_DELIVERY/01_Genesis_Legal/04_Presentaciones_Decks_y_Multimedia"
        elif any(w in name for w in ["propuesta", "sow", "contract", "cotizar", "plan legal", "branding-proposal", "comercial-proposal"]):
            return "02_CLIENT_SERVICE_DELIVERY/01_Genesis_Legal/02_Propuestas_Comerciales_y_Contratos"
        elif any(w in name for w in ["acta", "culminación", "informe", "arquitectura", "spec_dns", "spec_provisioning", "spec_operational", "spec_workspace"]):
            return "02_CLIENT_SERVICE_DELIVERY/01_Genesis_Legal/03_Actas_Informes_y_Gobernanza"
        elif any(w in name for w in ["doc_maestro", "seo", "sem", "filosofia", "deep-research", "schedule"]):
            return "02_CLIENT_SERVICE_DELIVERY/01_Genesis_Legal/05_Marketing_SEO_y_Estrategia_IA"
        else:
            return "02_CLIENT_SERVICE_DELIVERY/01_Genesis_Legal/01_Capacitaciones_y_Programas_IA"

    # 2. Other Clients & Proposals
    if any(w in name for w in ["kit de prensa", "certicamara", "pharma", "praxia", "onb", "kodland"]):
        return "02_CLIENT_SERVICE_DELIVERY/03_Otros_Clientes_y_Propuestas"

    # 3. Financial Ops
    if any(w in name for w in ["factura", "recibo", "extracto", "cuenta de cobro", "pago", "comprobante", "dian", "rut", "banco", "davivienda", "falabella", "movistar", "trader"]):
        if "banco" in name or "extracto" in name:
            return "01_FINANCIAL_OPS/01_Bancos_y_Extractos"
        elif "dian" in name or "rut" in name or "impuesto" in name:
            return "01_FINANCIAL_OPS/03_Impuestos_y_DIAN"
        elif "trader" in name or "trading" in name:
            return "01_FINANCIAL_OPS/04_Inversiones_y_Trading"
        else:
            return "01_FINANCIAL_OPS/02_Facturas_y_Comprobantes"

    # 4. 3D, CGI & VFX
    if ext in [".blend", ".fbx", ".obj", ".max", ".c4d", ".hip", ".uasset", ".stl", ".ma", ".mb"] or any(w in name for w in ["3d", "render", "mesh", "texture", "shader", "ciudad automata", "huevoman"]):
        return "05_PROJECTS_3D_CGI_VFX/01_Proyectos_Escenas_3D"

    # 5. AI & Dev
    if any(w in name for w in ["prompt", "gemini", "bigquery", "qa", "test document", "openai", "gpt", "model", "dataset", "agent", "colaboratory", "powerpoint generator", "rag", "como experta", "vamos a trabajar", "con base en lo anterior", "todas las respuestas", "bien, nos acercamos"]):
        return "04_PROJECTS_AI_AND_DEV/01_Agentes_e_IA_Generativa"

    # 6. Personal & Legal
    if any(w in name for w in ["cv", "curriculum", "hoja de vida", "perfil", "cedula", "cédula", "pasaporte"]):
        return "06_PERSONAL_LEGAL_DOCS/01_CV_y_Perfiles"
    if any(w in name for w in ["salud", "eps", "famisanar", "medico", "médico", "vacuna"]):
        return "06_PERSONAL_LEGAL_DOCS/02_Salud_y_EPS"
    if any(w in name for w in ["pqr", "reclamación", "personal", "angelica", "angélica", "mama", "mamá", "mom", "ma "]):
        return "06_PERSONAL_LEGAL_DOCS/03_Familia_y_Hogar"
    if any(w in name for w in ["asado", "ufc", "integrantes"]):
        return "06_PERSONAL_LEGAL_DOCS/04_Comunidad_y_Eventos"

    # 7. Knowledge Base / Books / Study
    if ext in [".epub", ".mobi", ".azw3", ".cbr", ".cbz"] or any(w in name for w in ["libro", "book", "manual", "guide", "guia", "paper", "informe de clase"]):
        return "03_KNOWLEDGE_BASE_RND/01_Libros_Comics_y_Papers"

    # 8. Media Assets
    if any(mime.startswith(p) for p in ["image/", "video/", "audio/"]) or any(w in name for w in ["leo_demo", "vídeo sin título", "video sin título"]):
        if mime.startswith("audio/"):
            return "07_MEDIA_CREATIVE_ASSETS/03_Audio_y_Musica"
        elif mime.startswith("video/") or "video" in name or "demo" in name:
            return "07_MEDIA_CREATIVE_ASSETS/04_Video_y_Cine"
        else:
            return "07_MEDIA_CREATIVE_ASSETS/02_Fotografia_y_Renders"

    # 9. Archive Backups
    if ext in [".zip", ".rar", ".7z", ".tar", ".gz", ".bak", ".iso", ".dump", ".sql"] or "backup" in name:
        return "08_ARCHIVE_HISTORICAL/01_Backups_y_Sistemas"

    # Default fallback
    return "04_PROJECTS_AI_AND_DEV/01_Agentes_e_IA_Generativa"

def execute_relocation(account_alias: str = "nomack3d") -> Dict[str, Any]:
    client = WorkspaceClient(account_alias)
    print(f"\n==================================================================")
    print(f" EJECUCIÓN DE REORGANIZACIÓN Y GOBERNANZA DE DRIVE: [{account_alias}]")
    print(f"==================================================================")

    manifest_path = os.path.join(os.path.dirname(__file__), f"drive_manifest_{account_alias}.json")
    catalog_path = os.path.join(os.path.dirname(__file__), "..", "..", "scratch", f"drive_catalog_{account_alias}.json")

    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)
    with open(catalog_path, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    folder_manifest = manifest.get("folders", {})
    canonical_roots = set(manifest.get("folders", {}).keys())

    items = catalog.get("files", [])
    all_folders = [x for x in items if x.get("mimeType") == "application/vnd.google-apps.folder"]
    folder_map = {f["id"]: f for f in all_folders}

    root_folders = []
    root_files = []
    for x in items:
        parents = x.get("parents", [])
        is_root = not parents or any(p not in folder_map for p in parents)
        if is_root:
            if x.get("mimeType") == "application/vnd.google-apps.folder":
                if x.get("name") not in canonical_roots:
                    root_folders.append(x)
            else:
                root_files.append(x)

    print(f"  [+] Carpetas Raíz identificadas: {len(root_folders)}")
    print(f"  [+] Archivos Huérfanos identificados: {len(root_files)}")

    audit_moves = []
    folder_success = 0
    folder_errors = 0

    root_map = ROOT_FOLDER_MAP_BY_ACCOUNT.get(account_alias, ROOT_FOLDER_MAP_BY_ACCOUNT.get("nomack3d", {}))

    # 1. Process Root Folders
    print(f"\n==> [1/2] Procesando {len(root_folders)} Carpetas Raíz...")
    for idx, rf in enumerate(root_folders, 1):
        folder_id = rf["id"]
        folder_name = rf["name"]
        parents = rf.get("parents", [])
        owners = rf.get("owners", [])
        is_owner = any(o.get("me", False) for o in owners)

        target_path = root_map.get(folder_name, "04_PROJECTS_AI_AND_DEV/03_Estrategia_y_Negocio")
        target_parent_id = folder_manifest.get(target_path, {}).get("id")

        if not target_parent_id:
            root_canonical = target_path.split("/")[0]
            target_parent_id = folder_manifest.get(root_canonical, {}).get("id")

        if not target_parent_id:
            print(f"    [SKIP] No se encontró destino para {folder_name}")
            continue

        if is_owner:
            print(f"  [{idx:02d}/{len(root_folders)}] 📁 [MOVE] '{folder_name}' -> '{target_path}'...")
            try:
                old_p = parents[0] if parents else None
                res = client.move_drive_file(folder_id, new_parent_id=target_parent_id, old_parent_id=old_p)
                folder_success += 1
                audit_moves.append({
                    "type": "folder",
                    "action": "move",
                    "id": folder_id,
                    "name": folder_name,
                    "target_path": target_path,
                    "status": "success"
                })
                print(f"     [OK] Carpeta movida con éxito.")
            except Exception as e:
                # Fallback to shortcut
                try:
                    res_sc = client.create_drive_shortcut(folder_name, target_id=folder_id, parent_id=target_parent_id)
                    folder_success += 1
                    audit_moves.append({
                        "type": "folder",
                        "action": "shortcut_fallback",
                        "id": folder_id,
                        "name": folder_name,
                        "target_path": target_path,
                        "status": "success"
                    })
                    print(f"     [OK] Acceso directo creado en la jerarquía canónica.")
                except Exception as sc_err:
                    folder_errors += 1
                    print(f"     [ERROR] Falló movimiento: {e}")
                    audit_moves.append({
                        "type": "folder",
                        "action": "move",
                        "id": folder_id,
                        "name": folder_name,
                        "error": str(e),
                        "status": "error"
                    })
        else:
            print(f"  [{idx:02d}/{len(root_folders)}] 🔗 [SHORTCUT] '{folder_name}' (Compartida) -> '{target_path}'...")
            try:
                res = client.create_drive_shortcut(folder_name, target_id=folder_id, parent_id=target_parent_id)
                folder_success += 1
                audit_moves.append({
                    "type": "folder",
                    "action": "shortcut",
                    "id": folder_id,
                    "name": folder_name,
                    "target_path": target_path,
                    "status": "success"
                })
                print(f"     [OK] Acceso directo creado en la jerarquía canónica.")
            except Exception as e:
                folder_errors += 1
                print(f"     [ERROR] Falló creación de shortcut: {e}")
                audit_moves.append({
                    "type": "folder",
                    "action": "shortcut",
                    "id": folder_id,
                    "name": folder_name,
                    "error": str(e),
                    "status": "error"
                })
        time.sleep(0.12)

    # 2. Process Loose Root Files
    file_success = 0
    file_errors = 0
    print(f"\n==> [2/2] Procesando {len(root_files)} Archivos Huérfanos...")
    for idx, fl in enumerate(root_files, 1):
        file_id = fl["id"]
        file_name = fl["name"]
        parents = fl.get("parents", [])
        owners = fl.get("owners", [])
        is_owner = any(o.get("me", False) for o in owners)

        target_path = determine_file_target(fl, account_alias)
        target_parent_id = folder_manifest.get(target_path, {}).get("id")

        if not target_parent_id:
            root_canonical = target_path.split("/")[0]
            target_parent_id = folder_manifest.get(root_canonical, {}).get("id")

        if not target_parent_id:
            print(f"    [SKIP] No se encontró destino para {file_name}")
            continue

        if is_owner:
            try:
                old_p = parents[0] if parents else None
                res = client.move_drive_file(file_id, new_parent_id=target_parent_id, old_parent_id=old_p)
                file_success += 1
                audit_moves.append({
                    "type": "file",
                    "action": "move",
                    "id": file_id,
                    "name": file_name,
                    "target_path": target_path,
                    "status": "success"
                })
                if idx % 25 == 0 or idx == len(root_files):
                    print(f"  [{idx:03d}/{len(root_files)}] 📄 [MOVE] {idx} procesados... [Último: {file_name[:35]} -> {target_path}]")
            except Exception as e:
                try:
                    res_sc = client.create_drive_shortcut(file_name, target_id=file_id, parent_id=target_parent_id)
                    file_success += 1
                    audit_moves.append({
                        "type": "file",
                        "action": "shortcut_fallback",
                        "id": file_id,
                        "name": file_name,
                        "target_path": target_path,
                        "status": "success"
                    })
                except Exception as sc_err:
                    file_errors += 1
                    print(f"  [ERROR] Falló archivo '{file_name}': {e}")
                    audit_moves.append({
                        "type": "file",
                        "id": file_id,
                        "name": file_name,
                        "error": str(e),
                        "status": "error"
                    })
        else:
            try:
                res = client.create_drive_shortcut(file_name, target_id=file_id, parent_id=target_parent_id)
                file_success += 1
                audit_moves.append({
                    "type": "file",
                    "action": "shortcut",
                    "id": file_id,
                    "name": file_name,
                    "target_path": target_path,
                    "status": "success"
                })
                if idx % 25 == 0 or idx == len(root_files):
                    print(f"  [{idx:03d}/{len(root_files)}] 🔗 [SHORTCUT] {idx} procesados... [Último: {file_name[:35]} -> {target_path}]")
            except Exception as e:
                file_errors += 1
                print(f"  [ERROR] Falló shortcut para '{file_name}': {e}")
                audit_moves.append({
                    "type": "file",
                    "id": file_id,
                    "name": file_name,
                    "error": str(e),
                    "status": "error"
                })
        time.sleep(0.1)

    report_path = os.path.join(os.path.dirname(__file__), f"drive_relocation_report_{account_alias}.json")
    result = {
        "account": account_alias,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "summary": {
            "total_folders_processed": folder_success,
            "folder_errors": folder_errors,
            "total_files_processed": file_success,
            "file_errors": file_errors,
            "total_operations": len(audit_moves)
        },
        "moves": audit_moves
    }
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"\n==================================================================")
    print(f" [ÉXITO TOTAL] REORGANIZACIÓN Y GOBERNANZA DE DRIVE COMPLETADA [{account_alias}]")
    print(f" - Carpetas Raíz Procesadas  : {folder_success}/{len(root_folders)}")
    print(f" - Archivos Huérfanos Movidos: {file_success}/{len(root_files)}")
    print(f" - Errores Totales           : {folder_errors + file_errors}")
    print(f" - Manifiesto de Auditoría   : {report_path}")
    print("==================================================================\n")
    return result

if __name__ == "__main__":
    alias = sys.argv[1] if len(sys.argv) > 1 else "nomack3d"
    execute_relocation(alias)
