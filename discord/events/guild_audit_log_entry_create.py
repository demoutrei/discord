from ..objects import AuditLogEntry
from ..snowflake import Snowflake


class GuildAuditLogEntryCreateEvent(AuditLogEntry):
  guild_id: Snowflake
  """ID of the guild."""