from template.math.task import MathTask
from template.tools.context import Context
from tests.fixtures.dataset import MATH_CONTEXT

TASKS = [
    MathTask,
]

CONTEXTS = {
    MathTask: MATH_CONTEXT,
}

TASK_FIELDS = {
    "name": str,
    "desc": str,
    "goal": str,
    "query": str,
    "topic": str,
    "subtopic": str,
    "tags": list,
    "context": Context,
    "reward_definition": list,
    "reference": str,
    # 'reward_threshold': float ,
    "penalty_definition": list,
    # 'criteria': str = ("",),
    "delimiter": str,
    "complete": bool,
    "static_reference": bool,
    "static_query": bool,
    "reference_system_prompt": str,
    "reference_prompt": str,
    "query_system_prompt": str,
    "query_prompt": str,
}
