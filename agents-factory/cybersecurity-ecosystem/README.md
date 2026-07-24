# Cybersecurity & AI Resilience Ecosystem

Bienvenido al **Cybersecurity & AI Resilience Ecosystem** de Antigravity. Este ecosistema consolida las capacidades ofensivas, defensivas, de gobernanza de IA y cumplimiento de seguridad, albergando una fuerza laboral de agentes autónomos entrenados bajo los estándares de **ISO 27001 (ISMS)**, **ISO 42001 (AIMS)**, **NIST CSF 2.0**, MITRE ATT&CK, D3FEND y OWASP Top 10 for LLMs.

---

## 🛡️ Guilds de Seguridad y Alineación Normativa ISO/NIST

Este ecosistema está organizado en gremios especializados ("Guilds") que integran los checklists del Gemini Notebook `NIST CSF 2.0 and ISO 42001, 27001: Cybersecurity and AI Management`:

- **SOC Guild (Defensa & DORA Metrics):**
  - Analistas defensivos (L1/L2), respuesta a incidentes y caza de amenazas (Threat Hunting).
  - Alineado con **NIST CSF Detect (DE)** y **Respond (RS)**.
  - Ejecuta el **Dead-man Switch (RS.MA-01)** y la recuperación del servicio en menos de 60 segundos (**DORA MTTR**).

- **Red Team Guild (Ofensiva & Emulación de Adversarios):**
  - Operadores ofensivos y evaluación de vulnerabilidades bajo MITRE ATT&CK.
  - Pruebas de estrés y simulaciones de Prompt Injection Indirecto (**NIST DE.AE-01**).

- **AppSec Guild (Seguridad en Aplicaciones & Sistemas Agénticos):**
  - Pruebas de seguridad en código, análisis estático y auditoría de herramientas MCP.
  - Alineado con **ISO 27001 A.12/A.14** (Seguridad Operativa) y **NIST CSF PR.PS-01** (Sandboxing y ejecución aislada).

- **Compliance & Risk Guild (Gobernanza ISO 42001 & 27001):**
  - Oficiales de cumplimiento y auditores de infraestructura.
  - **ISO 27001 ISMS Controls:** A.5 Políticas de Seguridad, A.8 Protección de Datos y Redacción de PII, A.9 Control de Acceso de Menos Privilegios (Least-Privilege MCP), A.10 Criptografía.
  - **ISO 42001 AIMS Controls:** Cláusula 6.1 (AIIA - AI Impact Assessment), Cláusula 7.5 (Gobernanza de Datos para RAG), Cláusula 8.2 (Transparencia Algorítmica y Esquemas XML `<corporate_context>`), Cláusula 8.4 (Supervisión Humana HITL y Kill Switch).

---

## 🧠 Integración de Skills & Matriz de Referencia

Este ecosistema hace uso del catálogo de 817+ skills (basado en el corpus *Anthropic-Cybersecurity-Skills*) y los checklists maestros de [implicit/NIST_ISO_CHECKLISTS.md](file:///c:/Users/Nomack/Documents/workspace/agents/antigravity/dev/prompt-generator/implicit/NIST_ISO_CHECKLISTS.md). Los agentes están enrutados semánticamente mediante `brain/routing-matrix.json` utilizando referencias a IDs de técnicas (ej. `T1059`, `T1566`, `PR.DS-01`, `AIMS-RA-01`).

---
*Construido para operar bajo arquitectura Zero-Trust, protegiendo y defendiendo infraestructuras cloud, on-prem y redes de agentes autónomos de IA.*
