from .._dataclass import dataclass
from ..enums import MembershipState, TeamMemberRole
from ..snowflake import Snowflake
from .user import User


@dataclass
class TeamMember:
  @property
  def membership_state(self) -> MembershipState:
    """User's membership state on the team."""
    return MembershipState(self.__dict__["membership_state"])

  @property
  def role(self) -> TeamMemberRole:
    """Role of the team member."""
    return TeamMemberRole(self.__dict__["role"])

  @property
  def team_id(self) -> Snowflake:
    """ID of the parent team of which they are a member."""
    return Snowflake(self.__dict__["team_id"])

  @property
  def user(self) -> User:
    """Avatar, discriminator, ID, and username of the user."""
    return User(**self.__dict__["user"])