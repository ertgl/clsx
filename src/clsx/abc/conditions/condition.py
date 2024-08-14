__all__ = ["Condition"]

from typing import (
    TypeAlias,
    Union,
)

from clsx.abc.conditions.bool_condition import BoolCondition
from clsx.abc.conditions.callable_condition import CallableCondition


Condition: TypeAlias = Union[
    BoolCondition,
    CallableCondition,
]
