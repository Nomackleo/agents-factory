# Reglas de Seguridad e Aislamiento IAM Multi-Tenant — Google Workspace Ecosystem

> **Ámbito**: Universal (`agents-factory/google-workspace-ecosystem/`)  
> **Aplicación**: Obligatoria para todos los agentes, subagentes y llamadas a herramientas MCP que interactúen con cuentas de Google Workspace (desarrollo personal, Génesis Legal u otros clientes enterprise).  
> **Marcos Normativos**: ISO/IEC 27001:2022 (A.9 Gestión de Accesos), ISO/IEC 42001:2023 (Gobernanza de IA), SOC 2.

---

## 1. Principios Mandatorios de Aislamiento Multi-Tenant

1. **Aislamiento Estricto de Credenciales por Tenant**:
   - Cada cliente o entorno posee su propio subdirectorio cifrado de credenciales OAuth (`client_secret.json`, `tokens.json`).
   - Queda estrictamente PROHIBIDO reutilizar o compartir `access_token` o `refresh_token` entre distintos dominios o tenants corporativos.
   - Ruta base de almacén de credenciales: `c:\Users\Nomack\.gemini\antigravity-ide\mcp\credentials\<tenant_id>\`.

2. **Principio de Menor Privilegio (RBAC & OAuth Scopes)**:
   - Todo agente o herramienta MCP debe solicitar únicamente los OAuth Scopes mínimos indispensables para la tarea en curso (ej. `admin.directory.user.readonly` para auditoría, `admin.directory.user` para aprovisionamiento).
   - Queda prohibido el uso indiscriminado de scopes `https://mail.google.com/` a menos que sea requerido para una migración explícitamente aprobada por el operador HITL.

3. **Supervisión Humana Obligatoria (HITL - Human-in-the-Loop)**:
   - Operaciones de alto impacto (suspensión o eliminación de usuarios, modificación de registros MX autoritativos, eliminación de Shared Drives o cambios globales en políticas de seguridad) REQUIEREN confirmación previa explícita del operador humano.

4. **Protocolo Auto-Healing con Watchdog de Tokens**:
   - Todo cliente MCP debe conectarse con el script `python bin/watchdog_health_check.py`.
   - Ante errores HTTP 401 Unauthorized o 403 Forbidden por expiración de tokens, el sistema renovará automáticamente el `access_token` usando el `refresh_token` de `mcp_oauth_tokens.json` sin interrumpir la ejecución ni exponer credenciales en logs.

5. **Auditoría e Inmutabilidad de Logs**:
   - Toda llamada a API o mutación de configuración ejecutada por un agente debe registrarse en logs append-only indicando: `timestamp`, `agent_name`, `tenant_domain`, `action`, `parameters` y `result_status`.
