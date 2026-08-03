from .._dataclass import dataclass
from ..objects import Sticker
from ..snowflake import Snowflake


@dataclass
class GuildStickersUpdateEvent:
  guild_id: Snowflake
  """ID of the guild."""

  stickers: list[Sticker]
  """Array of stickers."""