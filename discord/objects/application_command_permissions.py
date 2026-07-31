from .._dataclass import dataclass
from ..enums import ApplicationCommandPermissionType
from ..snowflake import Snowflake


@dataclass
class ApplicationCommandPermissions:
  """Application command permissions allow you to enable or disable commands for specific users, roles, or channels within a guild."""

  id: Snowflake
  """ID of the role, user, or channel. It can also be a permission constant"""

  permission: bool
  """``True`` to allow, ``False`` to disallow"""

  type: ApplicationCommandPermissionType
  """Role, user, or channel"""