from .._dataclass import dataclass
from ..flags import PermissionFlag


@dataclass
class InstallParams:
  permissions: PermissionFlag
  """Permissions to request for the bot role"""
  
  scopes: list[str]
  """Scopes to add the application to the server with"""