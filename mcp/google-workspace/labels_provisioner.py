#!/usr/bin/env python3
"""
Antigravity 2.0 - Multi-Tenant Label Provisioner
Provisions deterministic, hierarchical, color-coded labels in Gmail API for any account.
Supports account-specific taxonomies and namespaced manifests.
"""

import sys
import os
import json
import time
from typing import Dict, Any, List

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from workspace_client import WorkspaceClient

# Taxonomy definitions by account
TAXONOMIES = {
    "nomackleo": [
        {
            "name": "01_CLIENTES_Y_ENTIDADES",
            "bg": "#16a766", "text": "#ffffff",
            "children": [
                "Camara_Comercio_Bogota", "SCRD_Cultura_Bogota", "Famisanar_EPS",
                "Niilo_Consulting", "BBI_Corporativo", "Colombia_Tech_Week"
            ]
        },
        {
            "name": "02_OFERTAS_EMPLEO_Y_TALENTO",
            "bg": "#4a86e8", "text": "#ffffff",
            "children": ["CompuTrabajo", "LinkedIn_Jobs", "UnMejorEmpleo", "Intch_Networking"]
        },
        {
            "name": "03_EDUCACION_Y_CERTIFICACIONES",
            "bg": "#ffad47", "text": "#000000",
            "children": [
                "Udemy", "Google_Skills_Boost", "Tech_Global_University",
                "UdeCataluna", "BIG_School", "Founderz", "GrowUp_Analytics", "Autodesk_Tinkercad"
            ]
        },
        {
            "name": "04_TECNOLOGIA_IA_Y_DEV",
            "bg": "#a479e2", "text": "#ffffff",
            "children": [
                "Google_Cloud_Ecosystem", "OpenAI", "NVIDIA", "ArtStation_3D",
                "Meshy_3D_AI", "Devpost_Hackathons", "Medium_Tech_Digest", "DEV_Community",
                "OpenCV_Computer_Vision", "Filestack_API", "Rokoko_Mocap", "LottieFiles_Design",
                "Mermaid_AI", "WooCommerce", "Adobe_Creative_Cloud"
            ]
        },
        {
            "name": "05_FINANZAS_BANCA_Y_FACTURAS",
            "bg": "#43d692", "text": "#000000",
            "children": [
                "Davivienda", "Banco_Falabella", "Nu_Bank", "Addi_Fintech",
                "PSE_Pasarelas", "Baloto_Loterias", "Movistar_Servicios", "Educacion_Financiera"
            ]
        },
        {
            "name": "06_ECOMMERCE_Y_RETAIL",
            "bg": "#fb4c2f", "text": "#ffffff",
            "children": ["Dafiti", "Adidas", "Samsung", "Sony", "Shein", "Malwarebytes_Software"]
        }
    ],
    "nomack3d": [
        {
            "name": "01_CLIENTES_Y_ENTIDADES",
            "bg": "#16a766", "text": "#ffffff",
            "children": [
                "Genesis_Legal",
                "Proyectos_Leonel",
                "Mauricio_Gamboa",
                "Consultoria_Forense"
            ]
        },
        {
            "name": "02_OFERTAS_EMPLEO_Y_TALENTO",
            "bg": "#4a86e8", "text": "#ffffff",
            "children": [
                "Get_On_Board",
                "Portales_Tech"
            ]
        },
        {
            "name": "03_EDUCACION_Y_CERTIFICACIONES",
            "bg": "#ffad47", "text": "#000000",
            "children": [
                "British_Council_Ingles",
                "Google_Skills_Boost",
                "Academias_Online"
            ]
        },
        {
            "name": "04_TECNOLOGIA_IA_Y_DEV",
            "bg": "#a479e2", "text": "#ffffff",
            "children": [
                "Google_Cloud_Gemini",
                "GitHub_OpenSource",
                "OpenAI_ChatGPT",
                "NVIDIA_Cosmos_AI",
                "Warp_Terminal_Agent",
                "ComfyUI_Generative",
                "Sketchfab_3D_KitBash",
                "Napkin_AI",
                "Voidzero_ViteConf",
                "Medium_Tech_Digest"
            ]
        },
        {
            "name": "05_FINANZAS_BANCA_Y_FACTURAS",
            "bg": "#43d692", "text": "#000000",
            "children": [
                "Banca_Facturas",
                "Google_Workspace_Billing"
            ]
        },
        {
            "name": "06_ECOMMERCE_Y_RETAIL",
            "bg": "#fb4c2f", "text": "#ffffff",
            "children": [
                "Promociones_Compras"
            ]
        },
        {
            "name": "07_REDES_Y_COMUNIDAD",
            "bg": "#4a86e8", "text": "#ffffff",
            "children": [
                "Facebook"
            ]
        },
        {
            "name": "08_SISTEMA_Y_NOTIFICACIONES",
            "bg": "#666666", "text": "#ffffff",
            "children": [
                "Mailer_Daemon_Bounces",
                "Alertas_Seguridad_Google"
            ]
        }
    ]
}

def provision_account_labels(account_alias: str = "nomack3d") -> Dict[str, Any]:
    client = WorkspaceClient(account_alias)
    print(f"\n==================================================================")
    print(f" APROVISIONAMIENTO DE ETIQUETAS GMAIL: [{account_alias}]")
    print(f"==================================================================")

    taxonomy = TAXONOMIES.get(account_alias, TAXONOMIES["nomack3d"])
    existing_resp = client.list_labels()
    existing_labels = {l.get("name"): l for l in existing_resp.get("labels", [])}
    print(f"  [+] Etiquetas existentes encontradas: {len(existing_labels)}")

    audit_results = []

    for group in taxonomy:
        parent_name = group["name"]
        bg = group["bg"]
        text = group["text"]

        if parent_name in existing_labels:
            print(f"  [SKIP] Etiqueta raíz ya existe: {parent_name}")
            parent_meta = existing_labels[parent_name]
            audit_results.append({
                "name": parent_name,
                "id": parent_meta["id"],
                "status": "existing",
                "color": parent_meta.get("color", {"backgroundColor": bg, "textColor": text})
            })
        else:
            print(f"  [CREATING] Etiqueta raíz: {parent_name} (Color: {bg})")
            try:
                created = client.create_label(parent_name, background_color=bg, text_color=text)
                print(f"    -> Creada con éxito. ID: {created.get('id')}")
                existing_labels[parent_name] = created
                audit_results.append({
                    "name": parent_name,
                    "id": created.get("id"),
                    "status": "created",
                    "color": {"backgroundColor": bg, "textColor": text}
                })
            except Exception as e:
                print(f"    [ERROR] Falló creación de {parent_name}: {e}")
                audit_results.append({"name": parent_name, "status": "error", "error": str(e)})

        time.sleep(0.2)

        for child in group["children"]:
            child_full_name = f"{parent_name}/{child}"
            if child_full_name in existing_labels:
                print(f"    [SKIP] Sub-etiqueta ya existe: {child_full_name}")
                c_meta = existing_labels[child_full_name]
                audit_results.append({
                    "name": child_full_name,
                    "id": c_meta["id"],
                    "status": "existing",
                    "color": c_meta.get("color", {"backgroundColor": bg, "textColor": text})
                })
            else:
                print(f"    [CREATING] Sub-etiqueta: {child_full_name}")
                try:
                    c_created = client.create_label(child_full_name, background_color=bg, text_color=text)
                    print(f"      -> Creada con éxito. ID: {c_created.get('id')}")
                    existing_labels[child_full_name] = c_created
                    audit_results.append({
                        "name": child_full_name,
                        "id": c_created.get("id"),
                        "status": "created",
                        "color": {"backgroundColor": bg, "textColor": text}
                    })
                except Exception as e:
                    print(f"      [ERROR] Falló creación de {child_full_name}: {e}")
                    audit_results.append({"name": child_full_name, "status": "error", "error": str(e)})
            time.sleep(0.2)

    manifest_file = os.path.join(os.path.dirname(__file__), f"labels_manifest_{account_alias}.json")
    result = {
        "account": account_alias,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "total_labels": len(audit_results),
        "labels": audit_results
    }
    with open(manifest_file, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"\n==================================================================")
    print(f" [ÉXITO TOTAL] PROVISIÓN DE ETIQUETAS COMPLETADA ({len(audit_results)} etiquetas)")
    print(f" Manifiesto de Auditoría: {manifest_file}")
    print("==================================================================\n")
    return result

if __name__ == "__main__":
    alias = sys.argv[1] if len(sys.argv) > 1 else "nomack3d"
    provision_account_labels(alias)
