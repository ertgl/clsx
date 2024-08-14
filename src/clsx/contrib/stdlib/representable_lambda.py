__all__ = ["RepresentableLambda"]

from pprint import pformat
from typing import (
    Generic,
    TypeVar,
)


T = TypeVar("T")


class RepresentableLambda(Generic[T]):
    def __init__(
        self,
        value: T,
    ) -> None:
        self.value = value

    def __call__(self) -> T:
        return self.value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({pformat(self.value)})"
