from .._dataclass import dataclass
from ..utils import Optional
from .install_params import InstallParams


@dataclass
class ApplicationIntegrationTypeConfiguration:
  oauth2_install_params: Optional[InstallParams]
  """Install params for each installation context's default in-app authorization link"""