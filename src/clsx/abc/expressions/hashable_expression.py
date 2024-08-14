__all__ = ["HashableExpression"]

from typing import (
    TypeAlias,
    Union,
)

from clsx.abc.class_names.class_name import ClassName
from clsx.abc.expressions.callable_expression import CallableExpression
from clsx.abc.expressions.expression_iterable import ExpressionIterable
from clsx.abc.expressions.expression_tuple import ExpressionTuple


HashableExpression: TypeAlias = Union[
    None,
    ClassName,
    ExpressionTuple,
    ExpressionIterable,
    CallableExpression,
]
