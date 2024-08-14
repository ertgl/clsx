__all__ = ["ExpressionTuple"]

from typing import (
    TypeAlias,
    Union,
)

from clsx.abc.expressions.conditional_expression_tuple import ConditionalExpressionTuple
from clsx.abc.expressions.variadic_expression_tuple import VariadicExpressionTuple


ExpressionTuple: TypeAlias = Union[
    ConditionalExpressionTuple,
    VariadicExpressionTuple,
]
