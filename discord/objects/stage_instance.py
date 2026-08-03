from .._dataclass import dataclass
from ..enums import StageInstancePrivacyLevel
from ..snowflake import Snowflake
from ..utils import Nullable


@dataclass
class StageInstance:
  channel_id: Snowflake
  """The ID of the associated Stage channel."""

  discoverable_disabled: bool
  """Whether or not Stage Discovery is disabled (deprecated)."""
  
  guild_id: Snowflake
  """The guild ID of the associated Stage channel."""

  guild_scheduled_event_id: Nullable[Snowflake]
  """The ID of the scheduled event for this Stage instance."""
  
  id: Snowflake
  """The ID of this Stage instance."""

  privacy_level: StageInstancePrivacyLevel
  """The privacy level of the Stage instance."""

  topic: str
  """The topic of the Stage instance (1-120 characters)."""