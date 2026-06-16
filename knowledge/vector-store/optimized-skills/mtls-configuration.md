---
name: mtls-configuration
description: Configure mutual TLS (mTLS) for zero-trust service-to-service communication. Use when implementing zero-trust networking, certificate management, or securing internal service communication.
metadata:
  model: inherit
---

<role>
You are an AI agent designed to execute this specific skill.
</role>

<task>
Use this skill when:
- Implementing zero-trust networking
- Securing service-to-service communication
- Certificate rotation and management
- Debugging TLS handshake issues
- Compliance requirements (PCI-DSS, HIPAA)
- Multi-cluster secure communication
</task>

<capabilities>

</capabilities>

<heuristics>
[INSTRUCTIONS]
- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

[BEST PRACTICES]
</heuristics>

<constraints>
[DO NOT USE THIS SKILL WHEN]
- The task is unrelated to mtls configuration
- You need a different domain or tool outside this scope

[TEMPLATE 2: ISTIO DESTINATION RULE FOR MTLS]
```yaml
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: default
  namespace: istio-system
spec:
  host: "*.local"
  trafficPolicy:
    tls:
      mode: ISTIO_MUTUAL
---

[CHECK DESTINATION RULES]
kubectl get destinationrule --all-namespaces
</constraints>

<format>
[TEMPLATES]


[TEMPLATE 1: ISTIO MTLS (STRICT MODE)]
```yaml

[TEMPLATE 2: ISTIO DESTINATION RULE FOR MTLS]
```yaml
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: default
  namespace: istio-system
spec:
  host: "*.local"
  trafficPolicy:
    tls:
      mode: ISTIO_MUTUAL
---

[TEMPLATE 3: CERT-MANAGER WITH ISTIO]
```yaml

[TEMPLATE 4: SPIFFE/SPIRE INTEGRATION]
```yaml

[TEMPLATE 5: LINKERD MTLS (AUTOMATIC)]
```yaml
</format>

