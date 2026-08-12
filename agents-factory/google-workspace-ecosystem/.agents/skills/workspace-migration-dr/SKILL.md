---
name: workspace-migration-dr
description: "Orquestación multi-tenant de migraciones de correo (GWMMO, IMAP, PST), respaldo total de hosting/cPanel, corte de registros MX y recuperación ante desastres (DR)."
---

# Workspace Migration & Disaster Recovery Skill

## Descripción General

Esta habilidad proporciona procedimientos operativos estandarizados (SOPs) y scripts de orquestación para migrar históricamente correos, calendarios y contactos desde plataformas heredadas (SiteGround, cPanel, Exchange, IMAP) hacia Google Workspace con garantía de **Cero Pérdida de Datos**.

## Capacidades Principales

1. **Conmutación de Dominio Alias & Cutover DNS MX (Patrón Comprobado)**:
   - Vinculación del dominio heredado como *Dominio Aparcado* en el hosting cPanel/SiteGround para habilitar la edición de zona DNS.
   - Inserción de CNAME/TXT de verificación (`google-site-verification`).
   - Conmutación de registros MX a `smtp.google.com` (Prioridad 1) con TTL reducido (300s).
   - Actualización del registro TXT SPF a `v=spf1 include:_spf.google.com ~all`.
2. **Ingesta Incremental GWMMO**:
   - Inyección de parches de registro en Microsoft Outlook (Click-to-Run).
   - Ingesta directa desde archivos PST locales hacia casillas corporativas.
3. **Respaldo Total de Hosting y Bases de Datos**:
   - Exportación de bases de datos MySQL (`.sql.gz`).
   - Compresión de directorio raíz web (`/public_html`).
   - Exportación de zonas DNS completas (formato BIND/JSON).

## Requisitos de Integración MCP

- **Servidor MCP**: `google-workspace-mcp`
- **APIs de GCP Requeridas**: `admin.googleapis.com`, `gmail.googleapis.com`
- **Scripts Auxiliares**: `bin/audit_d_drive_pst.py`, `bin/fix_gwmmo_outlook_registry.ps1`, `bin/verify_pst_health.ps1`.
