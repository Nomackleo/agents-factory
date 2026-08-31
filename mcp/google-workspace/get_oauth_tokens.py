#!/usr/bin/env python3
"""
Antigravity 2.0 - Multi-Account OAuth2 Token Generator
Genera tokens de acceso y Refresh Tokens para cuentas personales (@gmail.com).
Soporta cuentas múltiples: nomackleo, nomack3d, etc.
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
    "https://www.googleapis.com/auth/presentations",
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/chat.spaces",
    "https://www.googleapis.com/auth/contacts"
]

auth_code = None

class OAuthCallbackHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global auth_code
        query = urllib.parse.urlparse(self.path).query
        query_components = urllib.parse.parse_qs(query)
        if "code" in query_components:
            auth_code = query_components["code"][0]
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            html = """
            <html>
            <body style="font-family: Arial, sans-serif; text-align: center; padding: 50px; background-color: #0b132b; color: #ffffff;">
                <h1 style="color: #4ade80;">✔ Autenticación Exitosa con Antigravity</h1>
                <p>El token ha sido capturado correctamente.</p>
                <p style="color: #94a3b8;">Puedes cerrar esta pestaña y volver a la terminal.</p>
            </body>
            </html>
            """
            self.wfile.write(html.encode("utf-8"))
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write("Error en la autorización de Google.".encode("utf-8"))

    def log_message(self, format, *args):
        return

def generate_account_token(account_alias, client_id, client_secret):
    global auth_code
    auth_code = None
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
    print(f"\n==================================================================")
    print(f" AUTENTICACIÓN GOOGLE WORKSPACE / GMAIL: [{account_alias}]")
    print(f"==================================================================")
    print(f"Abriendo el navegador para autorizar la cuenta...\nURL: {auth_url}\n")
    webbrowser.open(auth_url)
    
    server = HTTPServer(("localhost", port), OAuthCallbackHandler)
    server.handle_request()
    
    if not auth_code:
        print("[ERROR] No se recibió el código de autorización.")
        sys.exit(1)
        
    print("[+] Canjeando código por Refresh Token en Google OAuth2...")
    token_url = "https://oauth2.googleapis.com/token"
    token_data = urllib.parse.urlencode({
        "client_id": client_id,
        "client_secret": client_secret,
        "code": auth_code,
        "grant_type": "authorization_code",
        "redirect_uri": redirect_uri
    }).encode("utf-8")
    
    req = urllib.request.Request(
        token_url,
        data=token_data,
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    
    with urllib.request.urlopen(req) as resp:
        tokens = json.loads(resp.read().decode("utf-8"))
        
    refresh_token = tokens.get("refresh_token")
    if not refresh_token:
        print("[WARNING] Google no devolvió un refresh_token nuevo. Si ya habías autorizado antes, revoca el acceso en myaccount.google.com/permissions o pasa prompt=consent.")
        
    token_dir = os.path.expanduser(r"~\.config\antigravity")
    os.makedirs(token_dir, exist_ok=True)
    token_file = os.path.join(token_dir, f"tokens_{account_alias}.json")
    
    with open(token_file, "w", encoding="utf-8") as f:
        json.dump(tokens, f, indent=2)
        
    print("\n==================================================================")
    print(f" [ÉXITO] TOKENS GUARDADOS PARA: {account_alias}")
    print("==================================================================")
    print(f"Archivo de Tokens: {token_file}")
    if refresh_token:
        print(f"Refresh Token    : {refresh_token[:15]}... (Oculto)")
    print("==================================================================\n")
    return tokens

if __name__ == "__main__":
    account_alias = sys.argv[1] if len(sys.argv) > 1 else "nomackleo"
    client_id = sys.argv[2] if len(sys.argv) > 2 else ""
    client_secret = sys.argv[3] if len(sys.argv) > 3 else ""

    if not client_id or not client_secret:
        cred_path = os.path.expanduser(r"~\.config\antigravity\oauth_credentials.json")
        if os.path.exists(cred_path):
            with open(cred_path, "r", encoding="utf-8") as f:
                creds = json.load(f)
                client_id = client_id or creds.get("client_id")
                client_secret = client_secret or creds.get("client_secret")

    if not client_id or not client_secret:
        print("Uso: python get_oauth_tokens.py <ACCOUNT_ALIAS> [CLIENT_ID] [CLIENT_SECRET]")
        print("Ejemplo: python get_oauth_tokens.py nomackleo")
        sys.exit(1)

    generate_account_token(account_alias, client_id, client_secret)
