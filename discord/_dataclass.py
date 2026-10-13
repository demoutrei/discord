from typing import Any


def is_dataclass(obj: type) -> bool:
  return getattr(obj, "__is_dataclass__", False)


def dataclass[T](cls: T) -> T:
  def __init__(self, **data) -> None:
    self.__dict__: dict[str, Any] = data

  cls.__init__ = __init__
  cls.__is_dataclass__ = True
  return cls