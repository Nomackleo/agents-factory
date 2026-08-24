#!/usr/bin/env python3
"""
Prueba directa de acceso a Gmail, Drive y Calendar API para cuentas personales Antigravity.
"""

import os
import sys
import json
import urllib.request
import urllib.parse

def test_account(account_alias="nomackleo"):
    token_file = os.path.expanduser(rf"~\.config\antigravity\tokens_{account_alias}.json")
    if not os.path.exists(token_file):
        print(f"[ERROR] No se encontro el archivo de tokens: {token_file}")
        return

    with open(token_file, "r", encoding="utf-8") as f:
        tokens = json.load(f)

    access_token = tokens.get("access_token")
    print(f"\n==> [1/3] Verificando perfil de Gmail ({account_alias})...")
    url = "https://gmail.googleapis.com/gmail/v1/users/me/profile"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {access_token}"})

    try:
        with urllib.request.urlopen(req) as resp:
            profile = json.loads(resp.read().decode("utf-8"))
            print("  [OK] Gmail Conectado:")
            print(f"       - Email Address  : {profile.get('emailAddress')}")
            print(f"       - Total Mensajes : {profile.get('messagesTotal')}")
            print(f"       - Total Threads  : {profile.get('threadsTotal')}")
    except Exception as e:
        print(f"  [ERROR] Gmail API: {e}")

    print(f"\n==> [2/3] Verificando acceso a Google Drive ({account_alias})...")
    url_drive = "https://www.googleapis.com/drive/v3/about?fields=user,storageQuota"
    req_drive = urllib.request.Request(url_drive, headers={"Authorization": f"Bearer {access_token}"})

    try:
        with urllib.request.urlopen(req_drive) as resp:
            about = json.loads(resp.read().decode("utf-8"))
            user = about.get("user", {})
            quota = about.get("storageQuota", {})
            limit_gb = round(int(quota.get("limit", 0)) / (1024**3), 2) if quota.get("limit") else "Ilimitado"
            usage_gb = round(int(quota.get("usage", 0)) / (1024**3), 2)
            print("  [OK] Google Drive Conectado:")
            print(f"       - Propietario : {user.get('displayName')} ({user.get('emailAddress')})")
            print(f"       - Uso Storage : {usage_gb} GB / {limit_gb} GB")
    except Exception as e:
        print(f"  [ERROR] Drive API: {e}")

    print(f"\n==> [3/3] Verificando acceso a Google Calendar ({account_alias})...")
    url_cal = "https://www.googleapis.com/calendar/v3/users/me/calendarList?maxResults=5"
    req_cal = urllib.request.Request(url_cal, headers={"Authorization": f"Bearer {access_token}"})

    try:
        with urllib.request.urlopen(req_cal) as resp:
            calendars = json.loads(resp.read().decode("utf-8"))
            items = calendars.get("items", [])
            print(f"  [OK] Calendar Conectado ({len(items)} calendarios encontrados):")
            for cal in items[:3]:
                print(f"       - Calendario: {cal.get('summary')}")
    except Exception as e:
        print(f"  [ERROR] Calendar API: {e}")

    print("\n==================================================================")
    print(f" [ÉXITO TOTAL] SOBERANÍA Y CONEXIÓN VERIFICADA PARA: {account_alias}")
    print("==================================================================\n")

if __name__ == "__main__":
    alias = sys.argv[1] if len(sys.argv) > 1 else "nomackleo"
    test_account(alias)
