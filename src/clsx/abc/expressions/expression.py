__all__ = ["Expression"]

from typing import (
    TypeAlias,
    Union,
)

from clsx.abc.expressions.hashable_expression import HashableExpression
from clsx.abc.expressions.unhashable_expression import UnhashableExpression


Expression: TypeAlias = Union[
    HashableExpression,
    UnhashableExpression,
]
