from ..._dataclass import dataclass
from ...objects.application import Application
from ...objects.unavailable_guild import UnavailableGuild
from ...objects.user import User
from ...types import Optional


@dataclass
class ReadyEvent:
  application: Application
  """Contains :attr:`Application.id <discord.objects.Application.id>` and :attr:`Application.flags <discord.objects.Application.flags>`."""

  guilds: list[UnavailableGuild]
  """Guilds the user is in."""

  resume_gateway_url: str
  """Gateway URL for resuming connections."""

  session_id: str
  """Used for resuming connections."""

  shard: Optional[list[int, int]]
  """Shard information associated with this session, if sent with identifying."""

  user: User
  """Information about the user including email."""

  v: int
  """API version."""