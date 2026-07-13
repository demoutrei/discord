from .utils import MISSING, Optional
from typing import Self, TYPE_CHECKING

if TYPE_CHECKING:
  from .client import Client


class DiscordWebSocket:
  """Represents a WebSocket connection to the Discord gateway"""

  __instance: Optional[Self] = MISSING
  """Singleton DiscordWebSocket instance

  :meta private:
  """

  def __new__(cls: type[Self], client: Client, /) -> Self:
    """DiscordWebSocket constructor

    :param client: The underlying Discord client
    """
    if not cls.__instance:
      from .client import Client
      if not isinstance(client, Client):
        raise TypeError(f"client: Must be an instance of {Client}; not {client.__class__}")
      instance: Self = super().__new__(cls)
      instance.__client: Client = client
      cls.__instance: Self = instance
    return cls.__instance

  @property
  def _client(self) -> Client:
    """The underlying Discord client"""
    return self.__client