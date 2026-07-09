# Cybersecurity Ecosystem

Bienvenido al **Cybersecurity Ecosystem** de Antigravity. Este ecosistema consolida las capacidades ofensivas, defensivas y de cumplimiento de seguridad, albergando una fuerza laboral de agentes autónomos de seguridad entrenados en los marcos líderes de la industria (MITRE ATT&CK, NIST CSF, D3FEND, ATLAS, etc.).

## 🛡️ Guilds de Seguridad

Este ecosistema está organizado en gremios especializados ("Guilds") para segmentar las responsabilidades:

- **SOC Guild**: Analistas defensivos (L1/L2), respuesta a incidentes y caza de amenazas (Threat Hunting). Maestros en D3FEND y operaciones de contención.
- **Red Team Guild**: Operadores ofensivos, emulación de adversarios y expertos en MITRE ATT&CK. Capacidades desde reconocimiento inicial hasta exfiltración.
- **AppSec Guild**: Pruebas de seguridad en aplicaciones, auditoría de código, análisis de vulnerabilidades, y OWASP (incluyendo LLM/Agentic presets).
- **Compliance & Risk Guild**: Oficiales de cumplimiento, analistas de riesgo (NIST CSF, AI RMF) y auditores de infraestructura.

## 🧠 Integración de Skills

Este ecosistema hace uso del extenso catálogo de 817+ skills (basado en el corpus *Anthropic-Cybersecurity-Skills*). Los agentes de estas guilds están enrutados semánticamente mediante `brain/routing-matrix.json` utilizando referencias directas a IDs de técnicas (ej. `T1059`, `T1566`) para despachar el contexto correcto al agente correcto.

---
*Construido para operar en entornos zero-trust y defender/atacar infraestructuras cloud, on-prem y sistemas agénticos de IA.*
