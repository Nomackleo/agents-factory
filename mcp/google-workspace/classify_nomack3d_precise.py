#!/usr/bin/env python3
"""
Precise 100-email mapping for nomack3d@gmail.com
"""

import os
import json
from collections import Counter, defaultdict

def run_mapping():
    raw_path = os.path.join(os.path.dirname(__file__), "..", "..", "scratch", "analyzed_100_emails_nomack3d.json")
    manifest_path = os.path.join(os.path.dirname(__file__), "labels_manifest_nomack3d.json")
    
    with open(raw_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)
        
    emails = data.get("emails", [])
    mapped = []
    
    for e in emails:
        sender = e.get("from", "")
        subject = e.get("subject", "")
        snippet = e.get("snippet", "")
        date = e.get("date", "")
        msg_id = e.get("id", "")
        
        s_low = sender.lower()
        sub_low = subject.lower()
        snip_low = snippet.lower()
        
        # 1. Clientes y Entidades
        if any(x in s_low for x in ["genesislegal.co", "riesgos@genesislegal", "comercial@genesislegal", "coordinacion@genesislegal"]) or "genesislegal" in sub_low or "génesis legal" in sub_low or "confiabilidad" in sub_low:
            root = "01_CLIENTES_Y_ENTIDADES"
            if "coordinacion" in s_low or "forense" in sub_low:
                child = "Consultoria_Forense"
            else:
                child = "Genesis_Legal"
        elif "mauriciogamboag@gmail.com" in s_low or "mauricio gamboa" in s_low:
            root = "01_CLIENTES_Y_ENTIDADES"
            child = "Mauricio_Gamboa"
        elif "nomack3d@gmail.com" in s_low and ("migración" in sub_low or "migracion" in sub_low or "recordatorio" in sub_low or "respaldo" in sub_low or "estado actual" in sub_low):
            root = "01_CLIENTES_Y_ENTIDADES"
            child = "Proyectos_Leonel"
            
        # 2. Ofertas de Empleo y Talento
        elif "getonbrd.com" in s_low or "get on board" in s_low:
            root = "02_OFERTAS_EMPLEO_Y_TALENTO"
            child = "Get_On_Board"
        elif any(x in s_low for x in ["computrabajo", "linkedin", "unmejorempleo", "upwork", "fiverr"]):
            root = "02_OFERTAS_EMPLEO_Y_TALENTO"
            child = "Portales_Tech"
            
        # 3. Educación y Certificaciones
        elif "britishcouncil" in s_low or "british council" in s_low or "learnenglish" in s_low:
            root = "03_EDUCACION_Y_CERTIFICACIONES"
            child = "British_Council_Ingles"
        elif "skills.google" in s_low or "cloudskillsboost" in s_low:
            root = "03_EDUCACION_Y_CERTIFICACIONES"
            child = "Google_Skills_Boost"
        elif any(x in s_low for x in ["udemy", "platzi", "coursera", "techtitute"]):
            root = "03_EDUCACION_Y_CERTIFICACIONES"
            child = "Academias_Online"
            
        # 4. Tecnología, IA y Dev
        elif "gemini" in s_low or "gemini" in sub_low or "gemini notebook" in s_low or "google ai" in s_low or "googleai" in s_low or "meetings-noreply@google.com" in s_low or "googleone" in s_low or "discuss.ai.google.dev" in s_low or "workspace-noreply@google.com" in s_low:
            root = "04_TECNOLOGIA_IA_Y_DEV"
            child = "Google_Cloud_Gemini"
        elif "github.com" in s_low or "github" in s_low:
            root = "04_TECNOLOGIA_IA_Y_DEV"
            child = "GitHub_OpenSource"
        elif "openai" in s_low or "chatgpt" in s_low:
            root = "04_TECNOLOGIA_IA_Y_DEV"
            child = "OpenAI_ChatGPT"
        elif "nvidia" in s_low:
            root = "04_TECNOLOGIA_IA_Y_DEV"
            child = "NVIDIA_Cosmos_AI"
        elif "warp.dev" in s_low or "warp" in s_low:
            root = "04_TECNOLOGIA_IA_Y_DEV"
            child = "Warp_Terminal_Agent"
        elif "comfy" in s_low or "comfy.org" in s_low:
            root = "04_TECNOLOGIA_IA_Y_DEV"
            child = "ComfyUI_Generative"
        elif "sketchfab" in s_low or "kitbash" in s_low:
            root = "04_TECNOLOGIA_IA_Y_DEV"
            child = "Sketchfab_3D_KitBash"
        elif "napkin.ai" in s_low:
            root = "04_TECNOLOGIA_IA_Y_DEV"
            child = "Napkin_AI"
        elif "voidzero" in s_low or "viteconf" in sub_low:
            root = "04_TECNOLOGIA_IA_Y_DEV"
            child = "Voidzero_ViteConf"
        elif "medium.com" in s_low:
            root = "04_TECNOLOGIA_IA_Y_DEV"
            child = "Medium_Tech_Digest"
            
        # 5. Redes Sociales
        elif "facebook" in s_low or "facebookmail.com" in s_low:
            root = "07_REDES_Y_COMUNIDAD"
            child = "Facebook"
            
        # 6. Sistema y Notificaciones
        elif "mailer-daemon@googlemail.com" in s_low or "delivery status notification" in sub_low:
            root = "08_SISTEMA_Y_NOTIFICACIONES"
            child = "Mailer_Daemon_Bounces"
        elif "accounts.google.com" in s_low or "alerta de seguridad" in sub_low:
            root = "08_SISTEMA_Y_NOTIFICACIONES"
            child = "Alertas_Seguridad_Google"
        else:
            root = "04_TECNOLOGIA_IA_Y_DEV"
            child = "Google_Cloud_Gemini"
            
        mapped.append({
            "index": e.get("index"),
            "id": msg_id,
            "date": date,
            "from": sender,
            "subject": subject,
            "root_label": root,
            "child_label": f"{root}/{child}"
        })
        
    rep_file = os.path.join(os.path.dirname(__file__), "..", "..", "scratch", "categorized_100_emails_nomack3d.json")
    cat_counts = Counter(x["root_label"] for x in mapped)
    subcat_counts = Counter(x["child_label"] for x in mapped)
    
    with open(rep_file, "w", encoding="utf-8") as f:
        json.dump({
            "account": "nomack3d",
            "total": len(mapped),
            "summary_by_category": dict(cat_counts),
            "summary_by_subcategory": dict(subcat_counts),
            "items": mapped
        }, f, indent=2, ensure_ascii=False)
        
    print(f"Mapped {len(mapped)} emails for nomack3d:")
    for c, cnt in cat_counts.most_common():
        print(f"  {c:<35}: {cnt}")
        
    # Generate Matrix Markdown
    out_md = os.path.join(os.path.dirname(__file__), "..", "..", "scratch", "classification_matrix_100_emails_nomack3d.md")
    lines = [
        "# Matriz de Clasificación Forense y Auditoría: 100 Correos de Gmail (nomack3d@gmail.com)",
        "\n**Cuenta Evaluada:** `nomack3d@gmail.com`  ",
        f"**Total Correos Analizados:** {len(mapped)}  ",
        f"**Total Etiquetas Aprovisionadas:** {len(manifest['labels'])}  ",
        "**Estado de Mensajes:** 🔒 **100% INTACTOS (Listo para confirmación HITL y aplicación por lotes)**\n",
        "---\n",
        "## 1. Resumen Ejecutivo por Categoría y Paleta Cromática\n",
        "| Categoría Principal | Etiqueta Raíz | Color UI (Fondo / Texto) | N° Correos | % Distribución |",
        "| :--- | :--- | :---: | :---: | :---: |"
    ]
    
    color_map = {
        "01_CLIENTES_Y_ENTIDADES": ("#16a766", "#ffffff"),
        "02_OFERTAS_EMPLEO_Y_TALENTO": ("#4a86e8", "#ffffff"),
        "03_EDUCACION_Y_CERTIFICACIONES": ("#ffad47", "#000000"),
        "04_TECNOLOGIA_IA_Y_DEV": ("#a479e2", "#ffffff"),
        "05_FINANZAS_BANCA_Y_FACTURAS": ("#43d692", "#000000"),
        "06_ECOMMERCE_Y_RETAIL": ("#fb4c2f", "#ffffff"),
        "07_REDES_Y_COMUNIDAD": ("#4a86e8", "#ffffff"),
        "08_SISTEMA_Y_NOTIFICACIONES": ("#666666", "#ffffff")
    }
    
    for cat, count in cat_counts.most_common():
        bg, text = color_map.get(cat, ("#666666", "#ffffff"))
        lines.append(f"| **{cat}** | `{cat}` | `{bg}` | **{count}** | **{count}%** |")
        
    lines.append("\n---\n")
    lines.append("## 2. Desglose Muestral de los 100 Correos Clasificados\n")
    lines.append("| # | Fecha | Remitente | Asunto | Etiqueta Asignada Propuesta |")
    lines.append("| :-: | :--- | :--- | :--- | :--- |")
    
    for item in mapped:
        subj_clean = item["subject"].replace("|", "-").strip()
        from_clean = item["from"].replace("|", "-").strip()
        lines.append(f"| {item['index']} | {item['date'][:10]} | `{from_clean[:35]}` | {subj_clean[:45]} | `{item['child_label']}` |")
        
    with open(out_md, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
        
    print(f"Matrix report saved to: {out_md}")

if __name__ == "__main__":
    run_mapping()
