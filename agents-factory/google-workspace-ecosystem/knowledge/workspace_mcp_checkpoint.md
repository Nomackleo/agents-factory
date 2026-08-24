# CHECKPOINT: Google Workspace & Multi-Account MCP Integration

**Fecha:** 24 de Agosto de 2026  
**Ecosistema:** `google-workspace-ecosystem` (`agents-factory/google-workspace-ecosystem/`)  
**Proyecto Base GCP:** `alert-tine-501115-p4` (*antigravity*)  
**Cuenta Maestra GCP:** `nomackleo@gmail.com`  
**Client ID OAuth:** `${GOOGLE_WORKSPACE_CLIENT_ID}` (Configurado en GCP Desktop App)  
**Client Secret OAuth:** `${GOOGLE_WORKSPACE_CLIENT_SECRET}` (Almacenado de forma segura)

---

## 1. Estado Actual de Cuentas e Integración

### A. `nomackleo@gmail.com` (Cuenta Personal / Principal)
- **Estado:** 🟢 **AUTENTICADO Y VERIFICADO AL 100% (LIVE)**
- **Tokens Guardados:** `C:\Users\Nomack\.config\antigravity\tokens_nomackleo.json`
- **Gmail API:** Verificada en vivo (21,249 mensajes / 20,601 hilos).
- **Pendiente en GCP Console:**
  - Habilitar `drive.googleapis.com` en Marketplace: [Link Directo Drive](https://console.cloud.google.com/marketplace/product/google/drive.googleapis.com?project=alert-tine-501115-p4)
  - Habilitar `calendar-json.googleapis.com` en Marketplace: [Link Directo Calendar](https://console.cloud.google.com/marketplace/product/google/calendar-json.googleapis.com?project=alert-tine-501115-p4)
  - Habilitar `docs.googleapis.com` y `sheets.googleapis.com`.

### B. `nomack3d@gmail.com` (Segunda Cuenta Personal)
- **Estado:** 🟡 **CONFIGURADA EN TEST USERS, PENDIENTE CONSENTIMIENTO OAUTH**
- **Siguiente Acción:**
  1. Correr `python mcp/google-workspace/get_oauth_tokens.py nomack3d "<CLIENT_ID>" "<CLIENT_SECRET>"`
  2. Tokens se guardarán automáticamente en `C:\Users\Nomack\.config\antigravity\tokens_nomack3d.json`.

### C. `admin@genesislegal.co` / `genesislegal.co` (Inquilino Empresarial)
- **Estado:** 🟡 **LISTO PARA SERVICE ACCOUNT DWD (Pausado intencionalmente)**
- **Service Account en GCP:** `mcp-workspace-agent@alert-tine-501115-p4.iam.gserviceaccount.com`
- **Siguiente Acción:**
  1. Crear la clave `antigravity-sa-key.json` y registrar el `oauth2ClientId` en `admin.google.com` (Domain-Wide Delegation).
