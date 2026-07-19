from ..snowflake import Snowflake
from ._base import BaseObject


class UnavailableGuild(BaseObject):
  """Represents an Offline Guild, or a Guild whose information has not been provided through Guild Create events during the Gateway connect"""

  id: Snowflake
  unavailable: bool