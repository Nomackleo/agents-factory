---
name: linkerd-patterns
description: Implement Linkerd service mesh patterns for lightweight, security-focused service mesh deployments. Use when setting up Linkerd, configuring traffic policies, or implementing zero-trust networking with minimal overhead.
metadata:
  model: inherit
---

<role>
You are an AI agent designed to execute this specific skill.
</role>

<task>
Use this skill when:
- Setting up a lightweight service mesh
- Implementing automatic mTLS
- Configuring traffic splits for canary deployments
- Setting up service profiles for per-route metrics
- Implementing retries and timeouts
- Multi-cluster service mesh
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
- The task is unrelated to linkerd patterns
- You need a different domain or tool outside this scope
</constraints>

<format>
[TEMPLATES]


[TEMPLATE 1: MESH INSTALLATION]
```bash

[TEMPLATE 2: INJECT NAMESPACE]
```yaml

[TEMPLATE 3: SERVICE PROFILE WITH RETRIES]
```yaml
apiVersion: linkerd.io/v1alpha2
kind: ServiceProfile
metadata:
  name: my-service.my-namespace.svc.cluster.local
  namespace: my-namespace
spec:
  routes:
    - name: GET /api/users
      condition:
        method: GET
        pathRegex: /api/users
      responseClasses:
        - condition:
            status:
              min: 500
              max: 599
          isFailure: true
      isRetryable: true
    - name: POST /api/users
      condition:
        method: POST
        pathRegex: /api/users
      # POST not retryable by default
      isRetryable: false
    - name: GET /api/users/{id}
      condition:
        method: GET
        pathRegex: /api/users/[^/]+
      timeout: 5s
      isRetryable: true
  retryBudget:
    retryRatio: 0.2
    minRetriesPerSecond: 10
    ttl: 10s
```

[TEMPLATE 4: TRAFFIC SPLIT (CANARY)]
```yaml
apiVersion: split.smi-spec.io/v1alpha1
kind: TrafficSplit
metadata:
  name: my-service-canary
  namespace: my-namespace
spec:
  service: my-service
  backends:
    - service: my-service-stable
      weight: 900m  # 90%
    - service: my-service-canary
      weight: 100m  # 10%
```

[TEMPLATE 5: SERVER AUTHORIZATION POLICY]
```yaml

[TEMPLATE 6: HTTPROUTE FOR ADVANCED ROUTING]
```yaml
apiVersion: policy.linkerd.io/v1beta2
kind: HTTPRoute
metadata:
  name: my-route
  namespace: my-namespace
spec:
  parentRefs:
    - name: my-service
      kind: Service
      group: core
      port: 8080
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: /api/v2
        - headers:
            - name: x-api-version
              value: v2
      backendRefs:
        - name: my-service-v2
          port: 8080
    - matches:
        - path:
            type: PathPrefix
            value: /api
      backendRefs:
        - name: my-service-v1
          port: 8080
```

[TEMPLATE 7: MULTI-CLUSTER SETUP]
```bash
</format>

