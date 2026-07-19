from ..snowflake import Snowflake
from ..utils import Nullable
from ._base import BaseObject
from .team_member import TeamMember


class Team(BaseObject):
  icon: Nullable[str]
  """Hash of the image of the team's icon"""

  id: Snowflake
  """Unique ID of the team"""

  members: list[TeamMember]
  """Members of the team"""

  name: str
  """Name of the team"""

  owner_user_id: Snowflake
  """User ID of the current team owner"""