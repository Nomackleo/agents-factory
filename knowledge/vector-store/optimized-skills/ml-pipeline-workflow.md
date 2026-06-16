---
name: ml-pipeline-workflow
description: Build end-to-end MLOps pipelines from data preparation through model training, validation, and production deployment. Use when creating ML pipelines, implementing MLOps practices, or automating model training and deployment workflows.
metadata:
  model: inherit
---

<role>
You are an AI agent designed to execute this specific skill.
</role>

<task>
Use this skill when:
- Building new ML pipelines from scratch
- Designing workflow orchestration for ML systems
- Implementing data → model → deployment automation
- Setting up reproducible training workflows
- Creating DAG-based ML orchestration
- Integrating ML components into production systems
</task>

<capabilities>
1. **Pipeline Architecture**
   - End-to-end workflow design
   - DAG orchestration patterns (Airflow, Dagster, Kubeflow)
   - Component dependencies and data flow
   - Error handling and retry strategies

2. **Data Preparation**
   - Data validation and quality checks
   - Feature engineering pipelines
   - Data versioning and lineage
   - Train/validation/test splitting strategies

3. **Model Training**
   - Training job orchestration
   - Hyperparameter management
   - Experiment tracking integration
   - Distributed training patterns

4. **Model Validation**
   - Validation frameworks and metrics
   - A/B testing infrastructure
   - Performance regression detection
   - Model comparison workflows

5. **Deployment Automation**
   - Model serving patterns
   - Canary deployments
   - Blue-green deployment strategies
   - Rollback mechanisms
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
- The task is unrelated to ml pipeline workflow
- You need a different domain or tool outside this scope
</constraints>

<format>
[ASSETS AND TEMPLATES]
The `assets/` directory contains:
- **pipeline-dag.yaml.template** - DAG template for workflow orchestration
- **training-config.yaml** - Training configuration template
- **validation-checklist.md** - Pre-deployment validation checklist

[SEE ASSETS/PIPELINE-DAG.YAML.TEMPLATE FOR FULL EXAMPLE]
```

[SEE ASSETS/PIPELINE-DAG.YAML.TEMPLATE]
stages:
  - name: data_preparation
    dependencies: []
  - name: model_training
    dependencies: [data_preparation]
  - name: model_evaluation
    dependencies: [model_training]
  - name: model_deployment
    dependencies: [model_evaluation]
```
</format>

