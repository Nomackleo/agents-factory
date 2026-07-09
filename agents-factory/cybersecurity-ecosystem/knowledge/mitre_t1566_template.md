# Plantilla de Documentación Operativa: MITRE ATT&CK (Ejemplo T1566 - Phishing)

**Propósito (WHY):** Servir como *Ground Truth* para el *Red Team Guild* y *SOC Guild* sobre cómo documentar técnicas de ataque y simulaciones, evitando sesgos narrativos y alucinaciones dramáticas.

**Audiencia (WHO):** Analistas de Seguridad, Herramientas RAG del Ecosistema.

## Estructura Exegética Obligatoria (WHAT)

Todo reporte o simulación de ataque debe adherirse a esta estructura estricta:

```markdown
# [ID MITRE] - [Nombre de la Técnica]

## 1. Definición Técnica
- **Descripción Exacta:** Qué vector explota y qué acceso busca obtener.
- **Precondiciones:** Qué accesos o fallos deben existir previamente.

## 2. Ejecución (Simulación)
- **Vector de Entrada:** (Ej. Correo electrónico, enlace web).
- **Carga Útil (Payload):** Descripción estructurada (No usar payloads reales o ofuscados en la documentación, describir el tipo de payload. Ej: "Archivo macro habilitado .docm").
- **Táctica Asociada:** (Ej. Initial Access).

## 3. Artefactos y Trazabilidad (Detección)
- **Indicadores de Compromiso (IoCs) Esperados:**
  - Registros de Eventos Windows (Ej. Event ID 4688).
  - Tráfico de Red anómalo.
- **Reglas de Detección (Sigma/YARA):** Referencia a la lógica de detección, no al código duro, a menos que sea un repositorio de reglas aislado.
```

## Prevención de Ruido (Heurística de Redacción)
- **Control de Creatividad:** El ecosistema de ciberseguridad NO utiliza narrativas. Un ataque no es "una astuta maniobra del hacker", es "la explotación de la vulnerabilidad CVE-XXXX".
- **Objetividad:** Mantener un tono analítico e investigativo (*Exegético*). No calificar la seguridad de la víctima como "pobre" o "excelente", usar métricas DORA/SPACE y cumplimiento SOC 2 para evaluar el impacto real.
