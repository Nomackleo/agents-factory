# Google Workspace Ecosystem: Topologic Architecture & Multi-Agent Matrix

**WHO**: Maintained by the Enterprise Architecture, Google Workspace Lead Architects & AI Knowledge Engineering teams.  
**WHAT**: Ecosistema agéntico integral para la parametrización de nivel empresarial de Google Workspace (`admin.google.com`), resolución DNS autoritativa, ciberseguridad criptográfica de correo (SPF/DKIM/DMARC), gobierno de identidades (IAM), Unidades Compartidas (RBAC) e integración determinista con Google Cloud MCP.  
**METODOLOGÍA**: Top-Down (**Supervisor ➔ Research ➔ Ejecución ➔ Auditoría**) bajo estándares **Neo-CRISPE v2.0**.  
**CUMPLIMIENTO NORMATIVO**: ISO 9001:2015 (SGC), ISO/IEC 27001:2022 (ISMS), ISO/IEC 42001:2023 (AIMS), ISO 25010 (Calidad de Software), SOC 2 & NIST CSF 2.0.  

---

## 1. Topología del Ecosistema Agéntico

```mermaid
graph TD
    %% Core Ecosystem
    A["Google Workspace Ecosystem"] --> B[".agents/rules/"]
    A --> C[".agents/workflows/"]
    A --> D[".agents/skills/ (Subagentes Especialistas)"]
    A --> E["knowledge/ (Compendios Maestros)"]
    A --> F["notebooklm-templates/"]

    %% Rules
    B --> B1["workspace-enterprise-security-rules.md"]
    B --> B2["multi-tenant-iam-security-rules.md"]
    B --> B3["gdrive-posix-naming-rules.md"]

    %% Workflows
    C --> C1["workspace-deployment-and-audit-workflow.md"]
    C --> C2["gdrive-workspace-indexing-workflow.md"]

    %% Specialized Subagents (Skills)
    D --> D1["workspace-governance-iam-specialist"]
    D --> D2["workspace-security-dlp-architect"]
    D --> D3["workspace-gmail-routing-specialist"]
    D --> D4["workspace-calendar-assistant-agent"]
    D --> D5["workspace-drive-storage-specialist"]
    D --> D6["workspace-audit-compliance-analyst"]
    D --> D7["workspace-mcp-bridge-integrator"]
    D --> D8["workspace-sheets-data-architect"]
    D --> D9["workspace-slides-presentation-designer"]
    D --> D10["workspace-vids-media-specialist"]
    D --> D11["workspace-analytics-intelligence-analyst"]

    %% Knowledge Bases
    E --> E1["google_workspace_enterprise_admin_mastery.md"]
    E --> E2["google_workspace_mcp_integration_matrix.md"]
    E --> E3["sheets_api_v4_data_architecture_mastery.md"]
    E --> E4["slides_api_v1_presentation_automation_mastery.md"]
    E --> E5["vids_workspace_video_production_mastery.md"]
    E --> E6["google_analytics_4_data_api_mastery.md"]

    %% Styling Branding
    classDef domain fill:#07283d,stroke:#ffd231,stroke-width:2px,color:#ffffff
    classDef subagent fill:#056c5c,stroke:#ffd231,stroke-width:1px,color:#ffffff
    classDef file fill:#1a3a5c,stroke:#cccccc,stroke-width:1px,color:#ffffff
    classDef knowledge fill:#ba1650,stroke:#ffd231,stroke-width:1px,color:#ffffff

    class A domain
    class D1,D2,D3,D4,D5,D6,D7,D8,D9,D10,D11 subagent
    class B1,B2,B3,C1,C2,F file
    class E1,E2,E3,E4,E5,E6 knowledge
```

---

## 2. Catálogo de Subagentes Especialistas (Roles & Ámbitos)

| Subagente | Responsabilidad Principal | Herramientas & Ámbitos |
| :--- | :--- | :--- |
| **`workspace-governance-iam-specialist`** | Gestión de identidades, jerarquías de Unidades Organizacionales (UOs), asignación de licencias y roles de administración delegados. | `admin.directory.user`<br>`admin.directory.orgunit` |
| **`workspace-security-dlp-architect`** | Políticas de autenticación 2FA/MFA obligatorio por UO, listas de acceso contextual (CAA), reglas DLP y control de aplicaciones OAuth/API. | `admin.directory.user.security`<br>Security Center & DLP Engine |
| **`workspace-gmail-routing-specialist`** | Parametrización DNS (MX unificado, SPF, DKIM RSA 2048, DMARC), reglas Catch-All (*Default Routing*), Email Allowlist y SMTP Relay. | `gmail.settings.basic`<br>DNS & Enrutamiento SMTP |
| **`workspace-calendar-assistant-agent`** | Gestión de calendarios compartidos, recursos de salas/equipos, políticas de visibilidad por UO e interoperabilidad con Exchange/Outlook. | `calendar`<br>`calendar.events` |
| **`workspace-drive-storage-specialist`** | Arquitectura de Unidades Compartidas (*Shared Drives*), matriz RBAC, políticas de bloqueo de descarga/copia e indexación RAG. | `drive`<br>`drive.file`<br>`drive.metadata` |
| **`workspace-sheets-data-architect`** | Modelado de datos, tablas, fórmulas matriciales (`ARRAYFORMULA`, `XLOOKUP`, `QUERY`) y sincronización bidireccional de datos con Sheets API v4. | `sheets.spreadsheets`<br>`sheets.values` |
| **`workspace-slides-presentation-designer`** | Creación programática de pitch decks y presentaciones ejecutivas, inserción de diagramas, formas y temas visuales con Slides API v1. | `slides.presentations`<br>`slides.batchUpdate` |
| **`workspace-vids-media-specialist`** | Orquestación de proyectos de video corporativo en Google Vids, gestión de plantillas y activos multimedia en Google Drive. | `vids.projects`<br>`drive.file` |
| **`workspace-analytics-intelligence-analyst`** | Extracción de métricas, reportes de tráfico, eventos, embudos de conversión y análisis en tiempo real con Google Analytics 4 (GA4) Data API. | `analytics.data.readonly`<br>`analytics.readonly` |
| **`workspace-audit-compliance-analyst`** | Búsqueda forense en *Email Log Search*, auditoría de eventos de administración y reportes de conformidad ISO 27001 / ISO 9001. | `admin.reports.audit.readonly`<br>Email Log Search |
| **`workspace-mcp-bridge-integrator`** | Interfaz determinista y tipada con el servidor MCP unificado de Google Workspace y Google Cloud. | Google Workspace MCP Server |

---

## 3. Principio de Cero Sobrelapamiento (*Zero-Overlap Policy*)

Para garantizar la pureza operativa de los procesos y evitar colisiones entre el MCP oficial de Google Cloud y los subagentes:

1. **Ámbitos Estrictamente Delimitados**: Cada subagente invoca únicamente las herramientas y scopes autorizados en las matrices de conocimiento.
2. **Idempotencia de Operaciones**: Toda mutación en la API de Workspace se ejecuta de forma declarativa e idempotente.
3. **Control de Modificaciones Críticas**: Toda operación destructiva (eliminación de cuentas, archivos o Shared Drives) requiere validación *Human-in-the-Loop* (HITL).
