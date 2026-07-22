from ..enums import ApplicationCommandPermissionType
from ..snowflake import Snowflake
from ._base import BaseObject


class ApplicationCommandPermissions(BaseObject):
  """Application command permissions allow you to enable or disable commands for specific users, roles, or channels within a guild."""

  id: Snowflake
  """ID of the role, user, or channel. It can also be a permission constant"""

  permission: bool
  """``True`` to allow, ``False`` to disallow"""

  type: ApplicationCommandPermissionType
  """Role, user, or channel"""