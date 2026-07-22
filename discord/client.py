from ._http import HTTP
from ._logging import Logger
from .events import EventManager
from .gateway import DiscordWebSocket
from .flags import GatewayIntent
from .utils import MISSING, Nullable, Optional
from aiohttp import ClientSession
from collections.abc import Coroutine, Callable
from os import environ, getenv
from typing import Self
import asyncio


class Client:
  """Represents a Discord client.

  :param intents: Set of Gateway intents to associate with the client
  """

  __instance: Optional[Self] = MISSING
  """Singleton Discord client instance

  :meta private:
  """

  def __new__(cls: type[Self], *, intents: GatewayIntent) -> Self:
    if not cls.__instance:
      if not isinstance(intents, GatewayIntent):
        raise TypeError(f"intents: Must be an instance of {GatewayIntent}; not {intents.__class__}")
      instance: Self = super().__new__(cls)
      instance.__event_loop: Optional[asyncio.AbstractEventLoop] = MISSING
      instance.__event_manager: EventManager = EventManager(instance)
      instance.__http: HTTP = HTTP(instance)
      instance.__intents: GatewayIntent = intents
      instance.__session: Nullable[ClientSession] = None
      instance.__socket: Nullable[DiscordWebSocket] = None
      instance.__token: Optional[str] = environ.get("APPLICATION_TOKEN")
      if not instance._Client__token:
        from dotenv import load_dotenv
        load_dotenv()
        instance.__token: Optional[str] = getenv("APPLICATION_TOKEN")
      if not instance._Client__token:
        raise ValueError("No valid Discord application token configured")
        exit()
      cls.__instance: Self = instance
    return cls.__instance

  @property
  def _http(self) -> HTTP:
    """HTTP/S connection instance to the Discord API"""
    return self.__http

  @property
  def _loop(self):
    if not self.__event_loop:
      from asyncio import new_event_loop, set_event_loop
      self.__event_loop = new_event_loop()
      set_event_loop(self.__event_loop)
    return self.__event_loop

  @property
  def _session(self) -> Nullable[ClientSession]:
    """Current aiohttp session of the client, if any"""
    return self.__session

  async def close(self, code: int = 4000, /) -> None:
    """Close connection from the Discord API"""
    await self.ws.close(code)
    await self._session.close()

  def connect(self, *, gateway: bool = True) -> None:
    """Initiate a connection with the Discord API

    :param gateway: Join connection with the gateway
    """
    try:
      async def inner() -> None:
        if not isinstance(gateway, bool):
          raise TypeError(f"gateway: Must be an instance of {bool}; not {gateway.__class__}")
        self.__session: ClientSession = ClientSession(self._http.BASE_URL, raise_for_status = self._http._HTTP__status_check)
        if gateway:
          self.__socket: DiscordWebSocket = DiscordWebSocket(self)
          await self.ws.connect()
      self._loop.run_until_complete(inner())
    except KeyboardInterrupt:
      self._loop.create_task(self.close())
      Logger.info("Program terminated through keyboard interrupt")
      exit()
    except Exception as exception:
      Logger.error(exception)
    else:
      self._loop.create_task(self.close(1000))

  def event_listener(name: str) -> Callable[..., Coroutine]:
    """Register a dispatch event listener

    :param name: Name of the event to listen to
    """
    async def decorator(function: Callable[..., Coroutine]) -> None:
      self.__event_manager.add_listener(name, function)
    return decorator

  @property
  def intents(self) -> GatewayIntent:
    """Set of Gateway intents to associate with the client."""
    return self.__intents

  @property
  def ws(self) -> Nullable[DiscordWebSocket]:
    """WebSocket connection instance to the Discord gateway, if any."""
    return self.__socket