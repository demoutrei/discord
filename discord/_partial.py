from ._dataclass import is_dataclass
from .types import MISSING, Optional
from typing import Any, Self, Union


class PartialMeta(type):
  def __instancecheck__(cls, instance: object) -> bool:
    return cls.mro()[3] in instance.__class__.mro()[3:-1]


class Partial[T](metaclass = PartialMeta):
  def __class_getitem__(cls, item: T) -> type[Union[T, Self[T]]]:
    if not isinstance(item, (_ := type)):
      raise TypeError(f"item: Must be an instance of {_}; not {item.__class__}")
    if not is_dataclass(item): return item
    return type(f"Partial{item.__name__}", (cls, item))

  def __getattribute__(self, name: str, /) -> Optional[Any]:
    if not isinstance(name, (_ := str)):
      raise TypeError(f"name: Must be an instance of {_}; not {name.__class__}")
    if not name:
      raise ValueError(f"name: Must not be an empty string")
    properties: dict[str, property] = dict()
    for base_class in super().__getattribute__("__class__").mro()[3:-1][::-1]:
      if not is_dataclass(base_class): continue
      properties.update({ key: value for key, value in base_class.__dict__.items() if isinstance(value, property) })
    if name not in properties: return super().__getattribute__(name)
    if name not in self.__dict__: return MISSING
    return properties[name].fget(self)