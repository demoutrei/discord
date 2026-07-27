from ..objects import Channel, ThreadMember
from ..snowflake import Snowflake
from ..utils import Optional
from ._base import DispatchEvent


class ThreadListSyncEvent(DispatchEvent):
  channel_ids: Optional[list[Snowflake]]
  """Parent channel IDs whose threads are being synced. If omitted, then threads were synced for the entire guild. This array may contain channel IDs that have no active threads as well, so you know to clear that data."""
  
  guild_id: Snowflake
  """ID of the guild."""

  members: list[ThreadMember]
  """All thread member objects from the synced threads for the current user, indicating which threads the current user has been added to."""

  threads: list[Channel]
  """All active threads in the given channels that the current user can access."""