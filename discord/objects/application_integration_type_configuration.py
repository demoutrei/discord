from ..utils import Optional
from ._base import BaseObject
from .install_params import InstallParams


class ApplicationIntegrationTypeConfiguration(BaseObject):
  oauth2_install_params: Optional[InstallParams]
  """Install params for each installation context's default in-app authorization link"""