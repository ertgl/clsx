__all__ = ["NestedStrIterable"]

from typing import (
    Iterable,
    TypeAlias,
    Union,
)


NestedStrIterable: TypeAlias = Union[
    str,
    Iterable[str],
    Iterable["NestedStrIterable"],
]
