---
name: workspace-gmail-security
description: "Gestión multi-tenant de seguridad de correo Gmail, enrutamiento, MX, SPF/DKIM/DMARC, cuarentenas y protección anti-phishing."
---

# Workspace Gmail Security & Routing Skill

## Descripción General
Esta habilidad otorga capacidades avanzadas para auditar y parametrizar la seguridad del correo electrónico en Gmail, entregabilidad, firmas DKIM de 2048 bits, registros MX, políticas DMARC, reglas de enrutamiento (Default Routing / Split Delivery) y Cuarentenas de Administración en cualquier tenant corporativo.

## Capacidades Principales
1. **Verificación de Entregabilidad & DNS**:
   - Generación de claves DKIM `google._domainkey` (2048 bits).
   - Verificación de registros SPF (`v=spf1 include:_spf.google.com ~all`).
   - Auditoría de políticas DMARC (`p=quarantine` o `p=reject`).
2. **Enrutamiento Avanzado (Routing Rules)**:
   - Configuración de Hosts Secundarios para Split Delivery o Dual Delivery.
   - Definición de reglas de captura general (*Catch-All*) en Enrutamiento Predeterminado.
3. **Gestión de Cuarentenas & Phishing Shield**:
   - Creación de cuarentenas administrativas (`Cuarentena_Legal_Seguridad`).
   - Asignación de revisores y notificaciones de retención.
   - Activación de advertencias de destinatarios externos y banners de seguridad.

## Requisitos de Integración MCP
- **Servidor MCP**: `google-workspace-mcp`
- **APIs de GCP Requeridas**: `gmail.googleapis.com` (Gmail API), `admin.googleapis.com`
- **OAuth Scopes**:
  - `https://www.googleapis.com/auth/gmail.settings.basic`
  - `https://www.googleapis.com/auth/gmail.settings.sharing`
  - `https://www.googleapis.com/auth/admin.directory.domain`

## Árbol Diagnóstico Integrado (Email Routing Troubleshooter)
- Identifica si el tráfico entrante está retenido por enrutadores heredados cPanel (*Local Mail Exchanger*), perfiles IMAP locales en Microsoft Outlook o falta de cutover MX en el registrador DNS.
