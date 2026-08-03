from .._dataclass import dataclass
from ..snowflake import Snowflake


@dataclass
class UnavailableGuild:
  """Represents an Offline Guild, or a Guild whose information has not been provided through Guild Create events during the Gateway connect"""

  id: Snowflake
  unavailable: bool