"""
Prompt-to-Prompt & Multimodal JSON Prompt Compiler
Autor: Leonel Salcedo / Nomack Studio & Antigravity

Traduce descriptores estructurados JSON en prompts de difusión optimizados y controladores de atención cruzada.
"""

import json
from typing import Dict, Any, List, Tuple

class MultimodalPromptCompiler:
    """
    Compila especificaciones JSON estructuradas en prompts sintácticos de alta fidelidad
    para Nano Banana, Omni, Imagen, Midjourney y Stable Diffusion / Flux.
    """
    
    @staticmethod
    def compile_json_to_prompt(schema_data: Dict[str, Any]) -> str:
        parts = []
        
        # 1. Sujeto Principal
        subj = schema_data.get("subject", {})
        main_entity = subj.get("main_entity", "")
        action = subj.get("action_or_state", "")
        details = subj.get("details", "")
        parts.append(f"{main_entity}, {action}, {details}")
        
        # 2. Composición y Encuadre
        comp = schema_data.get("composition", {})
        shot = comp.get("shot_type", "")
        angle = comp.get("camera_angle", "")
        framing = comp.get("framing_rule", "")
        parts.append(f"{shot}, {angle}, composed with {framing}")
        
        # 3. Óptica y Cámara
        optics = schema_data.get("optics", {})
        focal = optics.get("focal_length", "")
        aperture = optics.get("aperture", "")
        dof = optics.get("depth_of_field", "")
        lens_fx = optics.get("lens_effects", "")
        parts.append(f"shot on {focal}, {aperture}, {dof}, {lens_fx}")
        
        # 4. Iluminación y Atmósfera
        light = schema_data.get("lighting", {})
        setup = light.get("setup_type", "")
        direction = light.get("key_light_direction", "")
        temp = light.get("color_temperature", "")
        atmos = light.get("atmosphere", "")
        parts.append(f"{setup}, key light from {direction}, {temp}, {atmos}")
        
        # 5. Paleta y Color Grading
        color = schema_data.get("color_palette", {})
        primary = ", ".join(color.get("primary_tones", []))
        accents = ", ".join(color.get("accent_tones", []))
        lut = color.get("grading_lut", "")
        parts.append(f"color palette featuring {primary} with {accents} accents, {lut} color grading")
        
        # 6. Dinámicas VFX / Movimiento
        vfx = schema_data.get("vfx_and_dynamics", {})
        if vfx:
            particles = vfx.get("particles", "")
            motion = vfx.get("motion_dynamics", "")
            cam_motion = vfx.get("camera_motion_for_video", "")
            vfx_tokens = [t for t in [particles, motion, cam_motion] if t]
            if vfx_tokens:
                parts.append(", ".join(vfx_tokens))
                
        # 7. Estilo y Motor
        style = schema_data.get("style", {})
        genre = style.get("genre", "")
        engine = style.get("render_engine_or_medium", "")
        bench = style.get("aesthetic_benchmark", "")
        parts.append(f"{genre}, rendered in {engine}, inspired by {bench}, 8k resolution, award winning cinematography")
        
        # Unir tokens limpiando comas redundantes
        full_prompt = ", ".join([p.strip().rstrip(",") for p in parts if p.strip()])
        return full_prompt

    @staticmethod
    def generate_word_swap_pairs(original_prompt: str, swap_dict: Dict[str, str]) -> Tuple[str, str]:
        """
        Genera el prompt fuente y el prompt destino para Cross-Attention Swap
        """
        target_prompt = original_prompt
        for src_word, tgt_word in swap_dict.items():
            target_prompt = target_prompt.replace(src_word, tgt_word)
        return original_prompt, target_prompt

if __name__ == "__main__":
    sample_spec = {
        "subject": {
            "main_entity": "3D PBR marble material sphere",
            "action_or_state": "hovering against dark background",
            "details": "micro veins, polished sheen"
        },
        "composition": {
            "shot_type": "macro-detail",
            "camera_angle": "eye-level",
            "framing_rule": "central-symmetry"
        },
        "optics": {
            "focal_length": "100mm macro lens",
            "aperture": "f/2.8",
            "depth_of_field": "shallow depth of field",
            "lens_effects": "clean optical glass"
        },
        "lighting": {
            "setup_type": "3-point studio lighting",
            "key_light_direction": "45-degree top-right",
            "color_temperature": "5600K clean white",
            "atmosphere": "crisp air"
        },
        "color_palette": {
            "primary_tones": ["#F8FAFC", "#0F172A"],
            "accent_tones": ["#C5A880"],
            "grading_lut": "Neutral Studio Standard"
        },
        "style": {
            "genre": "PBR 3D Texture Map",
            "render_engine_or_medium": "Octane Redshift 3D render",
            "aesthetic_benchmark": "Substance 3D Designer benchmark"
        }
    }
    
    compiled = MultimodalPromptCompiler.compile_json_to_prompt(sample_spec)
    print(f"[Compilador Prompt Multimodal]\n{compiled}")
