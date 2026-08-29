#!/usr/bin/env python3
"""
Antigravity 2.0 - Universal Email Classifier & Forensics Engine
Extracts, sanitizes with Model Armor, and categorizes emails for any Google Workspace account.
"""

import sys
import os
import json
import re
from datetime import datetime, timezone
from collections import Counter, defaultdict
from typing import Dict, Any, List, Optional

# Add current directory to path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from workspace_client import WorkspaceClient, ModelArmorSanitizer

def get_header(headers: List[Dict[str, str]], name: str) -> str:
    for h in headers:
        if h.get("name", "").lower() == name.lower():
            return h.get("value", "")
    return ""

class EmailClassifierEngine:
    def __init__(self, account_alias: str = "nomack3d"):
        self.account_alias = account_alias
        self.client = WorkspaceClient(account_alias)
        self.output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "scratch"))
        os.makedirs(self.output_dir, exist_ok=True)

    def fetch_and_sanitize_emails(self, max_results: int = 100) -> Dict[str, Any]:
        print(f"==> [{self.account_alias}] Extrayendo los {max_results} correos más recientes...")
        res = self.client.list_gmail_messages(max_results=max_results)
        messages = res.get("messages", [])
        print(f"  [+] {len(messages)} IDs de mensajes encontrados.")

        email_data = []
        suspicious_reports = []

        for idx, msg_meta in enumerate(messages, 1):
            msg_id = msg_meta.get("id")
            try:
                detail = self.client.get_message_detail(msg_id)
                payload = detail.get("payload", {})
                headers = payload.get("headers", [])

                subject = get_header(headers, "Subject")
                from_hdr = get_header(headers, "From")
                to_hdr = get_header(headers, "To")
                date_hdr = get_header(headers, "Date")
                snippet = detail.get("snippet", "")
                label_ids = detail.get("labelIds", [])
                internal_date_ms = int(detail.get("internalDate", "0"))
                date_iso = datetime.fromtimestamp(internal_date_ms / 1000.0, timezone.utc).strftime('%Y-%m-%d %H:%M:%S') if internal_date_ms else date_hdr

                # Model Armor Sanitization
                sanitized_subject, sub_findings = ModelArmorSanitizer.scan_and_sanitize(subject, f"Email {msg_id} Subject")
                sanitized_snippet, snip_findings = ModelArmorSanitizer.scan_and_sanitize(snippet, f"Email {msg_id} Snippet")

                if sub_findings or snip_findings:
                    suspicious_reports.extend(sub_findings + snip_findings)

                email_data.append({
                    "index": idx,
                    "id": msg_id,
                    "threadId": detail.get("threadId"),
                    "date": date_iso,
                    "from": from_hdr,
                    "to": to_hdr,
                    "subject": sanitized_subject,
                    "snippet": sanitized_snippet,
                    "labelIds": label_ids
                })

                if idx % 25 == 0 or idx == len(messages):
                    print(f"    -> Procesados {idx}/{len(messages)} correos...")
            except Exception as e:
                print(f"    [ERROR] No se pudo procesar correo {msg_id}: {e}")

        raw_output_path = os.path.join(self.output_dir, f"analyzed_{len(email_data)}_emails_{self.account_alias}.json")
        result = {
            "account": self.account_alias,
            "total_emails": len(email_data),
            "suspicious_findings": suspicious_reports,
            "emails": email_data
        }
        with open(raw_output_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        print(f"  [OK] Extracción guardada en: {raw_output_path}")
        return result

    def categorize_emails(self, email_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        print(f"\n==> [{self.account_alias}] Clasificando {len(email_data)} correos según taxonomía Google Workspace...")
        categorized = []

        for e in email_data:
            sender = e.get("from", "")
            subject = e.get("subject", "")
            snippet = e.get("snippet", "")
            date = e.get("date", "")
            msg_id = e.get("id", "")

            sender_lower = sender.lower()
            subject_lower = subject.lower()
            snippet_lower = snippet.lower()

            # 1. Educación, Cursos & Capacitación
            if any(x in sender_lower for x in ["udemy", "skills.google", "coursera", "platzi", "edx", "cloudskillsboost", "thebig", "grow up data", "founderz", "udecataluña", "tinkercad", "techtitute", "domestika", "crehana", "cgcookie", "rebelway", "school of motion"]) or any(x in subject_lower for x in ["curso", "aprende", "lecciones", "certificación", "skills boost", "udemy", "diplomado", "big school", "starter kit", "tutorial", "masterclass"]):
                cat = "03_EDUCACION_Y_CERTIFICACIONES"
                if "udemy" in sender_lower or "udemy" in subject_lower:
                    subcat = "Udemy"
                elif "skills.google" in sender_lower or ("google" in sender_lower and "skills" in subject_lower):
                    subcat = "Google_Skills_Boost"
                elif "techtitute" in sender_lower:
                    subcat = "Tech_Global_University"
                elif "domestika" in sender_lower:
                    subcat = "Domestika_Creative"
                elif "cgcookie" in sender_lower:
                    subcat = "CGCookie_Blender"
                elif "rebelway" in sender_lower:
                    subcat = "Rebelway_VFX"
                elif "platzi" in sender_lower:
                    subcat = "Platzi"
                elif "autodesk" in sender_lower or "tinkercad" in sender_lower:
                    subcat = "Autodesk_Tinkercad"
                elif "udecataluña" in sender_lower or "diplomado" in subject_lower:
                    subcat = "UdeCataluna"
                elif "founderz" in sender_lower:
                    subcat = "Founderz"
                elif "thebig" in sender_lower:
                    subcat = "BIG_School"
                elif "grow up" in sender_lower:
                    subcat = "GrowUp_Analytics"
                else:
                    subcat = "Academias_Online"

            # 2. Ofertas de Empleo, Freelance & Reclutamiento
            elif any(x in sender_lower for x in ["computrabajo", "unmejorempleo", "linkedin", "intch", "job", "empleo", "talent", "recluta", "bumeran", "elempleo", "upwork", "fiverr", "freelancer", "toptal", "artstation"]) and any(x in subject_lower or x in snippet_lower or x in sender_lower for x in ["job", "empleo", "vacante", "oportunidad", "candidat", "propuesta", "freelance", "hiring", "hired", "trabajo", "postulac"]):
                cat = "02_OFERTAS_EMPLEO_Y_TALENTO"
                if "computrabajo" in sender_lower:
                    subcat = "CompuTrabajo"
                elif "unmejorempleo" in sender_lower:
                    subcat = "UnMejorEmpleo"
                elif "linkedin" in sender_lower:
                    subcat = "LinkedIn_Jobs"
                elif "upwork" in sender_lower:
                    subcat = "Upwork_Freelance"
                elif "fiverr" in sender_lower:
                    subcat = "Fiverr_Gigs"
                elif "artstation" in sender_lower:
                    subcat = "ArtStation_Jobs"
                elif "intch" in sender_lower:
                    subcat = "Intch_Networking"
                else:
                    subcat = "Bolsas_Empleo"

            # 3. Clientes, Entidades Corporativas & Servicios Institucionales
            elif any(x in sender_lower for x in ["ccb.org.co", "scrd.gov.co", "famisanar", "niilo.co", "bbi.com.co", "genesislegal", "notaria", "cliente", "colombiatech", "colombia tech", "mincit", "dian", "alcaldia"]):
                cat = "01_CLIENTES_Y_ENTIDADES"
                if "ccb.org.co" in sender_lower:
                    subcat = "Camara_Comercio_Bogota"
                elif "scrd.gov.co" in sender_lower:
                    subcat = "SCRD_Cultura_Bogota"
                elif "famisanar" in sender_lower:
                    subcat = "Famisanar_EPS"
                elif "niilo" in sender_lower:
                    subcat = "Niilo_Consulting"
                elif "bbi" in sender_lower:
                    subcat = "BBI_Corporativo"
                elif "colombia tech" in sender_lower or "colombiatech" in sender_lower:
                    subcat = "Colombia_Tech_Week"
                else:
                    subcat = "Gestion_Clientes"

            # 4. Tecnología, 3D, IA & Desarrolladores
            elif any(x in sender_lower for x in ["google.com", "openai", "nvidia", "artstation", "medium", "github", "aws", "microsoft", "anthropic", "opencv", "filestack", "rokoko", "woocommerce", "adobe", "dev community", "sketchfab", "blender", "unrealengine", "epicgames", "meshy", "devpost", "lottiefiles", "mermaid", "sidefx", "unity", "chaosgroup", "allegorithmic", "substance"]):
                cat = "04_TECNOLOGIA_IA_Y_DEV"
                if "blender" in sender_lower or "blender" in subject_lower:
                    subcat = "Blender_3D"
                elif "unreal" in sender_lower or "epicgames" in sender_lower:
                    subcat = "Epic_Unreal_Engine"
                elif "sketchfab" in sender_lower:
                    subcat = "Sketchfab_3D"
                elif "sidefx" in sender_lower:
                    subcat = "SideFX_Houdini"
                elif "unity" in sender_lower:
                    subcat = "Unity_3D"
                elif "adobe" in sender_lower or "substance" in sender_lower:
                    subcat = "Adobe_Creative_Cloud"
                elif "openai" in sender_lower:
                    subcat = "OpenAI"
                elif "nvidia" in sender_lower:
                    subcat = "NVIDIA"
                elif "artstation" in sender_lower:
                    subcat = "ArtStation_3D"
                elif "meshy" in sender_lower:
                    subcat = "Meshy_3D_AI"
                elif "devpost" in sender_lower:
                    subcat = "Devpost_Hackathons"
                elif "medium" in sender_lower:
                    subcat = "Medium_Tech_Digest"
                elif "google" in sender_lower:
                    subcat = "Google_Cloud_Ecosystem"
                elif "opencv" in sender_lower:
                    subcat = "OpenCV_Computer_Vision"
                elif "filestack" in sender_lower:
                    subcat = "Filestack_API"
                elif "rokoko" in sender_lower:
                    subcat = "Rokoko_Mocap"
                elif "lottiefiles" in sender_lower:
                    subcat = "LottieFiles_Design"
                elif "mermaid" in sender_lower:
                    subcat = "Mermaid_AI"
                elif "woocommerce" in sender_lower:
                    subcat = "WooCommerce"
                elif "dev" in sender_lower:
                    subcat = "DEV_Community"
                else:
                    subcat = "Plataformas_Tech"

            # 5. Banca, Finanzas, Facturación & Servicios
            elif any(x in sender_lower for x in ["davivienda", "falabella", "banco", "factura", "extracto", "pago", "baloto", "movistar", "recibo", "achcolombia", "nu.com.co", "mis propias finanzas", "addi", "paypal", "payoneer", "stripe"]) or any(x in subject_lower for x in ["extracto", "factura", "pago", "transferencia", "recibo", "cuenta de cobro", "pse", "invoice"]):
                cat = "05_FINANZAS_BANCA_Y_FACTURAS"
                if "davivienda" in sender_lower:
                    subcat = "Davivienda"
                elif "falabella" in sender_lower:
                    subcat = "Banco_Falabella"
                elif "nu.com.co" in sender_lower:
                    subcat = "Nu_Bank"
                elif "paypal" in sender_lower:
                    subcat = "PayPal"
                elif "payoneer" in sender_lower:
                    subcat = "Payoneer"
                elif "stripe" in sender_lower:
                    subcat = "Stripe"
                elif "addi" in sender_lower:
                    subcat = "Addi_Fintech"
                elif "achcolombia" in sender_lower or "pse" in subject_lower:
                    subcat = "PSE_Pasarelas"
                elif "baloto" in sender_lower:
                    subcat = "Baloto_Loterias"
                elif "movistar" in sender_lower:
                    subcat = "Movistar_Servicios"
                elif "mis propias finanzas" in sender_lower:
                    subcat = "Educacion_Financiera"
                else:
                    subcat = "Banca_Facturas"

            # 6. E-Commerce & Retail
            elif any(x in sender_lower for x in ["dafiti", "adidas", "samsung", "sony", "shein", "amazon", "mercadolibre", "aliexpress", "malwarebytes"]):
                cat = "06_ECOMMERCE_Y_RETAIL"
                if "dafiti" in sender_lower:
                    subcat = "Dafiti"
                elif "adidas" in sender_lower:
                    subcat = "Adidas"
                elif "samsung" in sender_lower:
                    subcat = "Samsung"
                elif "sony" in sender_lower:
                    subcat = "Sony"
                elif "shein" in sender_lower:
                    subcat = "Shein"
                elif "amazon" in sender_lower:
                    subcat = "Amazon"
                elif "mercadolibre" in sender_lower:
                    subcat = "MercadoLibre"
                elif "malwarebytes" in sender_lower:
                    subcat = "Malwarebytes_Software"
                else:
                    subcat = "Promociones_Compras"

            # 7. Redes Sociales & Notificaciones Generales
            elif any(x in sender_lower for x in ["facebook", "instagram", "twitter", "x.com", "pinterest", "tiktok", "youtube"]):
                cat = "07_REDES_Y_COMUNIDAD"
                if "instagram" in sender_lower:
                    subcat = "Instagram"
                elif "youtube" in sender_lower:
                    subcat = "YouTube"
                elif "facebook" in sender_lower:
                    subcat = "Facebook"
                elif "twitter" in sender_lower or "x.com" in sender_lower:
                    subcat = "X_Twitter"
                else:
                    subcat = "Social_Media"
            else:
                cat = "04_TECNOLOGIA_IA_Y_DEV"
                subcat = "Plataformas_Tech"

            categorized.append({
                "index": e["index"],
                "id": msg_id,
                "date": date,
                "from": sender,
                "subject": subject,
                "category": cat,
                "subcategory": subcat
            })

        cat_counts = Counter(x["category"] for x in categorized)
        subcat_counts = Counter(f"{x['category']}/{x['subcategory']}" for x in categorized)

        report_file = os.path.join(self.output_dir, f"categorized_{len(categorized)}_emails_{self.account_alias}.json")
        result = {
            "account": self.account_alias,
            "total": len(categorized),
            "summary_by_category": dict(cat_counts),
            "summary_by_subcategory": dict(subcat_counts),
            "items": categorized
        }
        with open(report_file, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        print(f"  [OK] Clasificación guardada en: {report_file}")
        return result

if __name__ == "__main__":
    alias = sys.argv[1] if len(sys.argv) > 1 else "nomack3d"
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    engine = EmailClassifierEngine(alias)
    raw = engine.fetch_and_sanitize_emails(max_results=limit)
    report = engine.categorize_emails(raw["emails"])
