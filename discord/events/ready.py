from .._dataclass import dataclass
from ..objects import (
  Application,
  UnavailableGuild,
  User
)
from ..utils import Optional


@dataclass
class ReadyEvent:
  application: Application
  """Contains :attr:`~discord.objects.Application.id` and :attr:`~discord.objects.Application.flags`"""
  
  guilds: list[UnavailableGuild]
  """Guilds the user is in"""

  resume_gateway_url: str
  """Gateway URL for resuming connections"""

  session_id: str
  """Used for resuming connections"""

  shard: Optional[list[int, int]]
  """Shard information associated with this session, if sent when identifying"""
  
  user: User
  """Information about the user including email"""
  
  v: int
  """API version"""