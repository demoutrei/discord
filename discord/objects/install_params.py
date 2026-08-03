from .._dataclass import dataclass
from ..flags import PermissionFlags


@dataclass
class InstallParams:
  permissions: PermissionFlags
  """Permissions to request for the bot role"""
  
  scopes: list[str]
  """Scopes to add the application to the server with"""