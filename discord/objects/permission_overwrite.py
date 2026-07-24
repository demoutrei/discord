from ..flags import PermissionFlag
from ..snowflake import Snowflake
from ._base import BaseObject


class PermissionOverwrite(BaseObject):
  allow: PermissionFlag
  """Permission bit set to allow"""

  deny: PermissionFlag
  """Permission bit set to deny"""
  
  id: Snowflake
  """Role or user ID"""

  type: int
  """Either ``0`` (role) or ``1`` (member)"""