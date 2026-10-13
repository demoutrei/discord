from .._dataclass import dataclass
from ..snowflake import Snowflake
from ..types import Nullable
from .team_member import TeamMember


@dataclass
class Team:
  @property
  def icon(self) -> Nullable[str]:
    """Hash of the image of the team's icon."""
    return self.__dict__["icon"]

  @property
  def id(self) -> Snowflake:
    """Unique ID of the team."""
    return Snowflake(self.__dict__["id"])

  @property
  def members(self) -> list[TeamMember]:
    """Members of the team."""
    return [TeamMember(**data) for data in self.__dict__["members"]]

  @property
  def name(self) -> str:
    """Name of the team."""
    return self.__dict__["name"]

  @property
  def owner_user_id(self) -> Snowflake:
    """User ID of the current team owner."""
    return Snowflake(self.__dict__["owner_user_id"])