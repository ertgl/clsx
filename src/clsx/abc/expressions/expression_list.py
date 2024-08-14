__all__ = ["ExpressionList"]

from typing import (
    TYPE_CHECKING,
    TypeAlias,
)


if TYPE_CHECKING:
    from clsx.abc.expressions.expression import Expression


ExpressionList: TypeAlias = list["Expression"]
