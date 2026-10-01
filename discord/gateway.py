__all__ = (
  "DiscordWebSocket",
  "GatewayEvent"
)


from .enums import OpCode
from .logging import Logger
from .types import MISSING, Nullable, Optional
from aiohttp import ClientWebSocketResponse, WSMessage, WSMsgType
from typing import Any, Self, TYPE_CHECKING
import asyncio, threading, time

if TYPE_CHECKING:
  from .client import Client


class GatewayEvent:
  """Represents a Gateway event payload."""

  def __init__(self, *, op: int, d: Nullable[Any] = None, s: Nullable[int] = None, t: Nullable[str] = None) -> None:
    if not isinstance(op, int):
      raise TypeError(f"op: Must be an instance of {int}; not {op.__class__}")
    if s is not None:
      if not isinstance(s, int):
        raise TypeError(f"s: Must be an instance of {int}; not {s.__class__}")
    if t is not None:
      if not isinstance(t, str):
        raise TypeError(f"t: Must be an instance of {str}; not {t.__class__}")
    self.__op: int = op
    self.__d: Nullable[Any] = d
    self.__s: Nullable[int] = s
    self.__t: Nullable[str] = t


  @property
  def d(self) -> Nullable[Any]:
    """Event data."""

    return self.__d


  @property
  def op(self) -> OpCode:
    """Gateway opcode, which indicates the payload type."""

    return OpCode(self.__op)


  @property
  def s(self) -> Nullable[int]:
    """Sequence number of event used for resuming sessions and heartbeating."""

    return self.__s


  @property
  def t(self) -> Nullable[str]:
    """Event name."""

    return self.__t


  def to_dict(self) -> dict[str, Any]:
    """Parse into a dictionary."""

    return {
      "op": self.op.value,
      "d": self.d,
      "s": self.s,
      "t": self.t
    }


class DiscordWebSocket:
  """Represents a WebSocket connection to the Discord API gateway.

  :param client: The underlying Discord client.
  """

  __instance: Optional[Self] = MISSING
  """Singleton DiscordWebSocket instance.

  :meta private:
  """


  def __new__(cls: type[Self], client: Client, /) -> Self:
    """DiscordWebSocket constructor."""

    if not cls.__instance:
      from .client import Client
      if not isinstance(client, Client):
        raise TypeError(f"client: Must be an instance of {Client}; not {client.__class__}")
      instance: Self = super().__new__(cls)
      instance.__client: Client = client
      instance.__connection: Optional[ClientWebSocketResponse] = MISSING
      cls.__instance: Self = instance
    return cls.__instance


  async def close(self, code: int, /) -> None:
    """Close the connection.

    :param code: Close code.
    """

    if self.__connection:
      with Logger.debug(f"Connection closed with code: {code}"):
        await self.__connection.close(code = code)
        self.__connection: Optional[ClientWebSocketResponse] = MISSING


  async def connect(self, url: Optional[str] = MISSING, /) -> None:
    """Initiate a WebSocket connection to the Discord Gateway API.

    :param url: WSS URL to use for connecting to the gateway.
    """

    if url is not MISSING:
      if not isinstance(url, str):
        raise TypeError(f"url: Must be an instance of {str}; not {url.__class__}")
    else:
      async with await self.__client.http.get_gateway() as response:
        url: str = f"{response["url"]}/?v=10&encoding=json"
        self.__wss_url: str = url
        Logger.debug(f"Cached WSS URL: {self.__wss_url}")
    with Logger.debug("Connected to gateway."):
      url: str = url.strip()
      if not url:
        raise ValueError("url: Must not be an empty string.")
      self.__connection: ClientWebSocketResponse = await self.__client._session.ws_connect(url)
    while self.__connection:
      event: Nullable[GatewayEvent] = await self.receive()
      if not event: continue


  async def disconnect(self) -> None:
    """Disconnect the connection with the Discord Gateway API."""

    if self.__connection is not None:
      with Logger.debug("Discord WebSocket connection disconnected."):
        await self.__connection.close()
        self.__connection: Optional[ClientWebSocketResponse] = MISSING


  async def receive(self) -> Nullable[GatewayEvent]:
    """Poll an event from the gateway."""

    if not self.__connection:
      raise RuntimeError("No WebSocket connection found.")
    message: WSMessage = await self.__connection.receive()
    match message.type:
      case WSMsgType.CLOSE:
        await self.close(message.data)
      case _:
        ...


  async def send(self, event: GatewayEvent, /) -> None:
    if not isinstance(event, GatewayEvent):
      raise TypeError(f"event: Must be an instance of {GatewayEvent}; not {event.__class__}")
    with Logger.debug(f"Gateway event sent: {event.op!r}"):
      await self.__connection.send_json(event.to_dict())