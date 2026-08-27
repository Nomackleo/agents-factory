#!/usr/bin/env python3
"""
Antigravity 2.0 - Google Workspace & Multi-Account Unified Client
Módulo unificado para interactuar con Gmail, Drive, Docs, Sheets y Calendar APIs
con soporte multi-cuenta (nomackleo, nomack3d, genesis-legal) y refresco automático de tokens.
"""

import os
import sys
import json
import urllib.request
import urllib.parse
from typing import Dict, Any, Optional, List

DEFAULT_CLIENT_ID = os.environ.get("GOOGLE_WORKSPACE_CLIENT_ID", "")
DEFAULT_CLIENT_SECRET = os.environ.get("GOOGLE_WORKSPACE_CLIENT_SECRET", "")

def _load_default_credentials():
    global DEFAULT_CLIENT_ID, DEFAULT_CLIENT_SECRET
    if not DEFAULT_CLIENT_ID or not DEFAULT_CLIENT_SECRET:
        cred_path = os.path.expanduser(r"~\.config\antigravity\oauth_credentials.json")
        if os.path.exists(cred_path):
            try:
                with open(cred_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    DEFAULT_CLIENT_ID = DEFAULT_CLIENT_ID or data.get("client_id", "")
                    DEFAULT_CLIENT_SECRET = DEFAULT_CLIENT_SECRET or data.get("client_secret", "")
            except Exception:
                pass

_load_default_credentials()

class WorkspaceClient:
    def __init__(self, account_alias: str = "nomackleo", client_id: Optional[str] = None, client_secret: Optional[str] = None):
        self.account_alias = account_alias
        self.client_id = client_id or DEFAULT_CLIENT_ID
        self.client_secret = client_secret or DEFAULT_CLIENT_SECRET
        self.token_file = os.path.expanduser(rf"~\.config\antigravity\tokens_{account_alias}.json")
        self.tokens = self._load_tokens()

    def _load_tokens(self) -> Dict[str, Any]:
        if not os.path.exists(self.token_file):
            raise FileNotFoundError(f"No se encontró el archivo de tokens para '{self.account_alias}' en {self.token_file}.")
        with open(self.token_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def _save_tokens(self):
        with open(self.token_file, "w", encoding="utf-8") as f:
            json.dump(self.tokens, f, indent=2)

    def get_valid_access_token(self, force_refresh: bool = False) -> str:
        """Obtiene un token de acceso válido, refrescándolo si es necesario."""
        access_token = self.tokens.get("access_token")
        if not access_token or force_refresh:
            return self.refresh_token()
        return access_token

    def refresh_token(self) -> str:
        """Refresca el Access Token usando el Refresh Token permanente."""
        refresh_token = self.tokens.get("refresh_token")
        if not refresh_token:
            raise ValueError(f"No hay refresh_token guardado para '{self.account_alias}'.")

        token_url = "https://oauth2.googleapis.com/token"
        data = urllib.parse.urlencode({
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "refresh_token": refresh_token,
            "grant_type": "refresh_token"
        }).encode("utf-8")

        req = urllib.request.Request(token_url, data=data, headers={"Content-Type": "application/x-www-form-urlencoded"})
        try:
            with urllib.request.urlopen(req) as resp:
                result = json.loads(resp.read().decode("utf-8"))
            self.tokens["access_token"] = result["access_token"]
            if "refresh_token" in result:
                self.tokens["refresh_token"] = result["refresh_token"]
            self._save_tokens()
            return result["access_token"]
        except Exception as e:
            raise RuntimeError(f"Error al refrescar token para {self.account_alias}: {e}")

    def _make_request(self, url: str, method: str = "GET", payload: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        """Ejecuta una petición HTTP a las APIs de Google con reintento automático en caso de token expirado (401)."""
        token = self.get_valid_access_token()
        req_headers = {"Authorization": f"Bearer {token}"}
        if headers:
            req_headers.update(headers)

        data = None
        if payload is not None:
            data = json.dumps(payload).encode("utf-8")
            req_headers["Content-Type"] = "application/json"

        req = urllib.request.Request(url, data=data, headers=req_headers, method=method)
        try:
            with urllib.request.urlopen(req) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 401:
                # Token expirado -> refrescar e intentar una vez más
                token = self.refresh_token()
                req_headers["Authorization"] = f"Bearer {token}"
                req_retry = urllib.request.Request(url, data=data, headers=req_headers, method=method)
                with urllib.request.urlopen(req_retry) as resp_retry:
                    return json.loads(resp_retry.read().decode("utf-8"))
            else:
                body = e.read().decode("utf-8", errors="ignore")
                raise RuntimeError(f"HTTP {e.code} en {url}: {body}")

    # ==================== GMAIL API ====================
    def get_gmail_profile(self) -> Dict[str, Any]:
        """Consulta perfil y estadísticas de Gmail."""
        return self._make_request("https://gmail.googleapis.com/gmail/v1/users/me/profile")

    def list_gmail_messages(self, max_results: int = 10, query: str = "") -> Dict[str, Any]:
        """Lista mensajes de la bandeja de entrada con filtro opcional."""
        params = {"maxResults": str(max_results)}
        if query:
            params["q"] = query
        url = f"https://gmail.googleapis.com/gmail/v1/users/me/messages?{urllib.parse.urlencode(params)}"
        return self._make_request(url)

    # ==================== GOOGLE DRIVE API ====================
    def get_drive_about(self) -> Dict[str, Any]:
        """Consulta cuota de almacenamiento y datos de usuario en Drive."""
        return self._make_request("https://www.googleapis.com/drive/v3/about?fields=user,storageQuota")

    def list_drive_files(self, page_size: int = 10, query: str = "") -> Dict[str, Any]:
        """Lista archivos y carpetas de Google Drive."""
        params = {"pageSize": str(page_size), "fields": "files(id, name, mimeType, size, modifiedTime)"}
        if query:
            params["q"] = query
        url = f"https://www.googleapis.com/drive/v3/files?{urllib.parse.urlencode(params)}"
        return self._make_request(url)

    # ==================== GOOGLE CALENDAR API ====================
    def list_calendars(self) -> Dict[str, Any]:
        """Lista los calendarios disponibles para la cuenta."""
        return self._make_request("https://www.googleapis.com/calendar/v3/users/me/calendarList")

    def list_calendar_events(self, calendar_id: str = "primary", max_results: int = 10) -> Dict[str, Any]:
        """Lista próximos eventos del calendario."""
        params = {"maxResults": str(max_results), "orderBy": "startTime", "singleEvents": "true"}
        url = f"https://www.googleapis.com/calendar/v3/calendars/{urllib.parse.quote(calendar_id)}/events?{urllib.parse.urlencode(params)}"
        return self._make_request(url)


if __name__ == "__main__":
    import sys
    if sys.platform == "win32":
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

    alias = sys.argv[1] if len(sys.argv) > 1 else "nomackleo"
    print(f"==> Probando cliente unificado para: {alias}")
    client = WorkspaceClient(alias)
    
    # 1. Probar Gmail
    try:
        profile = client.get_gmail_profile()
        print(f"  [OK] Gmail: {profile.get('emailAddress')} ({profile.get('messagesTotal')} correos)")
    except Exception as e:
        print(f"  [ERROR] Gmail: {e}")

    # 2. Probar Drive
    try:
        drive = client.get_drive_about()
        print(f"  [OK] Drive: {drive.get('user', {}).get('displayName')}")
    except Exception as e:
        print(f"  [ERROR] Drive: {e}")

    # 3. Probar Calendar
    try:
        cals = client.list_calendars()
        print(f"  [OK] Calendar: {len(cals.get('items', []))} calendarios encontrados")
    except Exception as e:
        print(f"  [ERROR] Calendar: {e}")

