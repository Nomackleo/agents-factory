#!/usr/bin/env python3
"""
Antigravity 2.0 - Creative Asset Suite MCP Server (Affinity / Inkscape / ImageMagick / OTIO)
Controlador para la generación y post-procesamiento de activos 2D, conversiones vectoriales
y exportación de líneas de tiempo en formato estándar OpenTimelineIO.
"""

import sys
import os
import json
import subprocess
from typing import Dict, Any, Optional, List

def inkscape_render_svg(svg_path: str, output_png: str, width: int = 1920, height: int = 1080) -> Dict[str, Any]:
    """Renderiza un archivo SVG hacia PNG de alta resolución usando Inkscape CLI."""
    inkscape_paths = [
        r"C:\Program Files\Inkscape\bin\inkscape.exe",
        r"C:\Program Files\Inkscape\inkscape.exe"
    ]
    exe = next((p for p in inkscape_paths if os.path.exists(p)), "inkscape")

    cmd = [exe, svg_path, f"--export-filename={output_png}", f"--export-width={width}", f"--export-height={height}"]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {"status": "success", "output": output_png, "stdout": proc.stdout}
    except Exception as e:
        return {"status": "error", "message": str(e), "hint": "Asegúrate de que Inkscape esté instalado en PATH o Program Files."}

def imagemagick_apply_lut(input_image: str, lut_image: str, output_image: str) -> Dict[str, Any]:
    """Aplica una tabla de gradación de color (HALD CLUT / LUT) sobre una imagen usando ImageMagick."""
    cmd = ["magick", input_image, lut_image, "-hald-clut", output_image]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {"status": "success", "output": output_image, "stdout": proc.stdout}
    except Exception as e:
        return {"status": "error", "message": str(e), "hint": "Asegúrate de que ImageMagick esté instalado."}

def export_opentimelineio_json(clips_data: List[Dict[str, Any]], output_otio: str) -> Dict[str, Any]:
    """Genera un archivo estándar de intercambio OpenTimelineIO (OTIO) compatible con DaVinci Resolve, Premiere y Blender."""
    otio_structure = {
        "OTIO_SCHEMA": "Timeline.1",
        "name": "Antigravity_Montage_Timeline",
        "tracks": {
            "OTIO_SCHEMA": "Stack.1",
            "children": [
                {
                    "OTIO_SCHEMA": "Track.1",
                    "name": "Video Track 1",
                    "kind": "Video",
                    "children": clips_data
                }
            ]
        }
    }
    with open(output_otio, "w", encoding="utf-8") as f:
        json.dump(otio_structure, f, indent=2)
    return {"status": "success", "file": output_otio, "clips_count": len(clips_data)}

def dispatch_tool(tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
    if tool_name == "render_svg":
        return inkscape_render_svg(
            svg_path=arguments.get("svg_path", ""),
            output_png=arguments.get("output_png", "output.png"),
            width=int(arguments.get("width", 1920)),
            height=int(arguments.get("height", 1080))
        )
    elif tool_name == "apply_lut":
        return imagemagick_apply_lut(
            input_image=arguments.get("input_image", ""),
            lut_image=arguments.get("lut_image", ""),
            output_image=arguments.get("output_image", "output_graded.png")
        )
    elif tool_name == "export_otio":
        return export_opentimelineio_json(
            clips_data=arguments.get("clips_data", []),
            output_otio=arguments.get("output_otio", "timeline.otio")
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
        print("Uso: python creative_asset_mcp_server.py <tool_name> <json_arguments>")
