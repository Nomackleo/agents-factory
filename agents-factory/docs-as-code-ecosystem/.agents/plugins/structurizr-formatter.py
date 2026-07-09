#!/usr/bin/env python3
"""
Structurizr DSL & Mermaid Formatter Plugin
Este script asiste en la conversión y formateo de definiciones de arquitectura 
levantadas por los agentes para asegurar que cumplan con la sintaxis estricta 
del Modelo C4 en formato Structurizr o diagramas Mermaid.
"""
import sys

def format_to_c4_mermaid(components_dict):
    """
    Toma un diccionario básico de componentes y retorna un string en formato C4 Mermaid.
    """
    mermaid_str = "C4Context\n"
    mermaid_str += "  title System Context diagram for Architecture\n\n"
    
    for key, val in components_dict.items():
        if val.get('type') == 'Person':
            mermaid_str += f"  Person({key}, \"{val.get('label')}\", \"{val.get('desc')}\")\n"
        elif val.get('type') == 'System':
            mermaid_str += f"  System({key}, \"{val.get('label')}\", \"{val.get('desc')}\")\n"
            
    mermaid_str += "\n"
    for key, val in components_dict.items():
        if 'relates_to' in val:
            for rel in val['relates_to']:
                mermaid_str += f"  Rel({key}, {rel['target']}, \"{rel['desc']}\")\n"
                
    return mermaid_str

if __name__ == "__main__":
    print("Plugin Structurizr/Mermaid Formatter inicializado.")
    # Implementación CLI a demanda
