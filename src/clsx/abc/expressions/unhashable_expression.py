__all__ = ["UnhashableExpression"]

from typing import (
    TYPE_CHECKING,
    TypeAlias,
    Union,
)

from clsx.abc.expressions.expression_list import ExpressionList
from clsx.abc.expressions.expression_set import ExpressionSet


if TYPE_CHECKING:
    from clsx.abc.expressions.dict_expression import DictExpression


UnhashableExpression: TypeAlias = Union[
    "DictExpression",
    ExpressionList,
    ExpressionSet,
]
