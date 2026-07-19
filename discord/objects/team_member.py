from ..enums import MembershipState, TeamMemberRole
from ..snowflake import Snowflake
from ._base import BaseObject
from .user import User


class TeamMember(BaseObject):
  membership_state: MembershipState
  """User's membership state on the team"""

  role: TeamMemberRole
  """Role of the team member"""

  team_id: Snowflake
  """ID of the parent team of which they are a member"""

  user: User
  """Avatar, discriminator, ID, and username of the user"""