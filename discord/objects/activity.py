from .._dataclass import dataclass
from ..enums import ActivityType, StatusDisplayType
from ..flags import ActivityFlags
from ..utils import Nullable, Optional
from .activity_assets import ActivityAssets
from .activity_button import ActivityButton
from .activity_party import ActivityParty
from .activity_secrets import ActivitySecrets
from .activity_timestamps import ActivityTimestamps
from .emoji import Emoji


@dataclass
class Activity:
  """
  .. hint::
      Bot users are only able to set :attr:`~.name`, :attr:`~.state`, :attr:`~.type`, and :attr:`~.url`.
  """

  application_id: Optional[Snowflake]
  """Application ID for the game."""

  assets: Optional[ActivityAssets]
  """Images for the presence and their hover texts."""

  buttons: Optional[list[ActivityButton]]
  """Custom buttons shown in the Rich Presence (max 2)."""

  created_at: int
  """Unix timestamp (in milliseconds) of when the activity was added to the user's session."""

  details: Optional[Nullable[str]]
  """What the player is currently doing."""

  details_url: Optional[Nullable[str]]
  """URL that is linked when clicking on the details text."""

  emoji: Optional[Nullable[Emoji]]
  """Emoji used for a custom status."""

  flags: Optional[ActivityFlags]
  """Activity flags ``OR``d together, describes what the payload includes."""

  instance: Optional[bool]
  """Whether or not the activity is an instanced game session."""

  name: str
  """Activity's name."""

  party: Optional[ActivityParty]
  """Information for the current party of the player."""

  secrets: Optional[ActivitySecrets]
  """Secrets for Rich Presence joining and spectating."""

  state: Optional[Nullable[str]]
  """User's current party status, or text used for custom status."""

  state_url: Optional[Nullable[str]]
  """URl that is linked when clicking on the state text."""

  status_display_type: Optional[Nullable[StatusDisplayType]]
  """Status display type; controls which field is displayed in the user's status text in the member list."""

  timestamps: Optional[ActivityTimestamps]
  """Unix timestamps for start and/or end of the game."""

  type: ActivityType
  """Activity type."""

  url: Optional[Nullable[str]]
  """Stream URL, is validated when :attr:`~.type` is :attr:`~discord.enums.ActivityType.STREAMING`."""