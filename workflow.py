"""Template workflow module.

Only functions decorated with:

`@workflow.unary`, 
`@workflow.client_stream`,
`@workflow.server_stream`, or 
`@workflow.bi_di`

are built and exposed in generated workspace code.
"""

from per_datasets import workflow
from per_datasets.workflow import WorkflowStreamInput

@workflow.unary
def add(a: float, b: float) -> float:
    """Add two numbers.

    Example:
        >>> add(2.5, 3.7)
        6.2
    """
    return a + b


@workflow.input_stream
async def sum_stream(inputStream: WorkflowStreamInput[float], max_iters: int) -> float:
    """Consume an input stream and return one aggregate result.

    Runtime usage:
        >>> pds_session.workflows("<deployment_id>").sum_stream([[1.0], [2.0], [3.0]], max_iters=3)
        6.0
    """
    total = 0.0
    index = 0
    async for value in inputStream:
        total += float(value)
        index += 1
        if index >= int(max_iters):
            break
    return total