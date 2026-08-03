from .._dataclass import dataclass
from ..flags import PermissionFlags
from ..snowflake import Snowflake


@dataclass
class PermissionOverwrite:
  allow: PermissionFlags
  """Permission bit set to allow"""

  deny: PermissionFlags
  """Permission bit set to deny"""
  
  id: Snowflake
  """Role or user ID"""

  type: int
  """Either ``0`` (role) or ``1`` (member)"""