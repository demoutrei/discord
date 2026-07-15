from ._http import HTTP
from ._logging import Logger
from .gateway import DiscordWebSocket
from .utils import MISSING, Nullable, Optional
from aiohttp import ClientSession
from os import environ, getenv
from typing import Self


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
      instance.__http: HTTP = HTTP(instance)
      instance.__session: Nullable[ClientSession] = None
      instance.__socket: Nullable[DiscordWebSocket] = None
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

  @property
  def _session(self) -> Nullable[ClientSession]:
    """Current aiohttp session of the client, if any"""
    return self.__session

  async def connect(self, *, gateway: bool = True) -> None:
    """Initiate a connection with the Discord API

    :param gateway: Join connection with the gateway
    """
    try:
      if not isinstance(gateway, bool):
        raise TypeError(f"gateway: Must be an instance of {bool}; not {gateway.__class__}")
      self.__session: ClientSession = ClientSession(self._http.BASE_URL, raise_for_status = self._http._HTTP__status_check)
      if gateway:
        self.__socket: DiscordWebSocket = DiscordWebSocket(self)
        await self.ws.connect()
        ...
    except KeyboardInterrupt:
      ...
      Logger.info("Program terminated through keyboard interrupt")
      exit()
    except Exception as exception:
      Logger.error(exception)

  @property
  def ws(self) -> Nullable[DiscordWebSocket]:
    """WebSocket connection instance to the Discord gateway, if any"""
    return self.__socket