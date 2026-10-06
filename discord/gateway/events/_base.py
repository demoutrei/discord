from ...types import MISSING, Optional
from ..._dataclass import dataclass


@dataclass
class DispatchEvent:
  def __class_getitem__(cls, name: str, /) -> Optional[type]:
    if not isinstance(name, str):
      raise TypeError(f"name: Must be an instance of {str}; not {name.__class__}")
    name: str = name.strip()
    if not name:
      raise ValueError(f"name: Must not be an empty string")
    event_cls: Optional[type] = MISSING
    match name.upper():
      case "READY": from .ready import ReadyEvent as event_cls
    return event_cls