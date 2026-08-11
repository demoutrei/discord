from .flags import PermissionFlags
from .objects.components._base import Component, LabelChildComponent
from .snowflake import Snowflake
from .utils import ISO8601Timestamp, Match, MISSING, Nullable, Optional
from annotationlib import get_annotations
from datetime import datetime
from enum import Enum
from types import GenericAlias
from typing import Any, Self, Union


def is_dataclass(obj: type) -> bool:
  return getattr(obj, "__is_dataclass__", False)


def dataclass[T](cls: T) -> T:
  def __init__(self, **kwargs) -> None:
    for name, annotation in get_annotations(self.__class__).items():
      value: Optional[Nullable[Any]] = self.__parse(annotation, kwargs.get(name, ...), data = kwargs)
      setattr(self, name, value)

  def __init_subclass__(subclass, **kwargs) -> None:
    super(subclass).__init_subclass__(**kwargs)
    if subclass in (Component, LabelChildComponent):
      subclass.__new__ = object.__new__
    for base in subclass.__bases__:
      subclass.__annotations__.update(get_annotations(base))

  def __parse(self, annotation: Union[GenericAlias, type, Self[T]], /, value: Union[Any, Ellipsis], *, data: dict[str, Any]) -> Optional[Nullable[T]]:
    if isinstance(annotation, GenericAlias):
      if annotation.__origin__ is dict: return self.__parse_dict(annotation.__args__[0], annotation.__args__[1], value, data = data)
      if annotation.__origin__ is list: return self.__parse_list(annotation.__args__[0], value, data = data)
      if annotation.__origin__ is Match: return self.__parse_match(annotation.__args__[1:], annotation.__args__[0], value, data = data)
      if annotation.__origin__ is Nullable: return self.__parse_nullable(annotation.__args__[0], value, data = data)
      if annotation.__origin__ is Optional: return self.__parse_optional(annotation.__args__[0], value, data = data)
    if annotation in (Component, LabelChildComponent): return annotation(**value)
    if is_dataclass(annotation): return self.__parse_dataclass(annotation, value, data = data)
    if annotation is Snowflake and value not in (MISSING, None, Ellipsis): return Snowflake(value)
    if issubclass(annotation, Enum) and value not in (MISSING, None, Ellipsis):
      if annotation is PermissionFlags:
        value: int = int(value)
      return annotation(value)
    if annotation is ISO8601Timestamp and value not in (MISSING, None, Ellipsis):
      return datetime.fromisoformat(value)
    if value is Ellipsis: return MISSING
    return value

  def __parse_dataclass(self, annotation: Union[Self[T], type], value: Union[dict[str, Any], Ellipsis], *, data: dict[str, Any]) -> Optional[T]:
    if value is Ellipsis: return MISSING
    return annotation(**value)

  def __parse_dict(self, key_annotation: Union[GenericAlias, Self[T], type], value_annotation: Union[GenericAlias, Self[T], type], /, values: Union[dict[str, Any], Ellipsis], *, data: dict[str, Any]) -> Optional[dict[str, T]]:
    if values is Ellipsis: return MISSING
    return {self.__parse(key_annotation, key, data = data): self.__parse(value_annotation, value, data = data) for key, value in values.items()}

  def __parse_match(self, annotations: tuple[tuple[Union[int, str], Union[GenericAlias, Self[T], type]], ...], field: str, value: Union[Any, Ellipsis], *, data: dict[str, Any]) -> Optional[T]:
    if value is Ellipsis: return MISSING
    IS_SELF: bool = False
    if field.startswith("self."):
      IS_SELF: bool = True
      field: str = field[5:]
    field_value = (data if IS_SELF else value).get(field, ...)
    for case_value, case_cls in annotations:
      if case_value == field_value:
        return self.__parse(case_cls, value, data = data)

  def __parse_list(self, annotation: Union[GenericAlias, Self[T], type], values: Union[list[Any], Ellipsis], *, data: dict[str, Any]) -> Optional[list[T]]:
    if values is Ellipsis: return MISSING
    return [self.__parse(annotation, value, data = data) for value in values]

  def __parse_nullable(self, annotation: Union[GenericAlias, type, Self[T]], value: Union[Any, Ellipsis], *, data: dict[str, Any]) -> Nullable[T]:
    if value is Ellipsis: return MISSING
    if value is None: return None
    return self.__parse(annotation, value, data = data)

  def __parse_optional(self, annotation: Union[GenericAlias, type, Self[T]], value: Union[Any, Ellipsis], *, data: dict[str, Any]) -> Optional[T]:
    if value is Ellipsis: return MISSING
    return self.__parse(annotation, value, data = data)

  def __setattr__(self, name: str, value: Any) -> None:
    if name not in self.__dict__:
      object.__setattr__(self, name, value)

  def _to_dict(self) -> dict[str, Any]:
    data: dict[str, Any] = dict()
    for name, annotation in get_annotations(self.__class__).items():
      value: Optional[Any] = getattr(self, name, MISSING)
      if value is MISSING: continue
      if isinstance(value, list):
        value: list[Any] = [(item._to_dict() if is_dataclass(item) else item) for item in value]
      elif isinstance(value, dict):
        value: dict[str, Any] = {k: (v._to_dict() if is_dataclass(v) else v) for k, v in value.items()}
      elif is_dataclass(value.__class__):
        value: dict[str, Any] = value._to_dict()
      elif isinstance(value, Enum):
        if isinstance(value, PermissionFlags):
          value: str = str(value.value)
        else:
          value: Any = value.value
      elif isinstance(value, Snowflake):
        value: str = str(value)
      elif isinstance(value, datetime):
        value: str = value.isoformat()
      data[name]: Any = value
    return data

  def update(self, data: T) -> Self[T]:
    """:meta private:"""
    for name in get_annotations(self.__class__).keys():
      value: Any = getattr(data, name, MISSING)
      if value is MISSING: continue
      setattr(self, name, value)

  cls.__init__ = __init__
  cls.__init_subclass__ = classmethod(__init_subclass__)
  cls.__is_dataclass__ = True
  cls.__parse = __parse
  cls.__parse_dataclass = __parse_dataclass
  cls.__parse_dict = __parse_dict
  cls.__parse_list = __parse_list
  cls.__parse_match = __parse_match
  cls.__parse_nullable = __parse_nullable
  cls.__parse_optional = __parse_optional
  cls.__setattr__ = __setattr__
  cls._to_dict = _to_dict
  cls.update = update
  return cls