#!/usr/bin/env python3
"""
Gemini Audio API & WebAudio Spatial Engine Manifest Generator
Part of Antigravity Agent Factory (Obra Homenaje a la Madre de Leonel - 12 de Marzo)

Generates audio prompts for Gemini Audio API / MusicFX to produce 4 stems
and maps them to WebAudio API spatial audio nodes (Panner3D / BiquadFilter).
"""

import os
import json
import argparse
from typing import Dict, Any

def generate_audio_stems_manifest() -> Dict[str, Any]:
    manifest = {
        "project": "In Memoriam - Homenaje a la Madre de Leonel (12 de Marzo)",
        "module": "Gemini Audio Engine & WebAudio Spatialization",
        "sample_rate": 48000,
        "bit_depth": 24,
        "format": "FLAC / WebM Audio",
        "stems": [
            {
                "id": "stem_1_piano",
                "act": "Act I - El Silencio y el Recuerdo",
                "gemini_prompt": (
                    "Deep ambient piano note at 55Hz, single strike, long cathedral decay "
                    "reverb 8 seconds, quiet, minimalist, impressionist, high dynamic range, 24-bit 48kHz audio."
                ),
                "duration_seconds": 8.0,
                "webaudio_nodes": {
                    "panner": "StereoPannerNode(0.0)",
                    "filter": "BiquadFilterNode('lowpass', 450Hz)",
                    "gain": 0.85
                }
            },
            {
                "id": "stem_2_water",
                "act": "Act II - El Lago de la Inmensidad",
                "gemini_prompt": (
                    "Subtle liquid water ripples, organic sumi-e paper wash sound, binaural stereo, "
                    "soft flowing water, serene, meditative, no harsh frequencies."
                ),
                "duration_seconds": 25.0,
                "webaudio_nodes": {
                    "panner": "Panner3D(0.0, -1.0, -2.0)",
                    "filter": "BiquadFilterNode('lowpass', 1200Hz)",
                    "gain": 0.60
                }
            },
            {
                "id": "stem_3_murmuration",
                "act": "Act III - La Murmuración en Plano 2.5D",
                "gemini_prompt": (
                    "Soft wind rustle mixed with distant flock murmuration fluttering sound, "
                    "stochastic natural cadence, spatial audio panning left to right, delicate ambient."
                ),
                "duration_seconds": 45.0,
                "webaudio_nodes": {
                    "panner": "Panner3D(x_dynamic, y_dynamic, z_dynamic)",
                    "filter": "BiquadFilterNode('bandpass', 800Hz)",
                    "gain": 0.70
                }
            },
            {
                "id": "stem_4_climax_floral",
                "act": "Act IV - El Florecer en la Penumbra (3 Clicks)",
                "gemini_prompt": (
                    "Harmonic cello crescendo chord in A minor transitioning to crystal singing bowls, "
                    "bioluminescent glow sound effect, warm, uplifting, eternal memory homage, pristine clarity."
                ),
                "duration_seconds": 15.0,
                "webaudio_nodes": {
                    "panner": "StereoPannerNode(0.0)",
                    "filter": "BiquadFilterNode('highpass', 200Hz)",
                    "gain": 1.0
                }
            }
        ]
    }
    return manifest

def main():
    parser = argparse.ArgumentParser(description="Gemini Audio API Generator")
    parser.add_argument("--output", type=str, default="projects/homenaje-madre/assets/audio_stems_manifest.json", help="Output path")
    args = parser.parse_args()

    manifest = generate_audio_stems_manifest()
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    xml_report = f"""<hitl_approval_request>
  <task_name>Gemini Audio API Stems & WebAudio Spatialization Manifest</task_name>
  <requester>Gemini Audio Engine Subagent</requester>
  <approver>Leonel Salcedo (HITL Mandatory Gate)</approver>
  <payload_summary>
{json.dumps(manifest, indent=4)}
  </payload_summary>
  <status>WAITING_FOR_LEONEL_REVIEW</status>
</hitl_approval_request>"""

    print(xml_report)

if __name__ == "__main__":
    main()
