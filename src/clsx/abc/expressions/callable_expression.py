__all__ = ["CallableExpression"]

from typing import (
    TYPE_CHECKING,
    Callable,
    TypeAlias,
)


if TYPE_CHECKING:
    from clsx.abc.expressions.expression import Expression


CallableExpression: TypeAlias = Callable[[], "Expression"]
