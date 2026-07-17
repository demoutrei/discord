from .._dataclass import dataclass


@dataclass
class DispatchEvent:
  def __class_getitem__(cls, name: str) -> type:
    if not isinstance(name, str):
      raise TypeError(f"name: Must be an instance of {str}; not {name.__class__}")
    name: str = name.strip().upper()
    if not name:
      raise ValueError(f"name: Must not be an empty string")
    ...