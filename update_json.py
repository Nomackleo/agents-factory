import json

with open("pptx.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Add Google Meet and Calendar info to Slide 5 (or create a new slide)
new_slide = {
    "slide_number": 5.5,
    "abstract_layout": "split-2-column",
    "elements": [
        {
            "type": "title",
            "text": "FLUJO DE COMUNICACIÓN Y PRODUCTIVIDAD AVANZADA",
            "style_overrides": {
                "font_size": 36,
                "color": "#07283d"
            }
        },
        {
            "type": "subtitle",
            "text": "Google Meet y Calendars Pro en el Ecosistema Legal",
            "style_overrides": {
                "font_size": 20,
                "color": "#1a1a1a"
            }
        },
        {
            "type": "column_left",
            "text": "GOOGLE MEET: DEPOSICIONES SEGURAS\nTransición a un entorno de videoconferencias con cifrado de extremo a extremo y controles de acceso estrictos para audiencias legales y poligrafía.",
            "style_overrides": {
                "background_color": "#cccccc"
            }
        },
        {
            "type": "column_right",
            "text": "CALENDARS PRO\nGestión centralizada de recursos forenses (salas de poligrafía, laboratorios). Agendamiento inteligente y visibilidad interdepartamental controlada bajo estrictas normativas de privacidad.",
            "style_overrides": {
                "background_color": "#07283d",
                "color": "#ffffff"
            }
        }
    ],
    "speaker_notes": "Además de la gestión documental, la agilidad en los pipelines de Génesis requiere comunicaciones infalibles. Con Google Meet garantizamos que las deposiciones virtuales y entrevistas forenses estén protegidas por controles de acceso avanzados. Calendars Pro nos permite gestionar la disponibilidad de las salas de poligrafía como recursos corporativos, optimizando la productividad y el despliegue del personal sin exponer información confidencial."
}

# Update Slide 4 to include Automated Traffic Notification and Advanced Gmail Security
for s in data["slides"]:
    if s["slide_number"] == 4:
        s["elements"].insert(5, {
            "type": "table_row",
            "text": "Acceso y Tráfico | Automated Traffic Notification | Restricciones de acceso y alertas ante tráfico inusual, garantizando la seguridad en endpoints.",
            "style_overrides": {}
        })
        s["elements"].insert(6, {
            "type": "table_row",
            "text": "Seguridad Correo | Advanced Gmail Security | Configuración estricta de protocolos anti-phishing, spoofing y retención corporativa.",
            "style_overrides": {}
        })
        s["speaker_notes"] += " Sumamos a esto la Guía Avanzada de Seguridad de Gmail y las Restricciones de Acceso Automatizado, que bloquean intentos de acceso anómalos, asegurando que solo el personal autorizado de Génesis ingrese a la red, cumpliendo a cabalidad con los Términos de Servicio Empresariales de Google Workspace."

# Update Slide 10 to emphasize Purge Mechanisms
for s in data["slides"]:
    if s["slide_number"] == 10:
        s["elements"][2]["text"] = s["elements"][2]["text"].replace(
            "0001 RETENCIÓN INMUTABLE (HOLDS LEGALES): Conservación irreversible de correos, chats y archivos para auditorías judiciales.",
            "0001 RETENCIÓN Y PURGA ESTRATÉGICA (HOLDS): Conservación irreversible y mecanismos de purga programada (Data Retention and Purge Mechanisms) para cumplimiento legal."
        )

# Fix numbering
slides = data["slides"]
slides.insert(5, new_slide)
for i, s in enumerate(slides):
    s["slide_number"] = i + 1

with open("pptx_updated.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
