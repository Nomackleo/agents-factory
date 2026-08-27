#!/usr/bin/env python3
"""
Antigravity 2.0 - Blender MCP Server Bridge
Controlador y puente MCP para automatización headless de Blender (bpy),
generación de geometría procedural, renderizado Eevee Next / Cycles y exportación GLTF/GLB.
"""

import sys
import os
import json
import subprocess
import argparse
from typing import Dict, Any, Optional, List

BLENDER_EXE_PATH = os.environ.get("BLENDER_EXE_PATH", r"C:\Program Files\Blender Foundation\Blender 4.5\blender.exe")
if not os.path.exists(BLENDER_EXE_PATH):
    # Fallbacks comunes
    alt_paths = [
        r"C:\Program Files\Blender Foundation\Blender 4.4\blender.exe",
        r"C:\Program Files\Blender Foundation\Blender 4.3\blender.exe",
        r"C:\Program Files\Blender Foundation\Blender 4.2\blender.exe",
        r"C:\Program Files\Blender Foundation\Blender\blender.exe"
    ]
    for p in alt_paths:
        if os.path.exists(p):
            BLENDER_EXE_PATH = p
            break

def run_blender_script(script_content: str, blend_file: Optional[str] = None, extra_args: Optional[List[str]] = None) -> Dict[str, Any]:
    """Ejecuta un script Python arbitrario dentro de Blender en modo headless (--background)."""
    scratch_dir = os.path.expanduser(r"~\.gemini\antigravity-ide\scratch")
    os.makedirs(scratch_dir, exist_ok=True)
    temp_script = os.path.join(scratch_dir, "temp_blender_exec.py")
    
    with open(temp_script, "w", encoding="utf-8") as f:
        f.write(script_content)

    cmd = [BLENDER_EXE_PATH, "--background"]
    if blend_file and os.path.exists(blend_file):
        cmd.append(blend_file)
    cmd.extend(["--python", temp_script])
    if extra_args:
        cmd.extend(extra_args)

    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {
            "status": "success",
            "blender_path": BLENDER_EXE_PATH,
            "stdout": proc.stdout,
            "stderr": proc.stderr
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "error",
            "blender_path": BLENDER_EXE_PATH,
            "message": f"Error ejecutando Blender: {e}",
            "stdout": e.stdout,
            "stderr": e.stderr
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
            "note": "Asegúrate de que Blender esté instalado o define la variable de entorno BLENDER_EXE_PATH."
        }

def blender_render_frame(blend_file: str, frame: int, output_path: str, engine: str = "BLENDER_EEVEE_NEXT") -> Dict[str, Any]:
    """Renderiza un fotograma específico de una escena .blend."""
    script = f"""
import bpy
bpy.context.scene.render.engine = '{engine}'
bpy.context.scene.render.filepath = r'{output_path}'
bpy.context.scene.frame_set({frame})
bpy.ops.render.render(write_still=True)
print('[BLENDER_MCP_OK] Frame {frame} rendered to {output_path}')
"""
    return run_blender_script(script, blend_file=blend_file)

def blender_export_gltf(blend_file: str, output_glb: str) -> Dict[str, Any]:
    """Exporta una escena o colección .blend hacia un archivo binario optimizado GLTF/GLB."""
    script = f"""
import bpy
bpy.ops.export_scene.gltf(
    filepath=r'{output_glb}',
    export_format='GLB',
    export_apply=True,
    export_materials='EXPORT',
    export_colors=True
)
print('[BLENDER_MCP_OK] Scene exported to GLB: {output_glb}')
"""
    return run_blender_script(script, blend_file=blend_file)

def dispatch_tool(tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
    if tool_name == "blender_render_frame":
        return blender_render_frame(
            blend_file=arguments.get("blend_file", ""),
            frame=int(arguments.get("frame", 1)),
            output_path=arguments.get("output_path", "output_frame.png"),
            engine=arguments.get("engine", "BLENDER_EEVEE_NEXT")
        )
    elif tool_name == "blender_export_gltf":
        return blender_export_gltf(
            blend_file=arguments.get("blend_file", ""),
            output_glb=arguments.get("output_glb", "output_scene.glb")
        )
    elif tool_name == "blender_execute_script":
        return run_blender_script(
            script_content=arguments.get("script_content", ""),
            blend_file=arguments.get("blend_file")
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
        print("Uso: python blender_mcp_server.py <tool_name> <json_arguments>")
