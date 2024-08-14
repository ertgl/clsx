__all__ = ["CallableCondition"]

from typing import (
    TYPE_CHECKING,
    Callable,
    TypeAlias,
)


if TYPE_CHECKING:
    from clsx.abc.conditions.condition import Condition


CallableCondition: TypeAlias = Callable[[], "Condition"]
