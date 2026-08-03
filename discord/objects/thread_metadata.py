from .._dataclass import dataclass
from ..utils import ISO8601Timestamp, Optional


@dataclass
class ThreadMetadata:
  """Contains number of thread-specific channel fields that are not needed by other channel types."""

  archive_timestamp: ISO8601Timestamp
  """Timestamp when the thread's archive status was last changed, used for calculating recent activity."""

  archived: bool
  """Whether the thread is archived."""

  auto_archive_duration: int
  """The thread will stop showing in the channel list after :attr:`~.auto_archive_duration` minutes of inactivity, can be set to: 60, 1440, 4320, 10080."""

  create_timestamp: Optional[ISO8601Timestamp]
  """Timestamp when the thread was created; only populated for threads created after 2022-01-09."""

  invitable: Optional[bool]
  """Whether the non-moderators can add other non-moderators to a thread; only available on private threads."""

  locked: bool
  """Whether the thread is locked; when a thread is locked, only users with :attr:`~discord.flags.PermissionFlag.MANAGE_THREADS` can unarchive it."""