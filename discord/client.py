from .http import HTTPClient
from .logging import Logger
from .gateway import DiscordWebSocket
from .types import MISSING, Nullable, Optional
from aiohttp import ClientSession
from os import getenv
from typing import Self
import asyncio


class Client:
  """Represents a client used to connect to Discord's API."""
  
  __instance: Optional[Self] = MISSING
  """Singleton Discord client instance.

  :meta private:
  """


  def __new__(cls: type[Self]) -> Self:
    if not cls.__instance:
      instance: Self = super().__new__(cls)
      instance.__event_loop: Optional[asyncio.AbstractEventLoop] = MISSING
      instance.__http: HTTPClient = HTTPClient(instance)
      instance.__session: Nullable[ClientSession] = None
      instance.__socket: Nullable[DiscordWebSocket] = None
      instance.__token: Nullable[str] = getenv("APPLICATION_TOKEN")
      if not instance._Client__token:
        from dotenv import load_dotenv
        load_dotenv()
        instance.__token: Nullable[str] = getenv("APPLICATION_TOKEN")
      if not instance._Client__token:
        raise ValueError("No valid Discord application token configured.")
        exit()
      cls.__instance: Self = instance
    return cls.__instance


  @property
  def _loop(self) -> asyncio.AbstractEventLoop:
    if not self.__event_loop:
      from asyncio import new_event_loop, set_event_loop
      self.__event_loop = new_event_loop()
      set_event_loop(self.__event_loop)
    return self.__event_loop


  @property
  def _session(self) -> Nullable[ClientSession]:
    """Current aiohttp session of the client, if any."""
    return self.__session


  async def close(self, code: int = 4000, /) -> None:
    """Close connection from the Discord API."""

    await self.socket.close(code)
    await self._session.close()


  def connect(self, *, gateway_cls: Nullable[type[DiscordWebSocket]] = DiscordWebSocket) -> None:
    """Initiate a connection with the Discord API.

    :param gateway_cls: The :class:`discord.gateway.DiscordWebSocket` class to use for connecting with the Discord API Gateway. Pass ``None`` to disable.
    """
    try:
      if gateway_cls is not None and not issubclass(gateway_cls, DiscordWebSocket):
        raise TypeError(f"gateway_cls: Must be a subclass of {DiscordWebSocket}; not {gateway_cls}")
      async def inner() -> None:
        self.__session: ClientSession = ClientSession(self.http.BASE_URL, raise_for_status = self.http._HTTPClient__status_check)
        if gateway_cls is not None:
          self.__socket: DiscordWebSocket = gateway_cls(self)
          await self.socket.connect()
      self._loop.run_until_complete(inner())
    except KeyboardInterrupt:
      self._loop.create_task(self.close())
      Logger.info("Program terminated through keyboard interrupt.")
      exit()
    except Exception as exception:
      Logger.error(exception)
    else:
      self._loop.create_task(self.close(1000))


  @property
  def http(self) -> HTTPClient:
    """HTTP/S connection instance to the Discord API."""
    return self.__http


  @property
  def socket(self) -> Nullable[DiscordWebSocket]:
    """WebSocket conection instance to the Discord API gateway, if any."""
    return self.__socket