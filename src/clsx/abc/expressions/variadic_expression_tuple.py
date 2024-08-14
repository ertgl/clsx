__all__ = ["VariadicExpressionTuple"]

from typing import (
    TYPE_CHECKING,
    TypeAlias,
)


if TYPE_CHECKING:
    from clsx.abc.expressions.expression import Expression


VariadicExpressionTuple: TypeAlias = tuple["Expression", ...]
