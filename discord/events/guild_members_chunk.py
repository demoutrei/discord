from .._dataclass import dataclass
from ..objects import GuildMember
from ..snowflake import Snowflake
from ..utils import Optional
from .presence_update import PresenceUpdateEvent


@dataclass
class GuildMembersChunkEvent:
  chunk_count: int
  """Total number of expected chunks for this response."""
  
  chunk_index: int
  """Chunk index in the expected chunks for this response (``0 <= chunk_index < chunk-count``)."""
  
  guild_id: Snowflake
  """ID of the guild."""

  members: list[GuildMember]
  """Set of guild members."""

  nonce: Optional[str]
  """Nonce used in the ``Guild Members Request``."""

  not_found: Optional[list[Snowflake]]
  """When passing an invalid ID to ``REQUEST_GUILD_MEMBERS``, it will be returned here."""

  presences: Optional[list[PresenceUpdateEvent]]
  """When passing ``True`` to ``REQUEST_GUILD_MEMBERS``, presences of the returned members will be here."""