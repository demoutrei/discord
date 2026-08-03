from .._dataclass import dataclass
from ..enums import GuildScheduledEventEntityType, GuildScheduledEventPrivacyLevel, GuildScheduledEventStatus
from ..snowflake import Snowflake
from ..utils import ISO8601Timestamp, Nullable, Optional
from .guild_scheduled_event_entity_metadata import GuildScheduledEventEntityMetadata
from .guild_scheduled_event_recurrence_rule import GuildScheduledEventRecurrenceRule
from .user import User


@dataclass
class GuildScheduledEvent:
  channel_id: Nullable[Snowflake]
  """The channel ID in which the scheduled event will be hosted, or ``None`` if :attr:`~.entity_type` is :attr:`~discord.enums.GuildScheduledEventEntityType.EXTERNAL`."""

  creator: Optional[User]
  """The user that created the scheduled event."""

  creator_id: Optional[Nullable[Snowflake]]
  """The ID of the user that created the scheduled event.

  .. note::
      The :attr:`~.creator_id` will be null and :attr:`~.creator` will not be included for events created before October 25th, 2021, when the concept of :attr:`~.creator_id` was introduced and tracked.
  """
  
  description: Optional[Nullable[str]]
  """The description of the scheduled event (1-1000 characters)."""

  entity_id: Nullable[Snowflake]
  """The ID of an entity associated with a guild scheduled event."""

  entity_metadata: Nullable[GuildScheduledEventEntityMetadata]
  """Additional metadata for the guild scheduled event."""

  entity_type: GuildScheduledEventEntityType
  """The type of the scheduled event."""
  
  guild_id: Snowflake
  """The guild ID which the scheduled event belongs to."""
  
  id: Snowflake
  """The ID of the scheduled event."""

  image: Optional[Nullable[str]]
  """The cover image hash of the scheduled event."""

  name: str
  """The name of the scheduled event (1-100 characters)."""

  privacy_level: GuildScheduledEventPrivacyLevel
  """The privacy level of the scheduled event."""

  recurrence_rule: Nullable[GuildScheduledEventRecurrenceRule]
  """The definition for how often this event should recur."""

  scheduled_end_time: Nullable[ISO8601Timestamp]
  """The time the scheduled event will end, required if :attr:`~.entity_type` is :attr:`~discord.enums.GuildScheduledEventEntityType.EXTERNAL`."""

  scheduled_start_time: ISO8601Timestamp
  """The time the scheduled event will start."""

  status: GuildScheduledEventStatus
  """The status of the scheduled event."""

  user_count: Optional[int]
  """The number of users subscribed to the scheduled event."""