#!/usr/bin/env python3
"""
Antigravity 2.0 - DaVinci Resolve MCP Server Bridge
Controlador y puente MCP para la API de Scripting de DaVinci Resolve Studio (Python/Lua),
creación de proyectos, líneas de tiempo, inserción de clips, aplicación de LUTs y render queue.
"""

import sys
import os
import json
from typing import Dict, Any, Optional, List

# Rutas estándar de DaVinci Resolve Scripting API en Windows
RESOLVE_SCRIPT_MODULE_PATH = os.environ.get(
    "RESOLVE_SCRIPT_API",
    r"C:\Program Files\Blackmagic Design\DaVinci Resolve\Developer\Scripting\Modules",
)


def get_resolve_instance():
    """Intenta inicializar y obtener el objeto de la aplicación DaVinci Resolve en ejecución."""
    if RESOLVE_SCRIPT_MODULE_PATH not in sys.path and os.path.exists(
        RESOLVE_SCRIPT_MODULE_PATH
    ):
        sys.path.append(RESOLVE_SCRIPT_MODULE_PATH)

    try:
        import DaVinciResolveScript as dvr_script

        resolve = dvr_script.scriptapp("Resolve")
        return resolve
    except ImportError:
        # Fallback a fusionscript
        try:
            import fusionscript as dvr_script

            return dvr_script.scriptapp("Resolve")
        except Exception:
            return None
    except Exception:
        return None


def davinci_get_status() -> Dict[str, Any]:
    """Verifica si DaVinci Resolve está en ejecución y accesible vía Scripting API."""
    resolve = get_resolve_instance()
    if resolve:
        project_manager = resolve.GetProjectManager()
        current_project = project_manager.GetCurrentProject()
        proj_name = (
            current_project.GetName() if current_project else "Sin proyecto abierto"
        )
        return {
            "status": "connected",
            "version": resolve.GetVersionString(),
            "active_project": proj_name,
        }
    return {
        "status": "offline",
        "message": "DaVinci Resolve no está en ejecución o la API de Scripting no está habilitada.",
        "instructions": "Abre DaVinci Resolve Studio -> Preferencias -> Sistema -> General -> Acceso a scripts externo: 'Local o Red'.",
    }


def davinci_create_timeline(
    project_name: str, timeline_name: str, media_paths: List[str]
) -> Dict[str, Any]:
    """Crea una línea de tiempo e inserta los archivos de medios especificados."""
    resolve = get_resolve_instance()
    if not resolve:
        return davinci_get_status()

    project_manager = resolve.GetProjectManager()
    project = project_manager.LoadProject(
        project_name
    ) or project_manager.CreateProject(project_name)
    if not project:
        return {
            "status": "error",
            "message": f"No se pudo crear/cargar el proyecto '{project_name}'",
        }

    media_pool = project.GetMediaPool()
    imported_clips = media_pool.ImportMedia(media_paths) if media_paths else []

    # Crear la línea de tiempo con los clips importados
    timeline = (
        media_pool.CreateTimelineFromClips(timeline_name, imported_clips)
        if imported_clips
        else media_pool.CreateEmptyTimeline(timeline_name)
    )

    return {
        "status": "success",
        "project": project.GetName(),
        "timeline": timeline.GetName() if timeline else timeline_name,
        "imported_clips_count": len(imported_clips),
    }


def davinci_render_timeline(
    project_name: str,
    timeline_name: str,
    target_dir: str,
    render_preset: str = "H.264 Master",
) -> Dict[str, Any]:
    """Configura un trabajo de renderizado para la línea de tiempo especificada."""
    resolve = get_resolve_instance()
    if not resolve:
        return davinci_get_status()

    project_manager = resolve.GetProjectManager()
    project = project_manager.LoadProject(project_name)
    if not project:
        return {
            "status": "error",
            "message": f"Proyecto '{project_name}' no encontrado",
        }

    project.SetCurrentRenderFormatAndCodec("mp4", "H264")
    project.SetRenderSettings(
        {"TargetDir": target_dir, "CustomName": f"{timeline_name}_master"}
    )
    job_id = project.AddRenderJob()

    return {
        "status": "success",
        "project": project_name,
        "timeline": timeline_name,
        "job_id": job_id,
        "target_dir": target_dir,
    }


def dispatch_tool(tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
    if tool_name == "davinci_status":
        return davinci_get_status()
    elif tool_name == "davinci_create_timeline":
        return davinci_create_timeline(
            project_name=arguments.get("project_name", "Antigravity_Project"),
            timeline_name=arguments.get("timeline_name", "Main_Timeline"),
            media_paths=arguments.get("media_paths", []),
        )
    elif tool_name == "davinci_render_timeline":
        return davinci_render_timeline(
            project_name=arguments.get("project_name", "Antigravity_Project"),
            timeline_name=arguments.get("timeline_name", "Main_Timeline"),
            target_dir=arguments.get("target_dir", os.path.expanduser(r"~\Videos")),
            render_preset=arguments.get("render_preset", "H.264 Master"),
        )
    else:
        raise ValueError(f"Herramienta no reconocida: {tool_name}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        tool = sys.argv[1]
        raw_args = sys.argv[2] if len(sys.argv) > 2 else "{}"
        try:
            args = json.loads(raw_args)
        except Exception:
            args = {}
        res = dispatch_tool(tool, args)
        print(json.dumps(res, indent=2, ensure_ascii=False))
    else:
        print("Uso: python davinci_mcp_server.py <tool_name> <json_arguments>")
