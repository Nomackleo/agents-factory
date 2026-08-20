"""
Google ADK Multi-Agent Workflow Templates Reference
Autor: Leonel Salcedo / Nomack Studio & Antigravity

Implementaciones ejecutables de referencia de los 4 patrones maestros de Google ADK:
1. Coordinator & Dispatcher
2. Sequential Chain
3. Parallel Scatter-Gather
4. Loop (Evaluator-Optimizer)
"""

from typing import List, Dict, Any, Optional, Callable
import json

class MockAgentContext:
    def __init__(self, state: Optional[Dict[str, Any]] = None):
        self.state = state or {}
        self.history: List[Dict[str, Any]] = []

    def set(self, key: str, value: Any):
        self.state[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        return self.state.get(key, default)


class ADKAgentDescriptor:
    def __init__(
        self,
        name: str,
        description: str,
        instruction: str,
        model: str = "gemini-1.5-pro",
        tools: Optional[List[Callable]] = None,
        sub_agents: Optional[List['ADKAgentDescriptor']] = None
    ):
        self.name = name
        self.description = description
        self.instruction = instruction
        self.model = model
        self.tools = tools or []
        self.sub_agents = sub_agents or []

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "instruction": self.instruction,
            "model": self.model,
            "tools_count": len(self.tools),
            "sub_agents": [sa.name for sa in self.sub_agents]
        }


class ADKWorkflowBuilder:
    """
    Constructor de Workflows Multi-Agente compatibles con la especificación Google ADK.
    """

    @staticmethod
    def build_coordinator_workflow(coordinator_name: str, instruction: str, specialists: List[ADKAgentDescriptor]) -> ADKAgentDescriptor:
        return ADKAgentDescriptor(
            name=coordinator_name,
            description="Coordinador central con enrutamiento dinámico a especialistas.",
            instruction=instruction,
            sub_agents=specialists
        )

    @staticmethod
    def build_sequential_pipeline(pipeline_name: str, steps: List[ADKAgentDescriptor]) -> Dict[str, Any]:
        return {
            "type": "SequentialAgent",
            "name": pipeline_name,
            "execution_order": [step.name for step in steps],
            "step_count": len(steps)
        }

    @staticmethod
    def build_parallel_scatter_gather(workflow_name: str, workers: List[ADKAgentDescriptor], aggregator_name: str) -> Dict[str, Any]:
        return {
            "type": "ParallelAgent",
            "name": workflow_name,
            "parallel_workers": [w.name for w in workers],
            "aggregator": aggregator_name
        }

    @staticmethod
    def build_evaluator_optimizer_loop(generator: ADKAgentDescriptor, evaluator: ADKAgentDescriptor, threshold_score: float = 0.85, max_iter: int = 5) -> Dict[str, Any]:
        return {
            "type": "LoopAgent",
            "generator": generator.name,
            "evaluator": evaluator.name,
            "stopping_condition": f"score >= {threshold_score}",
            "max_iterations": max_iter
        }


if __name__ == "__main__":
    print("[Google ADK Templates] Módulo de plantillas de orquestación multi-agente listo.")
