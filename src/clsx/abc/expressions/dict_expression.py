__all__ = ["DictExpression"]

from typing import TypeAlias

from clsx.abc.conditions.condition import Condition
from clsx.abc.expressions.hashable_expression import HashableExpression


DictExpression: TypeAlias = dict[HashableExpression, Condition]
