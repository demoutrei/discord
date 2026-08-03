from ..objects import GuildMember
from ..snowflake import Snowflake


class GuildMemberAddEvent(GuildMember):
  guild_id: Snowflake
  """ID of the guild."""