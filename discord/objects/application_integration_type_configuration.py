from .._dataclass import dataclass
from ..types import MISSING, Optional
from .install_params import InstallParams


@dataclass
class ApplicationIntegrationTypeConfiguration:
  @property
  def oauth2_install_params(self) -> Optional[InstallParams]:
    """Install params for each installation context's default in-app authorization link."""
    if (data := self.__dict__.get("oauth2_install_params", MISSING)) is MISSING: return data
    return InstallParams(**data)