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
    
    # ===== GOOGLE SHEETS =====
    elif tool_name in ("sheets_get_values", "workspace_sheets_get_values"):
        return client.get_sheet_values(
            spreadsheet_id=arguments["spreadsheet_id"],
            range_name=arguments.get("range", "A1:Z100")
        )
    elif tool_name in ("sheets_update_values", "workspace_sheets_update_values"):
        return client.update_sheet_values(
            spreadsheet_id=arguments["spreadsheet_id"],
            range_name=arguments.get("range", "A1"),
            values=arguments.get("values", [])
        )
    elif tool_name in ("sheets_append_values", "workspace_sheets_append_values"):
        return client.append_sheet_values(
            spreadsheet_id=arguments["spreadsheet_id"],
            range_name=arguments.get("range", "A1"),
            values=arguments.get("values", [])
        )
    elif tool_name in ("sheets_create", "workspace_sheets_create"):
        return client.create_spreadsheet(
            title=arguments.get("title", "Nueva Hoja de Cálculo"),
            sheet_names=arguments.get("sheet_names")
        )
    
    # ===== GOOGLE SLIDES =====
    elif tool_name in ("slides_create", "workspace_slides_create"):
        return client.create_presentation(title=arguments.get("title", "Nueva Presentación"))
    elif tool_name in ("slides_get", "workspace_slides_get"):
        return client.get_presentation(presentation_id=arguments["presentation_id"])
    elif tool_name in ("slides_batch_update", "workspace_slides_batch_update"):
        return client.batch_update_presentation(
            presentation_id=arguments["presentation_id"],
            requests=arguments.get("requests", [])
        )

    # ===== GOOGLE VIDS =====
    elif tool_name in ("vids_list_projects", "workspace_vids_list_projects"):
        return client.list_vids_projects(
            page_size=int(arguments.get("page_size", 10)),
            query=arguments.get("query", "")
        )
    elif tool_name in ("vids_create_project", "workspace_vids_create_project"):
        return client.create_vids_project(
            title=arguments.get("title", "Nuevo Video Vids"),
            description=arguments.get("description", "")
        )

    # ===== GOOGLE ANALYTICS 4 =====
    elif tool_name in ("analytics_run_report", "workspace_analytics_run_report"):
        return client.run_analytics_report(
            property_id=arguments["property_id"],
            dimensions=arguments.get("dimensions", ["city", "browser"]),
            metrics=arguments.get("metrics", ["activeUsers", "screenPageViews"]),
            date_ranges=arguments.get("date_ranges"),
            limit=int(arguments.get("limit", 100))
        )
    elif tool_name in ("analytics_realtime_report", "workspace_analytics_realtime_report"):
        return client.run_realtime_analytics_report(
            property_id=arguments["property_id"],
            dimensions=arguments.get("dimensions", ["country"]),
            metrics=arguments.get("metrics", ["activeUsers"])
        )
    elif tool_name in ("analytics_account_summaries", "workspace_analytics_account_summaries"):
        return client.list_analytics_account_summaries()

    else:
        raise ValueError(f"Herramienta no reconocida: {tool_name}")

def main():
    if len(sys.argv) < 2:
        print("Uso: python mcp_workspace_server.py <tool_name> [--account <alias>] [--json <json_args>]")
        print("Herramientas: get_profile, list_messages, list_drive_files, about_storage, list_calendar_events,")
        print("              sheets_get_values, sheets_update_values, sheets_append_values, sheets_create,")
        print("              slides_create, slides_get, slides_batch_update,")
        print("              vids_list_projects, vids_create_project,")
        print("              analytics_run_report, analytics_realtime_report, analytics_account_summaries")
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
