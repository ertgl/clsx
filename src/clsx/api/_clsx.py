__all__ = ["clsx"]

from typing import (
    Any,
    overload,
)

from clsx.abc import (
    ClassName,
    Condition,
    Expression,
)
from clsx.contrib.itertools import dedup
from clsx.evaluation import ExpressionEvaluator


@overload
def clsx(
    *expressions: Expression,
) -> ClassName: ...


@overload
def clsx(
    expression: Expression,
    condition: Condition,
    /,
) -> ClassName: ...


def clsx(
    *expressions: Any,
) -> ClassName:
    return " ".join(
        dedup(
            ExpressionEvaluator.evaluate(
                expressions,
            ),
        ),
    )
