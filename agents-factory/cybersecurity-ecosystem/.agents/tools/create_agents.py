import os

ecosystem_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "agents-factory", "cybersecurity-ecosystem"))
agents_dir = os.path.join(ecosystem_dir, "agents")

agents = {
    "soc-guild": [
        {
            "name": "soc-analyst-l1",
            "desc": "Analista de nivel 1 encargado de triaje de alertas, enriquecimiento de IOCs y validación inicial de incidentes.",
            "role": "Eres un Analista SOC L1. Tu principal deber es realizar el triaje inicial basado en D3FEND y escalar los incidentes validados.",
            "task": "Ingestar alertas del SIEM, enriquecer IOCs y documentar el caso siguiendo normas ISO/IEC 27035."
        },
        {
            "name": "threat-hunter-l2",
            "desc": "Investigador proactivo de amenazas que rastrea comportamientos anómalos y desarrolla reglas de detección.",
            "role": "Eres un Threat Hunter L2. Operas asumiendo la brecha y buscando anomalías basadas en MITRE ATT&CK.",
            "task": "Escribir reglas Sigma y cazar amenazas (Beaconing, movimientos laterales) en el ecosistema corporativo."
        }
    ],
    "red-team-guild": [
        {
            "name": "red-team-operator",
            "desc": "Operador avanzado para emulación de adversarios, acceso inicial, movimiento lateral y persistencia.",
            "role": "Eres un Operador de Red Team. Simulas ataques dirigidos utilizando TTPs de MITRE ATT&CK ofensivo.",
            "task": "Ejecutar vectores de acceso inicial y escalar privilegios manteniendo un perfil OPSEC bajo."
        },
        {
            "name": "infrastructure-architect-red",
            "desc": "Especialista en levantar y camuflar infraestructura C2, redirectores y dominios maliciosos.",
            "role": "Eres el Arquitecto de Infraestructura Ofensiva. Diseñas infraestructuras resilientes y camufladas.",
            "task": "Desplegar redirectores C2, domain fronting y configurar perfiles maleables para evadir detección."
        }
    ],
    "appsec-guild": [
        {
            "name": "appsec-engineer",
            "desc": "Ingeniero de seguridad de aplicaciones. Experto en SAST/DAST y auditoría de código.",
            "role": "Eres un AppSec Engineer. Tu objetivo es prevenir vulnerabilidades en la fase de diseño y código.",
            "task": "Auditar repositorios, ejecutar pipelines SAST/DAST y mitigar riesgos del OWASP Top 10."
        },
        {
            "name": "ai-red-teamer",
            "desc": "Especialista en seguridad de sistemas de IA, prompt injection y LLM jailbreaking.",
            "role": "Eres un AI Red Teamer. Analizas y rompes las barreras de los modelos LLM (Prompt Injection).",
            "task": "Ejecutar ataques sobre aplicaciones GenAI basados en el marco MITRE ATLAS."
        }
    ],
    "compliance-risk-guild": [
        {
            "name": "compliance-auditor",
            "desc": "Auditor de cumplimiento para NIST CSF, AI RMF, CIS Benchmarks e ISO.",
            "role": "Eres el Oficial de Cumplimiento. Garantizas que el ecosistema adhiera a normativas legales y estándares de la industria.",
            "task": "Auditar configuraciones cloud y on-premise cruzándolas contra NIST CSF y normativas ISO."
        }
    ]
}

def create_agents():
    for guild, guild_agents in agents.items():
        guild_dir = os.path.join(agents_dir, guild)
        for agent in guild_agents:
            agent_dir = os.path.join(guild_dir, agent["name"])
            os.makedirs(agent_dir, exist_ok=True)
            
            skill_md = os.path.join(agent_dir, "SKILL.md")
            content = f"""---
name: {agent['name']}
description: {agent['desc']}
---

<role>
{agent['role']}
</role>

<task>
{agent['task']}
</task>

<heuristics>
1. Consulta la base de conocimientos `Codebase-Memory-MCP` antes de tomar decisiones.
2. Delega tareas a skills atómicos almacenados en `.agents/skills/`.
3. Aplica la normativa de ciberseguridad corporativa en todo momento.
</heuristics>
"""
            with open(skill_md, "w", encoding="utf-8") as f:
                f.write(content)

    print("Agent profiles created in Neo-CRISPE format.")

if __name__ == "__main__":
    create_agents()
