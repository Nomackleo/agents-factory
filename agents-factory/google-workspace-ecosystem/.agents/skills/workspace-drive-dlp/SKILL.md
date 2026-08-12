---
name: workspace-drive-dlp
description: "Gobernanza multi-tenant de Google Drive, administración de Unidades Compartidas (Shared Drives), reglas de DLP y prevención de fuga de datos."
---

# Workspace Drive & DLP Governance Skill

## Descripción General
Esta habilidad permite estructurar la arquitectura documental en Google Drive, administrar Unidades Compartidas (*Shared Drives*), aplicar políticas de Prevención de Fuga de Datos (DLP) y auditar permisos de descarga, copia e impresión conforme a los estándares ISO 27001 e ISO 25010.

## Capacidades Principales
1. **Aprovisionamiento de Unidades Compartidas (*Shared Drives*)**:
   - Creación de Shared Drives con estructuras RBAC por área o proyecto.
   - Aplicación de restricciones de seguridad (desactivación de descargas/copias para lectores en áreas sensibles como Forense, Poligrafía y Psicología).
2. **Políticas DLP y Clasificación de Datos**:
   - Creación de reglas de inspección de contenido para cédulas, tarjetas bancarias y sellos confidenciales.
3. **Auditoría RAG e Ingesta para Gemini**:
   - Generación de manifiestos `.context.jsonld` y archivos `.gdriveignore` para optimizar las consultas RAG en Gemini NotebookLM sin exponer PII ni secretos.

## Requisitos de Integración MCP
- **Servidor MCP**: `google-workspace-mcp`
- **APIs de GCP Requeridas**: `drive.googleapis.com` (Google Drive API), `admin.googleapis.com`
- **OAuth Scopes**:
  - `https://www.googleapis.com/auth/drive`
  - `https://www.googleapis.com/auth/drive.file`
