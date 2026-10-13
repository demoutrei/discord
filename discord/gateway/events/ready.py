from ..._dataclass import dataclass
from ...objects.application import Application
from ...objects.unavailable_guild import UnavailableGuild
from ...objects.user import User
from ...types import MISSING, Optional


@dataclass
class ReadyEvent:
  @property
  def application(self) -> Application:
    """Contains :attr:`Application.id <discord.objects.Application.id>` and :attr:`Application.flags <discord.objects.Application.flags>`."""
    return Application(**self.__dict__["application"])

  @property
  def guilds(self) -> list[UnavailableGuild]:
    """Guilds the user is in."""
    return [UnavailableGuild(**data) for data in self.__dict__["guilds"]]

  @property
  def resume_gateway_url(self) -> str:
    """Gateway URL for resuming connections."""
    return self.__dict__["resume_gateway_url"]

  @property
  def session_id(self) -> str:
    """Used for resuming connections."""
    return self.__dict__["session_id"]

  @property
  def shard(self) -> Optional[list[int, int]]:
    """Shard information associated with this session, if sent with identifying."""
    return self.__dict__.get("shard", MISSING)

  @property
  def user(self) -> User:
    """Information about the user including email."""
    return User(**self.__dict__["user"])

  @property
  def v(self) -> int:
    """API version."""
    return self.__dict__["v"]