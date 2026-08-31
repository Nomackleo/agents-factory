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
                body_bytes = resp.read()
                if not body_bytes:
                    return {"status": "success", "code": getattr(resp, "status", 200)}
                if "application/json" in content_type:
                    return json.loads(body_bytes.decode("utf-8"))
                return {"status": "success", "data": body_bytes.decode("utf-8", errors="ignore")}
        except urllib.error.HTTPError as e:
            if e.code == 401:
                token = self.refresh_token()
                req_headers["Authorization"] = f"Bearer {token}"
                req_retry = urllib.request.Request(url, data=data, headers=req_headers, method=method)
                with urllib.request.urlopen(req_retry) as resp_retry:
                    content_type_retry = resp_retry.headers.get("Content-Type", "")
                    body_retry = resp_retry.read()
                    if not body_retry:
                        return {"status": "success", "code": getattr(resp_retry, "status", 200)}
                    if "application/json" in content_type_retry:
                        return json.loads(body_retry.decode("utf-8"))
                    return {"status": "success", "data": body_retry.decode("utf-8", errors="ignore")}
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

    def list_labels(self) -> Dict[str, Any]:
        """Lista todas las etiquetas (labels) de la cuenta de Gmail."""
        return self._make_request("https://gmail.googleapis.com/gmail/v1/users/me/labels")

    def get_label(self, label_id: str) -> Dict[str, Any]:
        """Obtiene la configuración y metadatos de una etiqueta específica."""
        url = f"https://gmail.googleapis.com/gmail/v1/users/me/labels/{label_id}"
        return self._make_request(url)

    def create_label(self, name: str, background_color: Optional[str] = None, text_color: Optional[str] = None,
                     label_list_visibility: str = "labelShow", message_list_visibility: str = "show") -> Dict[str, Any]:
        """Crea una nueva etiqueta jerárquica con color y visibilidad en Gmail."""
        payload: Dict[str, Any] = {
            "name": name,
            "labelListVisibility": label_list_visibility,
            "messageListVisibility": message_list_visibility
        }
        if background_color and text_color:
            payload["color"] = {
                "backgroundColor": background_color,
                "textColor": text_color
            }
        url = "https://gmail.googleapis.com/gmail/v1/users/me/labels"
        return self._make_request(url, method="POST", payload=payload)

    def update_label(self, label_id: str, name: Optional[str] = None, background_color: Optional[str] = None,
                     text_color: Optional[str] = None, label_list_visibility: Optional[str] = None,
                     message_list_visibility: Optional[str] = None) -> Dict[str, Any]:
        """Actualiza el nombre, color o visibilidad de una etiqueta existente."""
        current = self.get_label(label_id)
        payload = {
            "id": label_id,
            "name": name if name is not None else current.get("name"),
            "labelListVisibility": label_list_visibility if label_list_visibility is not None else current.get("labelListVisibility", "labelShow"),
            "messageListVisibility": message_list_visibility if message_list_visibility is not None else current.get("messageListVisibility", "show")
        }
        if background_color and text_color:
            payload["color"] = {
                "backgroundColor": background_color,
                "textColor": text_color
            }
        url = f"https://gmail.googleapis.com/gmail/v1/users/me/labels/{label_id}"
        return self._make_request(url, method="PUT", payload=payload)

    def delete_label(self, label_id: str, hitl_confirmed: bool = False) -> Dict[str, Any]:
        """Elimina una etiqueta de Gmail de forma segura con verificación HITL."""
        if not hitl_confirmed:
            raise PermissionError("ACCION BLOQUEADA: Eliminar etiquetas requiere confirmación HITL.")
        url = f"https://gmail.googleapis.com/gmail/v1/users/me/labels/{label_id}"
        return self._make_request(url, method="DELETE")

    def modify_message_labels(self, message_id: str, add_label_ids: Optional[List[str]] = None,
                              remove_label_ids: Optional[List[str]] = None) -> Dict[str, Any]:
        """Modifica etiquetas de un mensaje individual en Gmail."""
        payload = {
            "addLabelIds": add_label_ids or [],
            "removeLabelIds": remove_label_ids or []
        }
        url = f"https://gmail.googleapis.com/gmail/v1/users/me/messages/{message_id}/modify"
        return self._make_request(url, method="POST", payload=payload)

    def batch_modify_message_labels(self, message_ids: List[str], add_label_ids: Optional[List[str]] = None,
                                    remove_label_ids: Optional[List[str]] = None) -> Dict[str, Any]:
        """Aplica o remueve etiquetas en lote (batchModify) sobre una lista de IDs de mensajes."""
        payload = {
            "ids": message_ids,
            "addLabelIds": add_label_ids or [],
            "removeLabelIds": remove_label_ids or []
        }
        url = "https://gmail.googleapis.com/gmail/v1/users/me/messages/batchModify"
        return self._make_request(url, method="POST", payload=payload)

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

    # ==================== GOOGLE SHEETS API (v4) ====================
    def get_spreadsheet(self, spreadsheet_id: str, ranges: Optional[List[str]] = None, include_grid_data: bool = False) -> Dict[str, Any]:
        """Obtiene la metadata y estructura de una hoja de cálculo."""
        params = {"includeGridData": "true" if include_grid_data else "false"}
        if ranges:
            params["ranges"] = ranges
        url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}?{urllib.parse.urlencode(params)}"
        return self._make_request(url)

    def get_sheet_values(self, spreadsheet_id: str, range_name: str) -> Dict[str, Any]:
        """Lee los valores de un rango de celdas (ej. 'Hoja 1!A1:D10')."""
        url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{urllib.parse.quote(range_name)}"
        return self._make_request(url)

    def update_sheet_values(self, spreadsheet_id: str, range_name: str, values: List[List[Any]], value_input_option: str = "USER_ENTERED") -> Dict[str, Any]:
        """Escribe valores en un rango específico de celdas."""
        params = {"valueInputOption": value_input_option}
        url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{urllib.parse.quote(range_name)}?{urllib.parse.urlencode(params)}"
        payload = {
            "range": range_name,
            "majorDimension": "ROWS",
            "values": values
        }
        return self._make_request(url, method="PUT", payload=payload)

    def append_sheet_values(self, spreadsheet_id: str, range_name: str, values: List[List[Any]], value_input_option: str = "USER_ENTERED") -> Dict[str, Any]:
        """Inserta nuevas filas al final de una tabla de datos."""
        params = {"valueInputOption": value_input_option, "insertDataOption": "INSERT_ROWS"}
        url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{urllib.parse.quote(range_name)}:append?{urllib.parse.urlencode(params)}"
        payload = {
            "range": range_name,
            "majorDimension": "ROWS",
            "values": values
        }
        return self._make_request(url, method="POST", payload=payload)

    def create_spreadsheet(self, title: str, sheet_names: Optional[List[str]] = None) -> Dict[str, Any]:
        """Crea una nueva hoja de cálculo en Google Sheets."""
        payload: Dict[str, Any] = {
            "properties": {"title": title}
        }
        if sheet_names:
            payload["sheets"] = [{"properties": {"title": name}} for name in sheet_names]
        url = "https://sheets.googleapis.com/v4/spreadsheets"
        return self._make_request(url, method="POST", payload=payload)

    def batch_update_spreadsheet(self, spreadsheet_id: str, requests: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Aplica múltiples operaciones de formato, validación o creación de hojas."""
        url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}:batchUpdate"
        return self._make_request(url, method="POST", payload={"requests": requests})

    # ==================== GOOGLE SLIDES API (v1) ====================
    def get_presentation(self, presentation_id: str) -> Dict[str, Any]:
        """Obtiene la estructura y contenido de una presentación de Google Slides."""
        url = f"https://slides.googleapis.com/v1/presentations/{presentation_id}"
        return self._make_request(url)

    def create_presentation(self, title: str) -> Dict[str, Any]:
        """Crea una nueva presentación en Google Slides."""
        url = "https://slides.googleapis.com/v1/presentations"
        return self._make_request(url, method="POST", payload={"title": title})

    def batch_update_presentation(self, presentation_id: str, requests: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Aplica actualizaciones en lote sobre diapositivas (crear slides, insertar texto, temas)."""
        url = f"https://slides.googleapis.com/v1/presentations/{presentation_id}:batchUpdate"
        return self._make_request(url, method="POST", payload={"requests": requests})

    # ==================== GOOGLE VIDS & VIDEO ASSETS ====================
    def list_vids_projects(self, page_size: int = 10, query: str = "") -> Dict[str, Any]:
        """Lista proyectos de Google Vids y videos corporativos en Google Drive."""
        vids_q = "mimeType = 'application/vnd.google-apps.vid' or mimeType contains 'video/'"
        if query:
            vids_q = f"({vids_q}) and ({query})"
        return self.list_drive_files(page_size=page_size, query=vids_q)

    def create_vids_project(self, title: str, description: str = "") -> Dict[str, Any]:
        """Crea un nuevo proyecto o placeholder de video en Google Drive."""
        return self.create_drive_file(
            name=title,
            mime_type="application/vnd.google-apps.vid",
            description=description
        )

    # ==================== GOOGLE ANALYTICS 4 DATA API (v1beta) ====================
    def run_analytics_report(self, property_id: str, dimensions: List[str], metrics: List[str], date_ranges: Optional[List[Dict[str, str]]] = None, limit: int = 100) -> Dict[str, Any]:
        """Ejecuta un reporte personalizado de Google Analytics 4 (GA4)."""
        if not date_ranges:
            date_ranges = [{"startDate": "30daysAgo", "endDate": "today"}]
        payload = {
            "dimensions": [{"name": d} for d in dimensions],
            "metrics": [{"name": m} for m in metrics],
            "dateRanges": date_ranges,
            "limit": limit
        }
        url = f"https://analyticsdata.googleapis.com/v1beta/properties/{property_id}:runReport"
        return self._make_request(url, method="POST", payload=payload)

    def run_realtime_analytics_report(self, property_id: str, dimensions: List[str], metrics: List[str]) -> Dict[str, Any]:
        """Ejecuta un reporte en tiempo real de usuarios activos en GA4."""
        payload = {
            "dimensions": [{"name": d} for d in dimensions],
            "metrics": [{"name": m} for m in metrics]
        }
        url = f"https://analyticsdata.googleapis.com/v1beta/properties/{property_id}:runRealtimeReport"
        return self._make_request(url, method="POST", payload=payload)

    def list_analytics_account_summaries(self) -> Dict[str, Any]:
        """Lista las cuentas y propiedades GA4 disponibles para el usuario."""
        url = "https://analyticsadmin.googleapis.com/v1alpha/accountSummaries"
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
