__all__ = ["ExpressionIterable"]

from typing import (
    TYPE_CHECKING,
    Iterable,
    TypeAlias,
)


if TYPE_CHECKING:
    from clsx.abc.expressions.expression import Expression


ExpressionIterable: TypeAlias = Iterable["Expression"]
