from ..events import PresenceUpdateEvent
from .._dataclass import dataclass
from ..snowflake import Snowflake
from ..utils import ISO8601Timestamp, Nullable, Optional
from .guild_member import GuildMember


@dataclass
class ThreadMember:
  """Contains information about a user that has joined a thread."""

  flags: int
  """Any user-thread settings, currently only used for notifications"""

  id: Optional[Snowflake]
  """ID of the thread.

  .. note::
      Omitted on the member sent within each thread in the ``GUILD_CREATE`` event.
  """

  join_timestamp: ISO8601Timestamp
  """Time the user last joined the thread"""

  member: Optional[GuildMember]
  """Additional information about the user.

  .. important::
      Only present when ``with_member`` is set to ``True`` when calling :meth:`~discord._http.HTTP.list_thread_members` or :meth:`~discord._http.HTTP.get_thread_member`.
  """

  presence: Optional[Nullable[PresenceUpdateEvent]]

  user_id: Optional[Snowflake]
  """ID of the user.

  .. note::
      Omitted on the member sent within each thread in the ``GUILD_CREATE`` event.
  """