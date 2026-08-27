#!/usr/bin/env python3
"""
Eliminación de correos de Udemy en nomackleo@gmail.com tras confirmación HITL del usuario.
"""

import os
import sys
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from workspace_client import WorkspaceClient

def main():
    if sys.platform == "win32":
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

    qa_report_file = os.path.join(current_dir, "qa_execution_report.json")
    if not os.path.exists(qa_report_file):
        print("[ERROR] No se encontró qa_execution_report.json")
        return

    with open(qa_report_file, "r", encoding="utf-8") as f:
        qa_data = json.load(f)

    udemy_msgs = qa_data.get("4.4_udemy_emails", {}).get("messages", [])
    if not udemy_msgs:
        print("[INFO] No se encontraron mensajes de Udemy registrados.")
        return

    msg_ids = [m["id"] for m in udemy_msgs]
    print(f"==> Procediendo a eliminar {len(msg_ids)} correos de Udemy con confirmación HITL...")

    client = WorkspaceClient("nomackleo")
    try:
        results = client.batch_trash_messages(msg_ids, hitl_confirmed=True)
        success_count = sum(1 for r in results if r.get("status") == "trashed")
        print(f"✔ [ÉXITO] {success_count}/{len(msg_ids)} correos de Udemy movidos a la Papelera de nomackleo@gmail.com.")
    except Exception as e:
        print(f"✖ [ERROR] Falló la operación: {e}")

if __name__ == "__main__":
    main()
