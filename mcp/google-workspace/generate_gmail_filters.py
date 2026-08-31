#!/usr/bin/env python3
"""
Antigravity 2.0 - Multi-Tenant Gmail Automated Filter XML Generator
Generates official Gmail Filter XML files (mailFilters.xml) compliant with Google Apps XML Schema.
Supports direct 1-click import into Gmail Web (Settings > Filters and Blocked Addresses > Import filters).
"""

import sys
import os
import json
import time
import xml.etree.ElementTree as ET
from xml.dom import minidom
from typing import Dict, Any, List

FILTER_RULES_BY_ACCOUNT = {
    "nomackleo@gmail.com": [
        {"label": "01_CLIENTES_Y_ENTIDADES/Camara_Comercio_Bogota", "from": "ccb.org.co OR notificaciones@ccb.org.co OR camara de comercio", "shouldNeverSpam": "true"},
        {"label": "01_CLIENTES_Y_ENTIDADES/SCRD_Cultura_Bogota", "from": "scrd.gov.co OR cultura bogota OR convocatorias scrd", "shouldNeverSpam": "true"},
        {"label": "01_CLIENTES_Y_ENTIDADES/Famisanar_EPS", "from": "famisanar.com.co OR eps famisanar", "shouldNeverSpam": "true"},
        {"label": "01_CLIENTES_Y_ENTIDADES/Niilo_Consulting", "from": "niilo.co OR gofest@niilo.co", "shouldNeverSpam": "true"},
        {"label": "01_CLIENTES_Y_ENTIDADES/BBI_Corporativo", "from": "bbi.com.co OR bbi corporativo OR clubtostao@bbi.com.co", "shouldNeverSpam": "true"},
        {"label": "01_CLIENTES_Y_ENTIDADES/Colombia_Tech_Week", "from": "colombiatech OR colombia tech", "shouldNeverSpam": "true"},
        {"label": "01_CLIENTES_Y_ENTIDADES/Proimagenes_Colombia", "from": "proimagenescolombia.com OR pc@proimagenescolombia.com", "shouldNeverSpam": "true"},
        
        {"label": "02_OFERTAS_EMPLEO_Y_TALENTO/CompuTrabajo", "from": "computrabajo.com OR empleo@computrabajo.com", "shouldNeverSpam": "true"},
        {"label": "02_OFERTAS_EMPLEO_Y_TALENTO/LinkedIn_Jobs", "from": "linkedin.com OR jobalerts-noreply@linkedin.com OR messages-noreply@linkedin.com", "shouldNeverSpam": "true"},
        {"label": "02_OFERTAS_EMPLEO_Y_TALENTO/UnMejorEmpleo", "from": "unmejorempleo.co OR candidatos@unmejorempleo.co", "shouldNeverSpam": "true"},
        {"label": "02_OFERTAS_EMPLEO_Y_TALENTO/Intch_Networking", "from": "intch.org OR email.intch.org", "shouldNeverSpam": "true"},
        {"label": "02_OFERTAS_EMPLEO_Y_TALENTO/Get_On_Board", "from": "getonbrd.com OR no-reply@getonbrd.com", "shouldNeverSpam": "true"},
        
        {"label": "03_EDUCACION_Y_CERTIFICACIONES/Udemy", "from": "udemy.com OR e.udemymail.com OR Udemy Instructor", "shouldNeverSpam": "true"},
        {"label": "03_EDUCACION_Y_CERTIFICACIONES/Google_Skills_Boost", "from": "skills.google OR cloudskillsboost.google", "shouldNeverSpam": "true"},
        {"label": "03_EDUCACION_Y_CERTIFICACIONES/Tech_Global_University", "from": "mails.techtitute.com OR techtitute.com", "shouldNeverSpam": "true"},
        {"label": "03_EDUCACION_Y_CERTIFICACIONES/UdeCataluna", "from": "udecataluna.edu.co OR udecataluña", "shouldNeverSpam": "true"},
        {"label": "03_EDUCACION_Y_CERTIFICACIONES/BIG_School", "from": "thebigschool.com OR thebig.com OR big school", "shouldNeverSpam": "true"},
        {"label": "03_EDUCACION_Y_CERTIFICACIONES/Founderz", "from": "founderz.com OR events@founderz.com", "shouldNeverSpam": "true"},
        {"label": "03_EDUCACION_Y_CERTIFICACIONES/GrowUp_Analytics", "from": "growupdataanalytics.com OR grow up data", "shouldNeverSpam": "true"},
        {"label": "03_EDUCACION_Y_CERTIFICACIONES/Autodesk_Tinkercad", "from": "autodesk.com OR tinkercad", "shouldNeverSpam": "true"},
        {"label": "03_EDUCACION_Y_CERTIFICACIONES/Platzi", "from": "platzi.com OR hello.platzi.com", "shouldNeverSpam": "true"},
        {"label": "03_EDUCACION_Y_CERTIFICACIONES/Duolingo", "from": "duolingo.com OR hello@duolingo.com", "shouldNeverSpam": "true"},
        {"label": "03_EDUCACION_Y_CERTIFICACIONES/Coursera", "from": "coursera.org OR m.learn.coursera.org", "shouldNeverSpam": "true"},
        {"label": "03_EDUCACION_Y_CERTIFICACIONES/QuantInsti_Trading", "from": "quantinsti.com", "shouldNeverSpam": "true"},
        
        {"label": "04_TECNOLOGIA_IA_Y_DEV/Google_Cloud_Ecosystem", "from": "google.com OR googleaistudio OR google developer program OR noreply-accounts@google.com", "shouldNeverSpam": "true"},
        {"label": "04_TECNOLOGIA_IA_Y_DEV/OpenAI", "from": "openai.com OR email.openai.com", "shouldNeverSpam": "true"},
        {"label": "04_TECNOLOGIA_IA_Y_DEV/NVIDIA", "from": "nvidia.com OR nvgaming.com", "shouldNeverSpam": "true"},
        {"label": "04_TECNOLOGIA_IA_Y_DEV/ArtStation_3D", "from": "artstation.com OR notifications@artstation.com", "shouldNeverSpam": "true"},
        {"label": "04_TECNOLOGIA_IA_Y_DEV/Meshy_3D_AI", "from": "meshy.ai OR news.meshy.ai", "shouldNeverSpam": "true"},
        {"label": "04_TECNOLOGIA_IA_Y_DEV/Devpost_Hackathons", "from": "devpost.com OR support@devpost.com", "shouldNeverSpam": "true"},
        {"label": "04_TECNOLOGIA_IA_Y_DEV/Medium_Tech_Digest", "from": "medium.com OR noreply@medium.com", "shouldNeverSpam": "true"},
        {"label": "04_TECNOLOGIA_IA_Y_DEV/DEV_Community", "from": "dev.to OR devcommunity.org", "shouldNeverSpam": "true"},
        {"label": "04_TECNOLOGIA_IA_Y_DEV/OpenCV_Computer_Vision", "from": "opencv.org OR newsletter@opencv.org", "shouldNeverSpam": "true"},
        {"label": "04_TECNOLOGIA_IA_Y_DEV/Filestack_API", "from": "filestack.com OR communication@filestack.com", "shouldNeverSpam": "true"},
        {"label": "04_TECNOLOGIA_IA_Y_DEV/Rokoko_Mocap", "from": "rokoko.com OR hi@rokoko.com", "shouldNeverSpam": "true"},
        {"label": "04_TECNOLOGIA_IA_Y_DEV/LottieFiles_Design", "from": "lottiefiles.com OR hello@lottiefiles.com", "shouldNeverSpam": "true"},
        {"label": "04_TECNOLOGIA_IA_Y_DEV/Mermaid_AI", "from": "mermaid.ai OR no-reply@mermaid.ai", "shouldNeverSpam": "true"},
        {"label": "04_TECNOLOGIA_IA_Y_DEV/WooCommerce", "from": "woocommerce.com OR hello@woocommerce.com", "shouldNeverSpam": "true"},
        {"label": "04_TECNOLOGIA_IA_Y_DEV/Adobe_Creative_Cloud", "from": "adobe.com OR mail@mail.adobe.com", "shouldNeverSpam": "true"},
        {"label": "04_TECNOLOGIA_IA_Y_DEV/Voidzero_ViteConf", "from": "voidzero.dev OR no-reply@voidzero.dev", "shouldNeverSpam": "true"},
        {"label": "04_TECNOLOGIA_IA_Y_DEV/AnyDesk_Software", "from": "anydesk.com OR noreply@anydesk.com", "shouldNeverSpam": "true"},
        {"label": "04_TECNOLOGIA_IA_Y_DEV/Raiola_Networks", "from": "raiolanetworks.es OR marketing@raiolanetworks.es", "shouldNeverSpam": "true"},
        
        {"label": "05_FINANZAS_BANCA_Y_FACTURAS/Davivienda", "from": "davivienda.com OR BANCO_DAVIVIENDA@davivienda.com", "shouldNeverSpam": "true"},
        {"label": "05_FINANZAS_BANCA_Y_FACTURAS/Banco_Falabella", "from": "bancofalabella.com OR co.bancofalabella.com", "shouldNeverSpam": "true"},
        {"label": "05_FINANZAS_BANCA_Y_FACTURAS/Nu_Bank", "from": "nu.com.co OR nu@nu.com.co OR soynu.com.co", "shouldNeverSpam": "true"},
        {"label": "05_FINANZAS_BANCA_Y_FACTURAS/Addi_Fintech", "from": "addi.com OR ofertas.addi.com", "shouldNeverSpam": "true"},
        {"label": "05_FINANZAS_BANCA_Y_FACTURAS/PSE_Pasarelas", "from": "achcolombia.com.co OR serviciopse@achcolombia.com.co OR epayco.com", "shouldNeverSpam": "true"},
        {"label": "05_FINANZAS_BANCA_Y_FACTURAS/Facturacion_Electronica", "from": "dataico.com OR noreply@dataico.com", "shouldNeverSpam": "true"},
        {"label": "05_FINANZAS_BANCA_Y_FACTURAS/Baloto_Loterias", "from": "baloto.com OR servicioalcliente@baloto.com", "shouldNeverSpam": "true"},
        {"label": "05_FINANZAS_BANCA_Y_FACTURAS/Movistar_Servicios", "from": "movistar.co OR mailc.movistar.co", "shouldNeverSpam": "true"},
        {"label": "05_FINANZAS_BANCA_Y_FACTURAS/Educacion_Financiera", "from": "mispropiasfinanzas.com OR info@mispropiasfinanzas.com", "shouldNeverSpam": "true"},
        
        {"label": "06_ECOMMERCE_Y_RETAIL/Dafiti", "from": "dafiti.com.co OR news.email.dafiti.com.co", "shouldNeverSpam": "true"},
        {"label": "06_ECOMMERCE_Y_RETAIL/Adidas", "from": "adidas.com OR co-news.adidas.com", "shouldNeverSpam": "true"},
        {"label": "06_ECOMMERCE_Y_RETAIL/Samsung", "from": "samsung.com OR co.email.samsung.com", "shouldNeverSpam": "true"},
        {"label": "06_ECOMMERCE_Y_RETAIL/Sony", "from": "sony-latin.com OR co.emailmkt.sony-latin.com", "shouldNeverSpam": "true"},
        {"label": "06_ECOMMERCE_Y_RETAIL/Shein", "from": "shein.com OR news.shein.com", "shouldNeverSpam": "true"},
        {"label": "06_ECOMMERCE_Y_RETAIL/Malwarebytes_Software", "from": "malwarebytes.com OR e.malwarebytes.com", "shouldNeverSpam": "true"}
    ],
    "nomack3d@gmail.com": [
        {"label": "01_CLIENTES_Y_ENTIDADES/Genesis_Legal", "from": "genesislegal.co OR comercial@genesislegal.co OR riesgos@genesislegal.co OR coordinacion@genesislegal.co OR admin@genesislegal.co", "shouldNeverSpam": "true"},
        {"label": "01_CLIENTES_Y_ENTIDADES/Consultoria_Forense", "from": "coordinacion@genesislegal.co OR forense", "shouldNeverSpam": "true"},
        {"label": "01_CLIENTES_Y_ENTIDADES/Mauricio_Gamboa", "from": "mauriciogamboag@gmail.com", "shouldNeverSpam": "true"},
        {"label": "01_CLIENTES_Y_ENTIDADES/Proyectos_Leonel", "from": "nomack3d@gmail.com", "shouldNeverSpam": "true"},
        {"label": "02_OFERTAS_EMPLEO_Y_TALENTO/Get_On_Board", "from": "getonbrd.com OR no-reply@getonbrd.com", "shouldNeverSpam": "true"},
        {"label": "03_EDUCACION_Y_CERTIFICACIONES/British_Council_Ingles", "from": "britishcouncil.org OR learnenglish@britishcouncil.org", "shouldNeverSpam": "true"},
        {"label": "04_TECNOLOGIA_IA_Y_DEV/Google_Cloud_Gemini", "from": "google.com OR gemini-notes@google.com OR notifications@discuss.ai.google.dev OR workspace-noreply@google.com OR googleone-noreply@google.com", "shouldNeverSpam": "true"},
        {"label": "04_TECNOLOGIA_IA_Y_DEV/GitHub_OpenSource", "from": "github.com OR notifications@github.com", "shouldNeverSpam": "true"},
        {"label": "04_TECNOLOGIA_IA_Y_DEV/OpenAI_ChatGPT", "from": "openai.com OR email.openai.com", "shouldNeverSpam": "true"},
        {"label": "04_TECNOLOGIA_IA_Y_DEV/NVIDIA_Cosmos_AI", "from": "nvidia.com OR news@nvidia.com OR inceptionprogram@nvidia.com", "shouldNeverSpam": "true"},
        {"label": "04_TECNOLOGIA_IA_Y_DEV/Warp_Terminal_Agent", "from": "warp.dev OR feedback+customerio@warp.dev", "shouldNeverSpam": "true"},
        {"label": "04_TECNOLOGIA_IA_Y_DEV/ComfyUI_Generative", "from": "comfy.org OR news.comfy.org", "shouldNeverSpam": "true"},
        {"label": "04_TECNOLOGIA_IA_Y_DEV/Sketchfab_3D_KitBash", "from": "sketchfab.com OR community@sketchfab.com", "shouldNeverSpam": "true"},
        {"label": "04_TECNOLOGIA_IA_Y_DEV/Napkin_AI", "from": "napkin.ai OR contact@napkin.ai", "shouldNeverSpam": "true"},
        {"label": "04_TECNOLOGIA_IA_Y_DEV/Voidzero_ViteConf", "from": "voidzero.dev", "shouldNeverSpam": "true"},
        {"label": "04_TECNOLOGIA_IA_Y_DEV/Medium_Tech_Digest", "from": "medium.com OR noreply@medium.com", "shouldNeverSpam": "true"},
        {"label": "07_REDES_Y_COMUNIDAD/Facebook", "from": "facebookmail.com OR reminders@facebookmail.com OR friendsuggestions@facebookmail.com", "shouldNeverSpam": "true"},
        {"label": "08_SISTEMA_Y_NOTIFICACIONES/Mailer_Daemon_Bounces", "from": "mailer-daemon@googlemail.com", "shouldNeverSpam": "true"},
        {"label": "08_SISTEMA_Y_NOTIFICACIONES/Alertas_Seguridad_Google", "from": "no-reply@accounts.google.com", "shouldNeverSpam": "true"}
    ]
}

def generate_filters_xml(account_email: str = "nomackleo@gmail.com") -> str:
    print(f"\n==> Generando paquete de filtros XML para: {account_email}...")
    alias = "nomack3d" if "nomack3d" in account_email else "nomackleo"
    rules = FILTER_RULES_BY_ACCOUNT.get(account_email, FILTER_RULES_BY_ACCOUNT.get("nomackleo@gmail.com", []))

    timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    feed = ET.Element("feed", {
        "xmlns": "http://www.w3.org/2005/Atom",
        "xmlns:apps": "http://schemas.google.com/apps/2006"
    })

    title = ET.SubElement(feed, "title")
    title.text = f"Mail Filters for {account_email}"

    id_elem = ET.SubElement(feed, "id")
    id_elem.text = f"tag:mail.google.com,2008:filters:{account_email}"

    upd_elem = ET.SubElement(feed, "updated")
    upd_elem.text = timestamp

    for idx, rule in enumerate(rules, 1):
        entry = ET.SubElement(feed, "entry")
        ET.SubElement(entry, "category", {"term": "filter"})
        t = ET.SubElement(entry, "title")
        t.text = f"Mail Filter {idx}: {rule['label']}"
        e_id = ET.SubElement(entry, "id")
        e_id.text = f"tag:mail.google.com,2008:filter:{idx}"
        e_upd = ET.SubElement(entry, "updated")
        e_upd.text = timestamp
        ET.SubElement(entry, "content")

        if "from" in rule:
            ET.SubElement(entry, "apps:property", {"name": "from", "value": rule["from"]})
        if "hasTheWord" in rule:
            ET.SubElement(entry, "apps:property", {"name": "hasTheWord", "value": rule["hasTheWord"]})

        if "label" in rule:
            ET.SubElement(entry, "apps:property", {"name": "label", "value": rule["label"]})
        if rule.get("shouldNeverSpam") == "true":
            ET.SubElement(entry, "apps:property", {"name": "shouldNeverSpam", "value": "true"})

    xml_str = ET.tostring(feed, encoding="utf-8")
    parsed = minidom.parseString(xml_str)
    pretty_xml = parsed.toprettyxml(indent="  ", encoding="utf-8").decode("utf-8")

    out_name = "gmail_filters_import.xml" if alias == "nomackleo" else f"gmail_filters_{alias}.xml"
    output_xml = os.path.join(os.path.dirname(__file__), out_name)
    with open(output_xml, "w", encoding="utf-8") as f:
        f.write(pretty_xml)

    print(f"\n==================================================================")
    print(f" [ÉXITO] ARCHIVO DE FILTROS GMAIL GENERADO: {len(rules)} REGLAS")
    print(f" Cuenta: {account_email}")
    print(f" Ruta  : {output_xml}")
    print("==================================================================\n")
    return output_xml

if __name__ == "__main__":
    email = sys.argv[1] if len(sys.argv) > 1 else "nomackleo@gmail.com"
    generate_filters_xml(email)
