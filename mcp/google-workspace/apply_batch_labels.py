#!/usr/bin/env python3
"""
Antigravity 2.0 - Batch Label Applicator for Gmail
Applies parent and subcategory labels to the 100 analyzed emails in nomackleo@gmail.com
with audit verification and error recovery.
"""

import sys
import os
import json
import time
from collections import defaultdict

# Add mcp/google-workspace to sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from workspace_client import WorkspaceClient

def run_batch_labeling(account_alias="nomackleo"):
    client = WorkspaceClient(account_alias)
    print(f"==> [1/2] Cargando reportes y manifiesto de etiquetas...")
    
    rep_path = os.path.join(os.path.dirname(__file__), "..", "..", "scratch", "categorized_100_emails_report.json")
    manifest_path = os.path.join(os.path.dirname(__file__), "labels_provisioned_manifest.json")
    
    with open(rep_path, "r", encoding="utf-8") as f:
        report = json.load(f)
        
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)
        
    label_name_to_id = {l["name"]: l["id"] for l in manifest.get("labels", [])}
    
    # Map category names to root label names
    category_to_root = {
        "01_EDUCACION_CAPACITACION": "03_EDUCACION_Y_CERTIFICACIONES",
        "02_EMPLEO_TALENTO": "02_OFERTAS_EMPLEO_Y_TALENTO",
        "03_CLIENTES_ENTIDADES": "01_CLIENTES_Y_ENTIDADES",
        "04_FINANZAS_SERVICIOS": "05_FINANZAS_BANCA_Y_FACTURAS",
        "05_TECH_IA_DEV": "04_TECNOLOGIA_IA_Y_DEV",
        "06_ECOMMERCE_RETAIL": "06_ECOMMERCE_Y_RETAIL",
        "07_GENERAL_NOTIFICACIONES": "04_TECNOLOGIA_IA_Y_DEV"  # fallback or tech
    }
    
    # Group message IDs by (parent_label_id, child_label_id)
    label_groups = defaultdict(list)
    item_audit = []
    
    for item in report.get("items", []):
        msg_id = item.get("id")
        cat = item.get("category")
        sub = item.get("subcategory")
        
        root_name = category_to_root.get(cat, "04_TECNOLOGIA_IA_Y_DEV")
        child_name = f"{root_name}/{sub}"
        
        parent_id = label_name_to_id.get(root_name)
        child_id = label_name_to_id.get(child_name)
        
        target_label_ids = []
        if parent_id:
            target_label_ids.append(parent_id)
        if child_id:
            target_label_ids.append(child_id)
            
        if target_label_ids:
            key = tuple(target_label_ids)
            label_groups[key].append(msg_id)
            item_audit.append({
                "msg_id": msg_id,
                "from": item.get("from"),
                "subject": item.get("subject"),
                "labels_assigned": [root_name] + ([child_name] if child_id else [])
            })
            
    print(f"  [+] {len(item_audit)} correos agrupados en {len(label_groups)} conjuntos de etiquetas.")
    
    print(f"\n==> [2/2] Aplicando etiquetas por lotes en Gmail API...")
    success_count = 0
    error_count = 0
    
    for label_ids_tuple, msg_ids in label_groups.items():
        add_labels = list(label_ids_tuple)
        label_names = [k for k, v in label_name_to_id.items() if v in add_labels]
        print(f"  -> Aplicando etiquetas {label_names} a {len(msg_ids)} mensaje(s)...")
        try:
            client.batch_modify_message_labels(
                message_ids=msg_ids,
                add_label_ids=add_labels,
                remove_label_ids=[]
            )
            success_count += len(msg_ids)
            print(f"     [OK] Etiquetados con éxito.")
        except Exception as e:
            print(f"     [ERROR] Falló lote: {e}")
            error_count += len(msg_ids)
        time.sleep(0.3)
        
    audit_file = os.path.join(os.path.dirname(__file__), "batch_labeling_execution_report.json")
    with open(audit_file, "w", encoding="utf-8") as f:
        json.dump({
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "account": account_alias,
            "total_requested": len(item_audit),
            "successfully_labeled": success_count,
            "errors": error_count,
            "labeled_items": item_audit
        }, f, indent=2, ensure_ascii=False)
        
    print(f"\n==================================================================")
    print(f" [ÉXITO TOTAL] PROCESO DE ETIQUETADO COMPLETADO")
    print(f" - Correos etiquetados exitosamente : {success_count}")
    print(f" - Reporte de ejecución guardado en : {audit_file}")
    print("==================================================================\n")

if __name__ == "__main__":
    alias = sys.argv[1] if len(sys.argv) > 1 else "nomackleo"
    run_batch_labeling(alias)
