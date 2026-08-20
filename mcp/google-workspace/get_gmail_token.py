#!/usr/bin/env python3
"""
Script de Autenticación OAuth2 para Cuentas Personales (@gmail.com)
Genera el Refresh Token para acceder a Gmail API de nomackleo@gmail.com en Antigravity.
"""

import sys
import os
import json
import urllib.parse
import urllib.request
import webbrowser
from http.server import HTTPServer, BaseHTTPRequestHandler

SCOPES = [
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/documents",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/calendar"
]

auth_code = None

class OAuthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global auth_code
        query_components = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        if "code" in query_components:
            auth_code = query_components["code"][0]
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write("<h1>Autenticacion completada con exito!</h1><p>Puedes cerrar esta ventana y volver a la terminal.</p>".encode("utf-8"))
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write("Error en la autorizacion.".encode("utf-8"))

    def log_message(self, format, *args):
        return

def get_tokens(client_id, client_secret):
    global auth_code
    port = 8080
    redirect_uri = f"http://localhost:{port}/"
    
    params = {
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "response_type": "code",
        "scope": " ".join(SCOPES),
        "access_type": "offline",
        "prompt": "consent"
    }
    
    auth_url = f"https://accounts.google.com/o/oauth2/v2/auth?{urllib.parse.urlencode(params)}"
    print(f"\n[1] Abriendo navegador para autorizar la cuenta nomackleo@gmail.com...")
    print(f"URL: {auth_url}\n")
    webbrowser.open(auth_url)
    
    server = HTTPServer(("localhost", port), OAuthHandler)
    server.handle_request()
    
    if not auth_code:
        print("Error: No se recibio el codigo de autorizacion.")
        sys.exit(1)
        
    print("[2] Canjeando codigo por Refresh Token...")
    token_url = "https://oauth2.googleapis.com/token"
    token_data = urllib.parse.urlencode({
        "client_id": client_id,
        "client_secret": client_secret,
        "code": auth_code,
        "grant_type": "authorization_code",
        "redirect_uri": redirect_uri
    }).encode("utf-8")
    
    req = urllib.request.Request(token_url, data=token_data, headers={"Content-Type": "application/x-www-form-urlencoded"})
    with urllib.request.urlopen(req) as resp:
        tokens = json.loads(resp.read().decode("utf-8"))
        
    print("\n==================================================================")
    print(" TOKEN GENERADO EXITOSAMENTE")
    print("==================================================================")
    print(f"Refresh Token : {tokens.get('refresh_token')}")
    print("==================================================================")
    
    token_file = os.path.expanduser(r"~\.config\antigravity\personal_tokens.json")
    os.makedirs(os.path.dirname(token_file), exist_ok=True)
    with open(token_file, "w", encoding="utf-8") as f:
        json.dump(tokens, f, indent=2)
    print(f"Tokens guardados en: {token_file}\n")
    return tokens

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python get_gmail_token.py <CLIENT_ID> <CLIENT_SECRET>")
        sys.exit(1)
    get_tokens(sys.argv[1], sys.argv[2])
