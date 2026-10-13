from .._dataclass import dataclass
from ..enums import ActivityType, StatusDisplayType
from ..flags import ActivityFlags
from ..snowflake import Snowflake
from ..types import MISSING, Nullable, Optional
from .activity_assets import ActivityAssets
from .activity_button import ActivityButton
from .activity_emoji import ActivityEmoji
from .activity_party import ActivityParty
from .activity_secrets import ActivitySecrets
from .activity_timestamps import ActivityTimestamps
from typing import Union


@dataclass
class Activity:
  """
  .. note::

      Bot users are only able to set :attr:`Activity.name <.name>`, :attr:`Activity.state <.state>`, :attr:`Activity.type <.type>`, and :attr:`Activity.url <.url>`.
  """
  
  @property
  def application_id(self) -> Optional[Snowflake]:
    """Application ID for the game."""
    if (data := self.__dict__.get("application_id", MISSING)) is MISSING: return data
    return Snowflake(data)
  
  @property
  def assets(self) -> Optional[ActivityAssets]:
    """Images for the presence and their hover texts."""
    if (data := self.__dict__.get("assets", MISSING)) is MISSING: return data
    return ActivityAssets(**data)

  @property
  def buttons(self) -> Optional[list[Union[ActivityButton, str]]]:
    """Custom button shown in the Rich Presence (max 2).

    .. note::
    
        When received over the gateway, the field is an array of strings, which are the button labels. Bots cannot access a user's activity button URLs. When sending, the field must be an array of the object.
    """
    if (data := self.__dict__.get("buttons", MISSING)) is MISSING: return data
    return [ActivityButton(**button) if not isinstance(button, str) else button for button in data]
  
  @property
  def created_at(self) -> int:
    """Unix timestamp (in milliseconds) of when the activity was added to the user's session."""
    return self.__dict__["created_at"]

  @property
  def details(self) -> Optional[Nullable[str]]:
    """What the player is currently doing."""
    return self.__dict__.get("details", MISSING)

  @property
  def details_url(self) -> Optional[Nullable[str]]:
    """URL that is linked when clicking on the details text."""
    return self.__dict__.get("details_url", MISSING)
  
  @property
  def emoji(self) -> Optional[Nullable[ActivityEmoji]]:
    """Emoji used for a custom status."""
    if (data := self.__dict__.get("emoji", MISSING)) in (MISSING, None): return data
    return ActivityEmoji(**data)

  @property
  def flags(self) -> Optional[ActivityFlags]:
    """Describes what the payload includes."""
    if (data := self.__dict__.get("flags", MISSING)) is MISSING: return data
    return ActivityFlags(data)
  
  @property
  def instance(self) -> Optional[bool]:
    """Whether or not the activity is an instanced game session."""
    return self.__dict__.get("instance", MISSING)
  
  @property
  def name(self) -> str:
    """Activity's name."""
    return self.__dict__["name"]

  @property
  def party(self) -> Optional[ActivityParty]:
    """Information for the current party of the player."""
    if (data := self.__dict__.get("party", MISSING)) is MISSING: return data
    return ActivityParty(**data)

  @property
  def secrets(self) -> Optional[ActivitySecrets]:
    """Secrets for Rich Presence joining and spectating."""
    if (data := self.__dict__.get("secrets", MISSING)) is MISSING: return data
    return ActivitySecrets(**data)

  @property
  def state(self) -> Optional[Nullable[str]]:
    """User's current party status, or text used for a custom status."""
    return self.__dict__.get("state", MISSING)

  @property
  def state_url(self) -> Optional[Nullable[str]]:
    """URL that is linked when clicking on the state text."""
    return self.__dict__.get("state_url", MISSING)

  @property
  def status_display_type(self) -> Optional[Nullable[StatusDisplayType]]:
    """Controls which field is displayed in the user's status text in the member list."""
    if (data := self.__dict__.get("status_display_type", MISSING)) in (MISSING, None): return data
    return StatusDisplayType(data)

  @property
  def timestamps(self) -> Optional[ActivityTimestamps]:
    """Unix timestamps for start and/or end of the game."""
    if (data := self.__dict__.get("timestamps", MISSING)) is MISSING: return data
    return ActivityTimestamps(**data)

  @property
  def type(self) -> ActivityType:
    """Activity type."""
    return ActivityType(self.__dict__["type"])

  @property
  def url(self) -> Optional[Nullable[str]]:
    """Stream URL, is validated when :attr:`Activity.type <.type>` is :attr:`ActivityType.STREAMING <discord.enums.ActivityType.STREAMING>`."""
    return self.__dict__.get("url", MISSING)