from .._dataclass import dataclass
from ..snowflake import Snowflake
from ..types import Nullable


@dataclass
class WelcomeScreenChannel:
  @property
  def channel_id(self) -> Snowflake:
    """The channels' ID."""
    return Snowflake(self.__dict__["channel_id"])

  @property
  def description(self) -> str:
    """The description shown for the channel."""
    return self.__dict__["description"]

  @property
  def emoji_id(self) -> Nullable[Snowflake]:
    """The emoji ID, if the emoji is custom."""
    if (data := self.__dict__["emoji_id"]) is None: return data
    return Snowflake(data)

  @property
  def emoji_name(self) -> Nullable[str]:
    """The emoji name if custom, the unicode character if standard, or ``None`` if no emoji is set."""
    return self.__dict__["emoji_name"]