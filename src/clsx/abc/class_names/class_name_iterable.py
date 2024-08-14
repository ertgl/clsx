__all__ = ["ClassNameIterable"]

from typing import Iterable, TypeAlias

from clsx.abc.class_names.class_name import ClassName


ClassNameIterable: TypeAlias = Iterable[ClassName]
