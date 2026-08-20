#!/usr/bin/env python3
"""
Prueba directa de acceso a Gmail API para nomackleo@gmail.com
"""

import os
import json
import urllib.request

def test_gmail():
    token_file = os.path.expanduser(r"~\.config\antigravity\personal_tokens.json")
    if not os.path.exists(token_file):
        print(f"[ERROR] No se encontro el archivo de tokens: {token_file}")
        print("Ejecuta primero: python get_gmail_token.py <CLIENT_ID> <CLIENT_SECRET>")
        return

    with open(token_file, "r") as f:
        tokens = json.load(f)

    access_token = tokens.get("access_token")
    print("==> Consultando la API de Gmail para nomackleo@gmail.com...")

    url = "https://gmail.googleapis.com/gmail/v1/users/me/profile"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {access_token}"})

    try:
        with urllib.request.urlopen(req) as resp:
            profile = json.loads(resp.read().decode("utf-8"))
            print("\n================================================")
            print(" ¡CONEXIÓN CON GMAIL EXITOSA!")
            print("================================================")
            print(f"Email Address  : {profile.get('emailAddress')}")
            print(f"Total Messages : {profile.get('messagesTotal')}")
            print(f"Total Threads  : {profile.get('threadsTotal')}")
            print("================================================\n")
    except Exception as e:
        print(f"[ERROR] Fallo la peticion a Gmail API: {e}")

if __name__ == "__main__":
    test_gmail()
