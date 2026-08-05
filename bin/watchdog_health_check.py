#!/usr/bin/env python3
"""
Watchdog & Health Check for Génesis Legal Workspace
Audits & self-heals Google Drive MCP tokens and NotebookLM CLI session.
"""

import json
import os
import subprocess
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone

# Ensure UTF-8 output encoding for Windows terminal compatibility
sys.stdout.reconfigure(encoding='utf-8')

TOKENS_PATH = r"C:\Users\Nomack\.gemini\antigravity-ide\mcp_oauth_tokens.json"
NLM_EXE = r"C:\Users\Nomack\.local\bin\nlm.exe"

def check_and_heal_google_drive():
    print("[Watchdog] Verificando estado de conexión a Google Drive API...")
    if not os.path.exists(TOKENS_PATH):
        print("[Watchdog ERROR] No se encontró el archivo de tokens mcp_oauth_tokens.json")
        return False

    try:
        data = json.load(open(TOKENS_PATH, "r", encoding="utf-8"))
    except Exception as e:
        print(f"[Watchdog ERROR] Error al leer mcp_oauth_tokens.json: {e}")
        return False

    drive_entry = data.get("https://drivemcp.googleapis.com/mcp/v1", {})
    token_info = drive_entry.get("token", {})
    access_token = token_info.get("access_token")
    refresh_token = token_info.get("refresh_token")
    client_id = drive_entry.get("client_id")
    client_secret = drive_entry.get("client_secret")

    if not access_token or not refresh_token:
        print("[Watchdog ERROR] Falta el token de acceso o refresh token en la configuración.")
        return False

    # Probar token actual con llamado directo a Drive API v3
    req = urllib.request.Request(
        "https://www.googleapis.com/drive/v3/files?pageSize=1",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    
    try:
        with urllib.request.urlopen(req) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            print("[Watchdog OK] Conexión a Google Drive API: 100% OPERATIVA Y VERIFICADA.")
            return True
    except urllib.error.HTTPError as e:
        if e.code == 401 or e.code == 403:
            print("[Watchdog WARN] Token expirado o no autorizado. Iniciando Auto-Healing (Refresh Token)...")
            return refresh_google_drive_token(data, refresh_token, client_id, client_secret)
        else:
            print(f"[Watchdog ERROR] Error en Google Drive API: {e.code} {e.reason}")
            return False

def refresh_google_drive_token(data, refresh_token, client_id, client_secret):
    url = "https://oauth2.googleapis.com/token"
    payload = urllib.parse.urlencode({
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": refresh_token,
        "grant_type": "refresh_token"
    }).encode("utf-8")

    req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/x-www-form-urlencoded"})

    try:
        with urllib.request.urlopen(req) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            new_access_token = res["access_token"]
            expires_in = res.get("expires_in", 3600)
            
            # Actualizar datos de token
            data["https://drivemcp.googleapis.com/mcp/v1"]["token"]["access_token"] = new_access_token
            if "refresh_token" in res:
                data["https://drivemcp.googleapis.com/mcp/v1"]["token"]["refresh_token"] = res["refresh_token"]
                
            with open(TOKENS_PATH, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
                
            print("[Watchdog Auto-Healing SUCCESS] Token de Google Drive REFROSCADO Y GUARDADO exitosamente.")
            return True
    except Exception as ex:
        print(f"[Watchdog Auto-Healing FAILED]: {ex}")
        return False

def check_gemini_notebook():
    print("[Watchdog] Verificando estado de conexión a Gemini Notebook / NotebookLM...")
    if not os.path.exists(NLM_EXE):
        print("[Watchdog WARN] nlm.exe no encontrado en ruta predeterminada.")
        return False

    res = subprocess.run([NLM_EXE, "notebook", "list"], capture_output=True, text=True)
    if res.returncode == 0 and "Authentication Expired" not in res.stdout and "Authentication Error" not in res.stderr:
        print("[Watchdog OK] Conexión a Gemini Notebook (NotebookLM): 100% OPERATIVA.")
        return True
    else:
        print("[Watchdog WARN] Sesión de Gemini Notebook (NotebookLM) expirada.")
        print("-> Para renovar, ejecuta: python authenticate_notebooklm.py")
        return False

def run_watchdog():
    print("\n==================================================================")
    print("   WATCHDOG DE HERRAMIENTAS Y CONECTORES -- GÉNESIS LEGAL      ")
    print("==================================================================")
    drive_ok = check_and_heal_google_drive()
    notebook_ok = check_gemini_notebook()
    print("------------------------------------------------------------------")
    if drive_ok:
        print("[ESTADO] CONEXIÓN A GOOGLE DRIVE: SANA Y AUTOCURADA")
    else:
        print("[ESTADO] REVISA AUTENTICACIÓN GOOGLE DRIVE")
    if notebook_ok:
        print("[ESTADO] CONEXIÓN A GEMINI NOTEBOOK: SANA")
    else:
        print("[ESTADO] REVISA SESIÓN EN GEMINI NOTEBOOK (python authenticate_notebooklm.py)")
    print("==================================================================\n")

if __name__ == "__main__":
    run_watchdog()
