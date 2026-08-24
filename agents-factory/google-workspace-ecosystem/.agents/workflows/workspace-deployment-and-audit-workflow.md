# Workflow de Despliegue, Parametrización y Auditoría Google Workspace

**PROPÓSITO**: Flujo de proceso estandarizado Top-Down (**Supervisor ➔ Research ➔ Ejecución ➔ Auditoría**) para desplegar, parametrizar y certificar entornos de Google Workspace Enterprise.

---

```mermaid
sequenceDiagram
    autonumber
    participant S as Supervisor / Lead Architect
    participant R as Research (knowledge.workspace.google.com)
    participant E as Ejecución (Subagentes Especialistas)
    participant MCP as Google Cloud Workspace MCP
    participant A as Auditoría & Compliance (ISO 27001)

    S->>R: 1. Definición de Requerimientos y Levantamiento de Dominio
    R->>S: 2. Especificación Técnica (DNS, IAM, RBAC, Seguridad)
    S->>E: 3. Despacho a Especialistas (IAM, Gmail, Drive, Calendar, DLP)
    E->>MCP: 4. Aplicación de Configuraciones e Invocación de Herramientas
    MCP->>E: 5. Respuesta de API (200 OK / 201 Created)
    E->>A: 6. Notificación de Despliegue Culminado
    A->>A: 7. Ejecución de Pruebas de Fuego (Smoke Tests) y Email Log Search
    A->>S: 8. Acta de Conformidad y Certificación Final (GEN-ACT)
```

---

## Fases del Workflow

### Fase 1: Supervisor (Definición Top-Down)
- Levantamiento de alcance de usuarios, licencias requeridas, dominios existentes y restricciones de negocio.

### Fase 2: Research & Especificación Técnica
- Consulta de la documentación oficial en `knowledge.workspace.google.com` y generación de la especificación de arquitectura (`workspace_architecture_spec.md`).

### Fase 3: Ejecución Modular
- Delegación a los subagentes especializados (`workspace-governance-iam-specialist`, `workspace-gmail-routing-specialist`, `workspace-drive-storage-specialist`, `workspace-security-dlp-architect`).
- Invocación de herramientas a través de `workspace-mcp-bridge-integrator`.

### Fase 4: Auditoría y Certificación
- Ejecución de las 3 Pruebas de Fuego (Casilla real, Catch-All y Firma DKIM saliente).
- Extracción de evidencia factual en *Email Log Search*.
- Emisión formal del Acta Técnica de Conformidad (`GEN-ACT-XXXX`).
