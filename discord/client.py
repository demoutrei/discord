from ._http import HTTP
from ._logging import Logger
from .gateway import DiscordWebSocket
from .utils import MISSING, Optional
from os import environ, getenv
from typing import NoReturn, Self


class Client:
  """Represents a Discord client"""

  __instance: Optional[Self] = MISSING
  """Singleton Discord client instance

  :meta private:
  """

  def __new__(cls: type[Self]) -> Self:
    """Client constructor"""
    if not cls.__instance:
      instance: Self = super().__new__(cls)
      instance.__http: HTTP = HTTP(self)
      instance.__socket: DiscordWebSocket = DiscordWebSocket(self)
      instance.__token: Optional[str] = environ.get("APPLICATION_TOKEN")
      if not instance._Client__token:
        from dotenv import load_dotenv
        load_dotenv()
        instance.__token: Optional[str] = getenv("APPLICATION_TOKEN")
      if not instance._Client__token:
        raise ValueError("No valid Discord application token configured")
      cls.__instance: Self = instance
    return cls.__instance

  @property
  def _http(self) -> HTTP:
    """HTTP/S connection instance to the Discord API"""
    return self.__http

  async def connect(self) -> NoReturn:
    """Connect to the Discord gateway"""
    ...

  @property
  def ws(self) -> DiscordWebSocket:
    """WebSocket connection instance to the Discord gateway"""
    return self.__socket