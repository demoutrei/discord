__all__ = (
  "Client",
)


from .http import HTTPClient
from .logging import Logger
from .gateway import DiscordWebSocket
from .types import MISSING, Nullable, Optional
from aiohttp import ClientSession
from os import environ, getenv
from typing import Self
import asyncio


class EnvironmentVariables:
  def __getattr__(self, key: str) -> Nullable[str]:
    if not isinstance(key, str):
      raise TypeError(f"key: Must be an instance of {str}; not {key.__class__}")
    if not key:
      raise ValueError(f"key: Must not be an empty string.")
    return getenv(key)
  
  
  def __init__(self) -> None:
    from dotenv import load_dotenv
    load_dotenv()


  def __setattr__(self, key: str, value: str) -> None:
    if not isinstance(key, str):
      raise TypeError(f"key: Must be an instance of {str}; not {key.__class__}.")
    if not key:
      raise ValueError(f"key: Must not be an emptry string.")
    if not key.isidentifier():
      raise ValueError(f"key: Must be a valid identifier.")
    if not isinstance(value, str):
      raise TypeError(f"value: Must be an instance of {str}; not {value.__class__}")
    if not value:
      raise ValueError(f"value: Must not be an empty string.")
    environ[key]: str = value



class Client:
  """Represents a client used to connect to Discord's API.

  :param gateway_cls: The :class:`~discord.gateway.DiscordWebSocket` subclass to use for connecting with the Discord API Gateway. Pass ``None`` to disable. Defaults to ``None``.
  """
  
  __instance: Optional[Self] = MISSING
  """Singleton Discord client instance.

  :meta private:
  """


  def __new__(cls: type[Self], *, gateway_cls: Nullable[DiscordWebSocket] = None) -> Self:
    if not cls.__instance:
      if gateway_cls is not None and not issubclass(gateway_cls, DiscordWebSocket):
        raise TypeError(f"gateway_cls: Must be a subclass of {DiscordWebSocket}; not {gateway_cls}")
      instance: Self = super().__new__(cls)
      instance.__event_loop: Optional[asyncio.AbstractEventLoop] = MISSING
      instance.__http: HTTPClient = HTTPClient(instance)
      instance.__session: Nullable[ClientSession] = None
      instance.__socket: Nullable[DiscordWebSocket] = gateway_cls(instance) if gateway_cls is not None else None
      instance.__env: EnvironmentVariables = EnvironmentVariables()
      if not instance.__env.APPLICATION_TOKEN:
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


  def connect(self) -> None:
    """Initiate a connection with the Discord API."""
    try:
      async def inner() -> None:
        self.__session: ClientSession = ClientSession(self.http.BASE_URL, raise_for_status = self.http._HTTPClient__status_check)
        if self.socket:
          await self.socket.setup()
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
  def env(self) -> EnvironmentVariables:
    """Configured environment variables for the client."""

    return self.__env


  @property
  def http(self) -> HTTPClient:
    """HTTP/S connection instance to the Discord API."""
    return self.__http


  @property
  def socket(self) -> Nullable[DiscordWebSocket]:
    """WebSocket connection instance to the Discord API gateway, if any."""
    return self.__socket