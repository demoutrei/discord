from .._dataclass import dataclass
from ..snowflake import Snowflake
from ..utils import Nullable
from .team_member import TeamMember


@dataclass
class Team:
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