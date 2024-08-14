__all__ = ["ClassNameParser"]

from clsx.abc import (
    ClassNameCharacterStream,
    ClassNameIterable,
)
from clsx.contrib.itertools import flatten_str


class ClassNameParser:
    @staticmethod
    def parse(
        stream: ClassNameCharacterStream,
    ) -> ClassNameIterable:
        buffer: list[str] = []
        for character in flatten_str(stream):
            if character.isspace():
                if buffer:
                    yield str.join("", buffer)
                    buffer = []
            else:
                buffer.append(character)
        if buffer:
            yield str.join("", buffer)
