__all__ = ["dedup"]

from typing import (
    Iterable,
    TypeVar,
)


T = TypeVar("T")


def dedup(iterable: Iterable[T]) -> Iterable[T]:
    seen = set()
    for value in iterable:
        if value not in seen:
            yield value
            seen.add(value)
