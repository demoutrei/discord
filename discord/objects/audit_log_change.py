from .._dataclass import dataclass
from ..utils import Optional
from typing import Any


@dataclass
class AuditLogChange:
  """
  .. hint::
      If :attr:`~.new_value` is not present in the change object while :attr:`~.old_value` is, it indicates that the property has been reset or set to ``None``. If :attr:`~.old_value` isn't included, it indicated that the property was previously ``None``.
  """

  key: str
  """Name of the changed entity, with a few exceptions."""

  new_value: Optional[Any]
  """New value of the key."""

  old_value: Optional[Any]
  """Old value of the key."""