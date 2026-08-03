from .._dataclass import dataclass
from ..objects import ThreadMember
from ..snowflake import Snowflake
from ..utils import Optional


@dataclass
class ThreadMembersUpdateEvent:
  added_members: Optional[list[ThreadMember]]
  """Users who were added to the thread.

  .. note::
      In this gateway event, the thread member objects will also include the guild member and nullable presence objects for each added thread member.
  """
  
  guild_id: Snowflake
  """ID of the guild."""
  
  id: Snowflake
  """ID of the thread."""

  member_count: int
  """Approximate number of members in the thread, capped at 50."""

  removed_member_ids: Optional[list[Snowflake]]
  """ID of the users who were removed from the thread."""