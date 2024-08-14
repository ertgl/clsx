__all__ = ["ClassNameCharacterStream"]

from typing import (
    TypeAlias,
    Union,
)

from clsx.abc.class_names.class_name_character_iterable import (
    ClassNameCharacterIterable,
)
from clsx.abc.class_names.nested_class_name_character_iterable import (
    NestedClassNameCharacterIterable,
)


ClassNameCharacterStream: TypeAlias = Union[
    ClassNameCharacterIterable,
    NestedClassNameCharacterIterable,
]
