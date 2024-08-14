__all__ = ["flatten_str"]

from typing import Iterable

from clsx.contrib.itertools.abc import NestedStrIterable


def flatten_str(iterable: NestedStrIterable) -> Iterable[str]:
    for value in iterable:
        if isinstance(value, str) and len(value) == 1:
            yield value
        else:
            yield from flatten_str(value)
