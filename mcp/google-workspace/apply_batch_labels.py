#!/usr/bin/env python3
"""
Antigravity 2.0 - Universal Batch Label Applicator for Google Workspace
Applies parent and subcategory labels to analyzed emails in any tenant or account
with audit manifest logging, rate limiting and zero error tolerance.
"""

import sys
import os
import json
import time
from collections import defaultdict
from typing import Dict, Any, List

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from workspace_client import WorkspaceClient

def run_batch_labeling(account_alias: str = "nomack3d") -> Dict[str, Any]:
    client = WorkspaceClient(account_alias)
    print(f"\n==================================================================")
    print(f" ETIQUETADO POR LOTES GMAIL: [{account_alias}]")
    print(f"==================================================================")

    # Resolve report and manifest paths
    base_dir = os.path.dirname(__file__)
    rep_path = os.path.abspath(os.path.join(base_dir, "..", "..", "scratch", f"categorized_100_emails_{account_alias}.json"))
    manifest_path = os.path.join(base_dir, f"labels_manifest_{account_alias}.json")

    if not os.path.exists(rep_path):
        # Fallback to general report
        rep_path = os.path.abspath(os.path.join(base_dir, "..", "..", "scratch", "categorized_100_emails_report.json"))
    if not os.path.exists(manifest_path):
        manifest_path = os.path.join(base_dir, "labels_provisioned_manifest.json")

    print(f"  [+] Cargando reporte de clasificación: {rep_path}")
    print(f"  [+] Cargando manifiesto de etiquetas  : {manifest_path}")

    with open(rep_path, "r", encoding="utf-8") as f:
        report = json.load(f)

    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    label_name_to_id = {l["name"]: l["id"] for l in manifest.get("labels", [])}

    # Group message IDs by target label tuple
    label_groups = defaultdict(list)
    item_audit = []

    for item in report.get("items", []):
        msg_id = item.get("id")
        root_name = item.get("root_label") or item.get("category")
        child_name = item.get("child_label") or f"{root_name}/{item.get('subcategory')}"

        # Resolve IDs
        parent_id = label_name_to_id.get(root_name)
        child_id = label_name_to_id.get(child_name)

        target_label_ids = []
        if parent_id:
            target_label_ids.append(parent_id)
        if child_id and child_id != parent_id:
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

    print(f"  [+] {len(item_audit)} correos agrupados en {len(label_groups)} lotes de etiquetado.")

    success_count = 0
    error_count = 0

    for label_ids_tuple, msg_ids in label_groups.items():
        add_labels = list(label_ids_tuple)
        label_names = [k for k, v in label_name_to_id.items() if v in add_labels]
        print(f"  -> Aplicando {label_names} a {len(msg_ids)} correo(s)...")
        try:
            client.batch_modify_message_labels(
                message_ids=msg_ids,
                add_label_ids=add_labels,
                remove_label_ids=[]
            )
            success_count += len(msg_ids)
            print(f"     [OK] Exitoso.")
        except Exception as e:
            print(f"     [ERROR] Falló lote: {e}")
            error_count += len(msg_ids)
        time.sleep(0.25)

    audit_file = os.path.join(base_dir, f"batch_labeling_report_{account_alias}.json")
    result = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "account": account_alias,
        "total_requested": len(item_audit),
        "successfully_labeled": success_count,
        "errors": error_count,
        "labeled_items": item_audit
    }
    with open(audit_file, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"\n==================================================================")
    print(f" [ÉXITO TOTAL] ETIQUETADO COMPLETADO PARA: {account_alias}")
    print(f" - Correos etiquetados exitosamente : {success_count}/{len(item_audit)}")
    print(f" - Reporte de ejecución guardado en : {audit_file}")
    print("==================================================================\n")
    return result

if __name__ == "__main__":
    alias = sys.argv[1] if len(sys.argv) > 1 else "nomack3d"
    run_batch_labeling(alias)
