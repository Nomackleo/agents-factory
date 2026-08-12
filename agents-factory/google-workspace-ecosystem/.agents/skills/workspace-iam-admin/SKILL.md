---
name: workspace-iam-admin
description: "Administración multi-tenant de identidades, usuarios, Unidades Organizacionales (UO), grupos y políticas 2SV en Google Workspace mediante Admin SDK API."
---

# Workspace IAM Admin Skill

## Descripción General

Esta habilidad permite a los agentes de Google Antigravity SDK aprovisionar, auditar y gestionar identidades corporativas, estructuras de Unidades Organizacionales (UO), asignación de licencias y cumplimiento de Verificación en 2 Pasos (2SV) para cualquier tenant de Google Workspace.

## Capacidades Principales

1. **Aprovisionamiento de Usuarios**: Crear, actualizar o suspender cuentas de usuario en UOs específicas (`/Genesis-Legal/UO-Direccion`, `/Genesis-Legal/UO-Forense`, etc.).
2. **Gestión de Dominios y Alias**: Configurar dominios primarios y dominios alias (ej. `gscg.com.co` como alias de `genesislegal.co`).
3. **Auditoría 2SV y Seguridad**: Verificar el estado de enrolamiento de 2FA y aplicar periodos de gracia.
4. **Control de Accesos RBAC**: Asignar roles de administración delegados y auditar aplicaciones OAuth conectadas.

## Requisitos de Integración MCP

- **Servidor MCP**: `google-workspace-mcp`
- **APIs de GCP Requeridas**: `admin.googleapis.com` (Admin SDK API), `iam.googleapis.com`
- **OAuth Scopes**:
  - `https://www.googleapis.com/auth/admin.directory.user`
  - `https://www.googleapis.com/auth/admin.directory.orgunit`
  - `https://www.googleapis.com/auth/admin.directory.domain`

## Modos de Ejecución Multi-Tenant

- `tenant_id`: Identificador del cliente (ej. `genesis-legal`, `personal-dev`, `enterprise-client-x`).
- Cada llamada debe pasar explícitamente el `tenant_id` para resolver las credenciales aisladas en Vault.
