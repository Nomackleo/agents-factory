#!/usr/bin/env python3
"""
Antigravity 2.0 - Gmail Label Hierarchy & Taxonomy Provisioner
Creates deterministic, color-coded, hierarchical labels in Gmail (nomackleo@gmail.com)
without modifying or moving any emails (read-only audit compliance).
"""

import sys
import os
import json
import time

# Add mcp/google-workspace to sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from workspace_client import WorkspaceClient

# Valid Gmail API Color Palette Pairs:
# Green (Clients/Entities): bg '#16a766', text '#ffffff'
# Blue (Jobs/Career): bg '#4a86e8', text '#ffffff'
# Amber/Orange (Education/Courses): bg '#ffad47', text '#000000'
# Purple (Tech/AI/Dev): bg '#a479e2', text '#ffffff'
# Mint/Emerald (Finances/Bills): bg '#43d692', text '#000000'
# Coral/Red (E-Commerce/Retail): bg '#fb4c2f', text '#ffffff'

LABEL_DEFINITIONS = [
    # 1. CLIENTES Y ENTIDADES (Green)
    {
        "name": "01_CLIENTES_Y_ENTIDADES",
        "bg": "#16a766", "text": "#ffffff",
        "children": [
            "Camara_Comercio_Bogota",
            "SCRD_Cultura_Bogota",
            "Famisanar_EPS",
            "Niilo_Consulting",
            "BBI_Corporativo",
            "Colombia_Tech_Week"
        ]
    },
    # 2. OFERTAS DE EMPLEO Y TALENTO (Blue)
    {
        "name": "02_OFERTAS_EMPLEO_Y_TALENTO",
        "bg": "#4a86e8", "text": "#ffffff",
        "children": [
            "CompuTrabajo",
            "LinkedIn_Jobs",
            "UnMejorEmpleo",
            "Intch_Networking"
        ]
    },
    # 3. EDUCACION Y CERTIFICACIONES (Amber/Orange)
    {
        "name": "03_EDUCACION_Y_CERTIFICACIONES",
        "bg": "#ffad47", "text": "#000000",
        "children": [
            "Udemy",
            "Google_Skills_Boost",
            "Tech_Global_University",
            "UdeCataluna",
            "BIG_School",
            "Founderz",
            "GrowUp_Analytics",
            "Autodesk_Tinkercad"
        ]
    },
    # 4. TECNOLOGIA, IA Y DESARROLLADORES (Purple)
    {
        "name": "04_TECNOLOGIA_IA_Y_DEV",
        "bg": "#a479e2", "text": "#ffffff",
        "children": [
            "Google_Cloud_Ecosystem",
            "OpenAI",
            "NVIDIA",
            "ArtStation_3D",
            "Meshy_3D_AI",
            "Devpost_Hackathons",
            "Medium_Tech_Digest",
            "DEV_Community",
            "OpenCV_Computer_Vision",
            "Filestack_API",
            "Rokoko_Mocap",
            "LottieFiles_Design",
            "Mermaid_AI",
            "WooCommerce",
            "Adobe_Creative_Cloud"
        ]
    },
    # 5. FINANZAS, BANCA Y FACTURAS (Mint/Emerald)
    {
        "name": "05_FINANZAS_BANCA_Y_FACTURAS",
        "bg": "#43d692", "text": "#000000",
        "children": [
            "Davivienda",
            "Banco_Falabella",
            "Nu_Bank",
            "Addi_Fintech",
            "PSE_Pasarelas",
            "Baloto_Loterias",
            "Movistar_Servicios",
            "Educacion_Financiera"
        ]
    },
    # 6. E-COMMERCE Y RETAIL (Coral/Red)
    {
        "name": "06_ECOMMERCE_Y_RETAIL",
        "bg": "#fb4c2f", "text": "#ffffff",
        "children": [
            "Dafiti",
            "Adidas",
            "Samsung",
            "Sony",
            "Shein",
            "Malwarebytes_Software"
        ]
    }
]

def provision_labels(account_alias="nomackleo"):
    client = WorkspaceClient(account_alias)
    print(f"==> Iniciando provisión de etiquetas para: {account_alias}")
    
    # 1. Fetch existing labels
    existing_resp = client.list_labels()
    existing_labels = {l.get("name"): l for l in existing_resp.get("labels", [])}
    print(f"  [+] Etiquetas existentes encontradas: {len(existing_labels)}")
    
    audit_results = []
    
    for group in LABEL_DEFINITIONS:
        parent_name = group["name"]
        bg = group["bg"]
        text = group["text"]
        
        # Create or verify parent label
        if parent_name in existing_labels:
            print(f"  [SKIP] Etiqueta raíz ya existe: {parent_name} (ID: {existing_labels[parent_name]['id']})")
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
        
        # Create or verify children labels
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
            
    # Save provisioning audit manifest
    audit_file = os.path.join(os.path.dirname(__file__), "labels_provisioned_manifest.json")
    with open(audit_file, "w", encoding="utf-8") as f:
        json.dump({
            "account": account_alias,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "total_labels": len(audit_results),
            "labels": audit_results
        }, f, indent=2, ensure_ascii=False)
        
    print(f"\n==================================================================")
    print(f" [ÉXITO TOTAL] PROVISIÓN DE ETIQUETAS COMPLETADA ({len(audit_results)} etiquetas)")
    print(f" Manifiesto de Auditoría: {audit_file}")
    print("==================================================================\n")

if __name__ == "__main__":
    alias = sys.argv[1] if len(sys.argv) > 1 else "nomackleo"
    provision_labels(alias)
