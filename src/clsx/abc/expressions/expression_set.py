__all__ = ["ExpressionSet"]

from typing import TypeAlias

from clsx.abc.expressions.hashable_expression import HashableExpression


ExpressionSet: TypeAlias = set[HashableExpression]
