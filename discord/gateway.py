from ._logging import Logger
from .utils import MISSING, Nullable, Optional
from aiohttp import ClientWebSocketResponse
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
      instance.__connection: Optional[ClientWebSocketResponse] = MISSING
      instance.__wss_url: Optional[str] = MISSING
      cls.__instance: Self = instance
    return cls.__instance

  @property
  def _client(self) -> Client:
    """The underlying Discord client"""
    return self.__client

  async def connect(self, url: Optional[str] = MISSING, /) -> None:
    """Initiate a websocket connection to the Discord gateway

    :param url: WSS URL to use for connecting to gateway
    """
    if url is not MISSING:
      if not isinstance(url, str):
        raise TypeError(f"url: Must be an instance of {str}; not {url.__class__}")
    else:
      async with await self._client._http.get_gateway() as response:
        url: str = response["url"]
        self.__wss_url: str = url
        Logger.debug(f"Cached WSS URL: {url}")
    url: str = url.strip()
    if not url:
      raise ValueError("url: Must not be an empty string")
    self.__connection: ClientWebSocketResponse = await self._client._session.ws_connect(url)
    Logger.debug("Connected to gateway")