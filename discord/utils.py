__all__ = (
  "MISSING",
  "Nullable",
  "Optional"
)


from typing import Any, Literal, Union


class _MissingSentinel:
  __slots__: tuple = tuple()
  __instance: Union[Self, None] = None

  def __bool__(self) -> Literal[False]:
    return False

  def __eq__(self, _: Any) -> Literal[False]:
    return False

  def __hash__(self) -> Literal[0]:
    return 0

  def __new__(cls: type[Self]) -> Self:
    if cls.__instance is None:
      instance: Self = super().__new__(cls)
      cls.__instance: Self = instance
    return cls.__instance

  def __repr__(self) -> Literal["..."]:
    return "..."


type ISO8601Timestamp = str
"""Represents an ISO8601 timestamp"""

type Match[V, T] = tuple[str, tuple[V, T], ...]
"""Represents a match-case data type"""

MISSING: _MissingSentinel = _MissingSentinel()
"""Represents a singleton MISSING sentinel"""

type Nullable[T] = Union[T, None]
"""Represents a nullable data type"""

type Optional[T] = Union[T, MISSING]
"""Represents an optional data type"""