from template.math.dataset import MathDataset

DATASETS = [
    MathDataset,
]

MATH_CONTEXT = MathDataset(seed=123).next()

CONTEXTS = {
    MathDataset: MATH_CONTEXT,
}

CONTEXT_FIELDS = {
    "title": str,
    "topic": str,
    "subtopic": str,
    "content": str,
    "internal_links": list,
    "external_links": list,
    "source": str,
    "tags": list,
    "extra": dict,
    "stats": dict,
}
