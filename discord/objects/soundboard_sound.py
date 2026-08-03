from .._dataclass import dataclass
from ..snowflake import Snowflake
from ..utils import Nullable, Optional
from .user import User


@dataclass
class SoundboardSound:
  available: bool
  """Whether this sound can be used, may be false due to loss of Server Boosts."""
  
  emoji_id: Nullable[Snowflake]
  """The ID of this sound's custom emoji."""

  emoji_name: Nullable[str]
  """The unicode character of this sound's standard emoji."""

  guild_id: Optional[Snowflake]
  """The ID of the guild this sound is in."""
  
  name: str
  """The name of the sound."""

  sound_id: Snowflake
  """The ID of the sound."""

  user: Optional[User]
  """The user who created this sound."""

  volume: float
  """The volume of this sound, from 0 to 1."""