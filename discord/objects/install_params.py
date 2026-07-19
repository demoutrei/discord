from ..flags import PermissionFlag
from ._base import BaseObject


class InstallParams(BaseObject):
  permissions: PermissionFlag
  """Permissions to request for the bot role"""
  
  scopes: list[str]
  """Scopes to add the application to the server with"""