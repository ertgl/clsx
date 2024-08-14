__all__ = ["ConditionalExpressionTuple"]

from typing import (
    TYPE_CHECKING,
    TypeAlias,
)

from clsx.abc.conditions.condition import Condition


if TYPE_CHECKING:
    from clsx.abc.expressions.expression import Expression


ConditionalExpressionTuple: TypeAlias = tuple["Expression", Condition]
