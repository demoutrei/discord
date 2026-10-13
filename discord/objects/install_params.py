from .._dataclass import dataclass
from ..flags import PermissionFlags


@dataclass
class InstallParams:
  @property
  def permissions(self) -> PermissionFlags:
    """Permissions to request for the bot role."""
    return PermissionFlags(int(self.__dict__["permissions"]))
  
  @property
  def scopes(self) -> list[str]:
    """Scopes to add the application to the server with."""
    return self.__dict__["scopes"]