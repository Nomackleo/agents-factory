#!/usr/bin/env python3
"""
Antigravity 2.0 - Google Drive Canonical Hierarchy Provisioner
Provisions the 9 Canonical Root Folders and their subdirectories in Google Drive for nomackleo@gmail.com.
Idempotent execution with manifest export.
"""

import sys
import os
import json
import time
from typing import Dict, Any, List

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from workspace_client import WorkspaceClient

CANONICAL_HIERARCHY = {
    "00_GOVERNANCE_MY_BUSINESS": [
        "01_Identidad_y_Bio",
        "02_Contratos_Marco_y_NDAs"
    ],
    "01_FINANCIAL_OPS": [
        "01_Bancos_y_Extractos",
        "02_Facturas_y_Comprobantes",
        "03_Impuestos_y_DIAN",
        "04_Inversiones_y_Trading",
        "05_Produccion_y_Finanzas"
    ],
    "02_CLIENT_SERVICE_DELIVERY": [
        "01_Genesis_Legal",
        "01_Genesis_Legal/01_Capacitaciones_e_IA_Corporativa",
        "01_Genesis_Legal/02_Propuestas_y_Contratos",
        "01_Genesis_Legal/03_Cronogramas_e_Informes",
        "01_Genesis_Legal/04_Presentaciones_Ejecutivas",
        "01_Genesis_Legal/05_Prompts_y_Arquitectura_Modelos",
        "02_Kodland_Academy",
        "02_Kodland_Academy/Clases",
        "02_Kodland_Academy/Virtual_Backgrounds",
        "03_Otros_Clientes_y_Propuestas"
    ],
    "03_KNOWLEDGE_BASE_RND": [
        "01_Libros_Comics_y_Papers",
        "02_Academias_y_Cursos",
        "03_Becas_y_Convocatorias",
        "04_Notas_y_Manuales"
    ],
    "04_PROJECTS_AI_AND_DEV": [
        "01_Agentes_e_IA_Generativa",
        "02_Herramientas_y_Software",
        "03_Estrategia_y_Negocio"
    ],
    "05_PROJECTS_3D_CGI_VFX": [
        "01_Software_3ds_Max",
        "02_Animacion_y_Crowds",
        "03_Impresion_3D_y_Assets",
        "04_Escenas_y_Modelos_High"
    ],
    "06_PERSONAL_LEGAL_DOCS": [
        "01_CV_y_Perfiles",
        "02_Salud_y_EPS",
        "03_Familia_y_Hogar",
        "04_Comunidad_y_Eventos"
    ],
    "07_MEDIA_CREATIVE_ASSETS": [
        "01_Fotografia_y_Renders",
        "02_Audio_y_Musica",
        "03_Video_y_Cine"
    ],
    "08_ARCHIVE_HISTORICAL": [
        "01_Backups_Dropbox_y_Sistemas",
        "02_Archivos_Historicos_VFXLearning"
    ]
}

def provision_drive_structure(account_alias: str = "nomackleo") -> Dict[str, Any]:
    client = WorkspaceClient(account_alias)
    print(f"\n==================================================================")
    print(f" PROVISIÓN DE ESTRUCTURA CANÓNICA DE DRIVE: [{account_alias}]")
    print(f"==================================================================")

    # 1. Fetch existing folders in Drive to be strictly idempotent
    print(f"==> Verificando carpetas existentes en Drive...")
    query = "mimeType = 'application/vnd.google-apps.folder' and trashed = false"
    existing_folders_res = client.list_drive_files(page_size=500, query=query)
    existing_folders = {f["name"]: f for f in existing_folders_res.get("files", [])}
    print(f"  [+] Carpetas encontradas en el índice: {len(existing_folders)}")

    folder_manifest = {}

    # 2. Create Root Canonical Folders
    for root_name, subfolders in CANONICAL_HIERARCHY.items():
        if root_name in existing_folders:
            root_id = existing_folders[root_name]["id"]
            print(f"  [SKIP] Carpeta raíz ya existe: {root_name} (ID: {root_id})")
            folder_manifest[root_name] = {
                "id": root_id,
                "name": root_name,
                "parent_path": "root",
                "status": "existing"
            }
        else:
            print(f"  [CREATING] Carpeta raíz: {root_name}...")
            try:
                res = client.create_drive_folder(root_name)
                root_id = res["id"]
                print(f"    -> Creada con éxito. ID: {root_id}")
                existing_folders[root_name] = res
                folder_manifest[root_name] = {
                    "id": root_id,
                    "name": root_name,
                    "parent_path": "root",
                    "status": "created"
                }
            except Exception as e:
                print(f"    [ERROR] Falló creación de raíz {root_name}: {e}")
                continue

        time.sleep(0.2)

        # 3. Create Subfolders (handling nesting like A/B)
        for sub in subfolders:
            parts = sub.split("/")
            current_parent_path = root_name
            current_parent_id = root_id

            for i, part in enumerate(parts):
                current_full_path = f"{root_name}/" + "/".join(parts[:i+1])
                
                # Check if this exact path is already known
                if current_full_path in folder_manifest:
                    current_parent_id = folder_manifest[current_full_path]["id"]
                    current_parent_path = current_full_path
                    continue

                # Query if part exists under current_parent_id
                sub_q = f"mimeType = 'application/vnd.google-apps.folder' and name = '{part}' and '{current_parent_id}' in parents and trashed = false"
                sub_check = client.list_drive_files(page_size=5, query=sub_q).get("files", [])
                
                if sub_check:
                    sub_id = sub_check[0]["id"]
                    print(f"    [SKIP] Subcarpeta ya existe: {current_full_path} (ID: {sub_id})")
                    folder_manifest[current_full_path] = {
                        "id": sub_id,
                        "name": part,
                        "parent_path": current_parent_path,
                        "status": "existing"
                    }
                    current_parent_id = sub_id
                    current_parent_path = current_full_path
                else:
                    print(f"    [CREATING] Subcarpeta: {current_full_path}...")
                    try:
                        res_sub = client.create_drive_folder(part, parent_id=current_parent_id)
                        sub_id = res_sub["id"]
                        print(f"      -> Creada con éxito. ID: {sub_id}")
                        folder_manifest[current_full_path] = {
                            "id": sub_id,
                            "name": part,
                            "parent_path": current_parent_path,
                            "status": "created"
                        }
                        current_parent_id = sub_id
                        current_parent_path = current_full_path
                    except Exception as e:
                        print(f"      [ERROR] Falló creación de {current_full_path}: {e}")
                        break
                time.sleep(0.2)

    manifest_path = os.path.join(os.path.dirname(__file__), f"drive_manifest_{account_alias}.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump({
            "account": account_alias,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "total_folders": len(folder_manifest),
            "folders": folder_manifest
        }, f, indent=2, ensure_ascii=False)

    print(f"\n==================================================================")
    print(f" [ÉXITO] PROVISIÓN DE ESTRUCTURA CANÓNICA COMPLETADA")
    print(f" Total de Carpetas Canónicas Creadas/Registradas: {len(folder_manifest)}")
    print(f" Manifiesto Guardado en: {manifest_path}")
    print("==================================================================\n")
    return folder_manifest

if __name__ == "__main__":
    alias = sys.argv[1] if len(sys.argv) > 1 else "nomackleo"
    provision_drive_structure(alias)
