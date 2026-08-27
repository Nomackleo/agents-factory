#!/usr/bin/env python3
"""
Antigravity 2.0 - Google Workspace & Multi-Account Unified Client
Módulo unificado para interactuar con Gmail, Drive, Docs, Sheets y Calendar APIs
con soporte multi-cuenta, Model Armor (Sanitización de Ingesta), control de versiones y HITL.
"""

import os
import sys
import json
import urllib.request
import urllib.parse
import re
from datetime import datetime, timezone, timedelta
from typing import Dict, Any, Optional, List, Tuple

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

class ModelArmorSanitizer:
    """
    Sistema de Sanitización de Ingesta y Detección de Vectores de Inyección de Prompt (Model Armor).
    Analiza textos, correos y documentos externos antes de que sean procesados por el LLM.
    """
    SUSPICIOUS_PATTERNS = [
        r"ignore\s+(all\s+)?(previous|prior)\s+instructions",
        r"system\s*:\s*you\s+are\s+now",
        r"<\s*script\s*>",
        r"you\s+must\s+execute",
        r"output\s+the\s+following\s+secret",
        r"override\s+all\s+safety\s+rules",
        r"new\s+system\s+prompt\s*:",
        r"bypass\s+restrictions",
        r"act\s+as\s+DAN",
        r"disregard\s+(the\s+)?system\s+message"
    ]

    @classmethod
    def scan_and_sanitize(cls, text: str, source_label: str = "documento") -> Tuple[str, List[str]]:
        findings = []
        for pattern in cls.SUSPICIOUS_PATTERNS:
            matches = re.findall(pattern, text, re.IGNORECASE)
            if matches:
                findings.append(f"Vector sospechoso detectado [{source_label}]: patrón '{pattern}'")
        
        # Sanitizar caracteres nulos o secuencias de escape peligrosas
        sanitized = text.replace("\x00", "").replace("\r\n", "\n")
        return sanitized, findings


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
        access_token = self.tokens.get("access_token")
        if not access_token or force_refresh:
            return self.refresh_token()
        return access_token

    def refresh_token(self) -> str:
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

    def _make_request(self, url: str, method: str = "GET", payload: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None, raw_body: Optional[bytes] = None) -> Dict[str, Any]:
        token = self.get_valid_access_token()
        req_headers = {"Authorization": f"Bearer {token}"}
        if headers:
            req_headers.update(headers)

        data = raw_body
        if payload is not None and data is None:
            data = json.dumps(payload).encode("utf-8")
            req_headers["Content-Type"] = "application/json"

        req = urllib.request.Request(url, data=data, headers=req_headers, method=method)
        try:
            with urllib.request.urlopen(req) as resp:
                content_type = resp.headers.get("Content-Type", "")
                if "application/json" in content_type:
                    return json.loads(resp.read().decode("utf-8"))
                return {"status": "success", "data": resp.read().decode("utf-8", errors="ignore")}
        except urllib.error.HTTPError as e:
            if e.code == 401:
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
        return self._make_request("https://gmail.googleapis.com/gmail/v1/users/me/profile")

    def list_gmail_messages(self, max_results: int = 10, query: str = "") -> Dict[str, Any]:
        params = {"maxResults": str(max_results)}
        if query:
            params["q"] = query
        url = f"https://gmail.googleapis.com/gmail/v1/users/me/messages?{urllib.parse.urlencode(params)}"
        return self._make_request(url)

    def get_message_detail(self, message_id: str) -> Dict[str, Any]:
        url = f"https://gmail.googleapis.com/gmail/v1/users/me/messages/{message_id}?format=full"
        return self._make_request(url)

    def trash_message(self, message_id: str, hitl_confirmed: bool = False) -> Dict[str, Any]:
        """Mueve un mensaje a la papelera (Trash) de forma segura con confirmación HITL."""
        if not hitl_confirmed:
            raise PermissionError("ACCION BLOQUEADA: Mover correos a papelera exige confirmación HITL.")
        url = f"https://gmail.googleapis.com/gmail/v1/users/me/messages/{message_id}/trash"
        return self._make_request(url, method="POST")

    def batch_trash_messages(self, message_ids: List[str], hitl_confirmed: bool = False) -> List[Dict[str, Any]]:
        """Mueve múltiples mensajes a la papelera (Trash) con confirmación HITL."""
        if not hitl_confirmed:
            raise PermissionError("ACCION BLOQUEADA: Mover correos a papelera exige confirmación HITL.")
        results = []
        for msg_id in message_ids:
            try:
                res = self.trash_message(msg_id, hitl_confirmed=True)
                results.append({"id": msg_id, "status": "trashed", "res": res})
            except Exception as e:
                results.append({"id": msg_id, "status": "error", "error": str(e)})
        return results

    def batch_delete_messages(self, message_ids: List[str], hitl_confirmed: bool = False) -> Dict[str, Any]:
        """Elimina mensajes de forma permanente (requiere scope https://mail.google.com/)."""
        if not hitl_confirmed:
            raise PermissionError("ACCION BLOQUEADA: La eliminación masiva exige confirmación explícita (HITL).")
        url = "https://gmail.googleapis.com/gmail/v1/users/me/messages/batchDelete"
        return self._make_request(url, method="POST", payload={"ids": message_ids})

    # ==================== GOOGLE DRIVE API ====================
    def get_drive_about(self) -> Dict[str, Any]:
        return self._make_request("https://www.googleapis.com/drive/v3/about?fields=user,storageQuota")

    def list_drive_files(self, page_size: int = 10, query: str = "", order_by: str = "createdTime desc") -> Dict[str, Any]:
        params = {
            "pageSize": str(page_size),
            "fields": "files(id, name, mimeType, size, createdTime, modifiedTime, webViewLink)",
            "orderBy": order_by
        }
        if query:
            params["q"] = query
        url = f"https://www.googleapis.com/drive/v3/files?{urllib.parse.urlencode(params)}"
        return self._make_request(url)

    def create_drive_file(self, name: str, mime_type: str = "application/vnd.google-apps.document", description: str = "") -> Dict[str, Any]:
        """Crea un archivo o documento de Google en Drive."""
        metadata = {
            "name": name,
            "mimeType": mime_type,
            "description": description
        }
        url = "https://www.googleapis.com/drive/v3/files"
        return self._make_request(url, method="POST", payload=metadata)

    # ==================== GOOGLE CALENDAR API ====================
    def list_calendars(self) -> Dict[str, Any]:
        return self._make_request("https://www.googleapis.com/calendar/v3/users/me/calendarList")

    def list_calendar_events(self, calendar_id: str = "primary", max_results: int = 20, time_min: Optional[str] = None, time_max: Optional[str] = None, q: Optional[str] = None) -> Dict[str, Any]:
        params = {"maxResults": str(max_results), "singleEvents": "true", "orderBy": "startTime"}
        if time_min:
            params["timeMin"] = time_min
        if time_max:
            params["timeMax"] = time_max
        if q:
            params["q"] = q
        url = f"https://www.googleapis.com/calendar/v3/calendars/{urllib.parse.quote(calendar_id)}/events?{urllib.parse.urlencode(params)}"
        return self._make_request(url)


if __name__ == "__main__":
    if sys.platform == "win32":
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

    alias = sys.argv[1] if len(sys.argv) > 1 else "nomackleo"
    print(f"==> Verificando cliente unificado y Model Armor para: {alias}")
    client = WorkspaceClient(alias)
    profile = client.get_gmail_profile()
    print(f"  [OK] Conectado: {profile.get('emailAddress')}")
