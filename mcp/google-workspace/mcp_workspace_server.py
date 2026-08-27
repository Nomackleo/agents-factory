#!/usr/bin/env python3
"""
Antigravity 2.0 - Standalone Google Workspace MCP Server & CLI Bridge
Expone herramientas tipadas para interactuar con Gmail, Drive y Calendar
soportando múltiples cuentas (nomackleo, nomack3d, genesis-legal).
"""

import sys
import os
import json
import argparse
from typing import Dict, Any, Optional

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from workspace_client import WorkspaceClient

def dispatch_tool(tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
    account = arguments.get("account", "nomackleo")
    client = WorkspaceClient(account)

    if tool_name in ("workspace_get_profile", "get_profile"):
        return client.get_gmail_profile()
    elif tool_name in ("workspace_list_messages", "list_messages"):
        max_results = int(arguments.get("max_results", 10))
        query = arguments.get("query", "")
        return client.list_gmail_messages(max_results=max_results, query=query)
    elif tool_name in ("workspace_list_drive_files", "list_drive_files"):
        page_size = int(arguments.get("page_size", 10))
        query = arguments.get("query", "")
        return client.list_drive_files(page_size=page_size, query=query)
    elif tool_name in ("workspace_about_storage", "about_storage"):
        return client.get_drive_about()
    elif tool_name in ("workspace_list_calendar_events", "list_calendar_events"):
        max_results = int(arguments.get("max_results", 10))
        return client.list_calendar_events(max_results=max_results)
    elif tool_name in ("workspace_list_calendars", "list_calendars"):
        return client.list_calendars()
    else:
        raise ValueError(f"Herramienta no reconocida: {tool_name}")

def main():
    if len(sys.argv) < 2:
        print("Uso: python mcp_workspace_server.py <tool_name> [--account <alias>] [--max_results <N>] [--query <q>]")
        print("Herramientas: get_profile, list_messages, list_drive_files, about_storage, list_calendar_events, list_calendars")
        sys.exit(1)

    tool_name = sys.argv[1]
    parser = argparse.ArgumentParser(description="Google Workspace MCP Tool Runner")
    parser.add_argument("tool", help="Nombre de la herramienta")
    parser.add_argument("--account", default="nomackleo", help="Alias de cuenta (nomackleo, nomack3d)")
    parser.add_argument("--max_results", type=int, default=10, help="Resultados máximos")
    parser.add_argument("--page_size", type=int, default=10, help="Tamaño de página")
    parser.add_argument("--query", default="", help="Query de búsqueda")
    parser.add_argument("--json", default=None, help="JSON de argumentos")

    parsed, unknown = parser.parse_known_args()
    args_dict = {
        "account": parsed.account,
        "max_results": parsed.max_results,
        "page_size": parsed.page_size,
        "query": parsed.query
    }
    
    if parsed.json:
        try:
            args_dict.update(json.loads(parsed.json))
        except Exception:
            pass

    try:
        res = dispatch_tool(tool_name, args_dict)
        print(json.dumps(res, indent=2, ensure_ascii=False))
    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e)}, indent=2))

if __name__ == "__main__":
    main()
