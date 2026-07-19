from ._logging import Logger
from .enums import OpCode
from .events import DispatchEvent
from .flags import GatewayIntent
from .utils import MISSING, Nullable, Optional
from aiohttp import ClientWebSocketResponse, WSMessage, WSMsgType
from typing import Any, Self, TYPE_CHECKING
import asyncio, threading, time

if TYPE_CHECKING:
  from .client import Client


class GatewayEvent:
  """Represents a Gateway event payload"""
  
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
    """Event data"""
    return self.__d

  @property
  def op(self) -> OpCode:
    """Gateway opcode, which indicates the payload type"""
    return OpCode(self.__op)

  @property
  def s(self) -> Nullable[int]:
    """Sequence number of event used for resuming sessions and heartbeating"""
    return self.__s

  @property
  def t(self) -> Nullable[str]:
    """Event name"""
    return self.__t

  def to_dict(self) -> dict[str, Any]:
    """Parse into a dictionary"""
    return {
      "op": self.op.value,
      "d": self.d,
      "s": self.s,
      "t": self.t
    }

  @classmethod
  def HEARTBEAT(cls, sequence: Nullable[int], /) -> Self:
    """Generate a :attr:`~discord.enums.OpCode.HEARTBEAT` event with the given ``s`` field.
    
    :param sequence: Last received sequence number
    """
    if sequence is not None and not isinstance(sequence, int):
      raise TypeError(f"sequence: Must be an instance of {int}; not {sequence.__class__}")
    return cls(op = OpCode.HEARTBEAT.value, d = sequence)

  @classmethod
  def IDENTIFY(cls, *, token: str, intents: GatewayIntent) -> Self:
    """Generate an :attr:`~discord.enums.OpCode.IDENTIFY` event.

    :param token: Authentication token
    :param intents: Gateway intents you wish to receive
    """
    if not isinstance(token, str):
      raise TypeError(f"token: Must be an instance of {str}; not {token.__class__}")
    if not isinstance(intents, GatewayIntent):
      raise TypeError(f"intents: Must be an instance of {GatewayIntent}; not {intents.__class__}")
    return cls(
      op = OpCode.IDENTIFY.value,
      d = {
        "token": token,
        "intents": intents.value,
        "properties": {
          "os": "windows",
          "browser": "demoutrei.discord",
          "device": "demoutrei.discord"
        }
      }
    )

  @classmethod
  def RESUME(cls, *, token: str, session_id: str, sequence: Nullable[int]) -> Self:
    """Generate a :attr:`~discord.enums.OpCode.RESUME` event

    :param token: Session token
    :param session_id: Session ID
    :param sequence: Last sequence number received
    """
    if not isinstance(token, str):
      raise TypeError(f"token: Must be an instance of {str}; not {token.__class__}")
    if not isinstance(session_id, str):
      raise TypeError(f"session_id: Must be an instance of {str}; not {session_id.__class__}")
    if sequence is not None:
      if not isinstance(sequence, int):
        raise TypeError(f"sequence: Must be an instance of {int}; not {sequence.__class__}")
    return cls(
      op = OpCode.RESUME.value,
      d = {
        "token": token,
        "session_id": session_id,
        "seq": sequence
      }
    )


class KeepAliveThread(threading.Thread):
  def __init__(self, socket: "DiscordWebSocket", /, *, interval: int) -> None:
    super().__init__(daemon = True)
    self.__heartbeat_timeout: float = 60.0
    self.__interval: int = interval
    self.__latency: float = float("inf")
    self.__socket: DiscordWebSocket = socket
    self.__stop_event: threading.Event = threading.Event()
    self._last_ack: float = time.perf_counter()
    self._last_receive: float = time.perf_counter()
    self._last_send: float = time.perf_counter()

  def ack(self) -> None:
    ack_time: float = time.perf_counter()
    self._last_ack: float = ack_time
    self.__latency: float = ack_time - self._last_send

  def beat(self) -> dict[str, Nullable[int]]:
    self._last_send: float = time.perf_counter()
    return self.get_payload()

  @property
  def interval(self) -> float:
    return self.__interval / 1_000

  @property
  def latency(self) -> float:
    return self.__latency

  def run(self) -> None:
    while not self.__stop_event.wait(self.interval):
      if self._last_receive + self.__heartbeat_timeout < time.perf_counter():
        with Logger.debug("Attempted a restart."):
          future: asyncio.Future = asyncio.run_coroutine_threadsafe(self.__socket._client.close(4000), loop = self.__socket._client._loop)
          try: future.result()
          except BaseException as exception: raise exception
          finally: self.stop()
          return
      future: asyncio.Future = asyncio.run_coroutine_threadsafe(self.__socket.heartbeat(), loop = self.__socket._client._loop)
      try:
        total: int = 0
        while True:
          try:
            future.result(10)
            break
          except Exception as exception: raise exception
      except Exception: self.stop()
      else: self._last_send: float = time.perf_counter()

  def stop(self) -> None:
    self.__stop_event.set()

  def tick(self) -> None:
    self._last_receive: float = time.perf_counter()


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
      instance.__last_sequence: Nullable[int] = None
      instance.__resume_gateway_url: Optional[str] = MISSING
      instance.__session_id: Optional[str] = MISSING
      instance.__wss_url: Optional[str] = MISSING
      instance._keep_alive: Optional[KeepAliveThread] = MISSING
      cls.__instance: Self = instance
    return cls.__instance

  def __heartbeat_payload(self) -> GatewayEvent:
    return GatewayEvent.HEARTBEAT(self.__last_sequence)

  @property
  def _client(self) -> Client:
    """The underlying Discord client"""
    return self.__client

  async def close(self, code: int, /) -> None:
    """Close connection.
    
    :param code: Close code
    """
    if self._keep_alive:
      self._keep_alive.stop()
      self._keep_alive: Optional[KeepAliveThread] = MISSING
    if self.__connection:
      with Logger.debug(f"Connection closed with code: {code}"):
        await self.__connection.close(code = code)
        self.__connection: Optional[ClientWebSocketResponse] = MISSING

  async def connect(self, url: Optional[str] = MISSING, /) -> None:
    """Initiate a websocket connection to the Discord gateway

    :param url: WSS URL to use for connecting to gateway
    """
    if url is not MISSING:
      if not isinstance(url, str):
        raise TypeError(f"url: Must be an instance of {str}; not {url.__class__}")
    else:
      async with await self._client._http.get_gateway() as response:
        url: str = f"{response["url"]}/?v=10&encoding=json"
        self.__wss_url: str = url
        Logger.debug(f"Cached WSS URL: {self.__wss_url}")
    with Logger.debug("Connected to gateway"):
      url: str = url.strip()
      if not url:
        raise ValueError("url: Must not be an empty string")
      self.__connection: ClientWebSocketResponse = await self._client._session.ws_connect(url)
    while self.__connection:
      event: Nullable[GatewayEvent] = await self.receive()
      if not event: continue
      match event.op:
        case OpCode.DISPATCH:
          await self.dispatch(event)
        case OpCode.HEARTBEAT: await self.heartbeat()
        case OpCode.HEARTBEAT_ACK: await self.heartbeat_ack()
        case OpCode.HELLO:
          await self.hello(heartbeat_interval = event.d["heartbeat_interval"])
          await self.identify()
        case OpCode.INVALID_SESSION:
          if not event.d:
            await self.disconnect()
            await self.connect()
            await self.identify()
          else:
            await self.reconnect()
        case OpCode.RECONNECT: await self.reconnect()
        case _:
          continue

  async def disconnect(self) -> None:
    """Disconnect the connection with the Discord gateway API"""
    if self._keep_alive is not None:
      self._keep_alive.stop()
      self._keep_alive: Optional[KeepAliveThread] = MISSING
    if self.__connection is not None:
      with Logger.debug("Discord websocket connection disconnected"):
        await self.__connection.close()
        self.__connection: Optional[ClientWebSocketResponse] = MISSING

  async def dispatch(self, event: GatewayEvent) -> None:
    """Handle a dispatch event"""
    if not isinstance(event, GatewayEvent):
      raise TypeError(f"event: Must be an instance of {GatewayEvent}; not {event.__class__}")
    if event.op is not OpCode.DISPATCH:
      raise ValueError(f"event.op: Must be {OpCode.DISPATCH}; not {event.op}")
    event_cls: Nullable[type[DispatchEvent]] = DispatchEvent[event.t]
    if event_cls is not None:
      dispatch_event: DispatchEvent = event_cls(**event.d)
      if event.t.strip().upper() == "READY":
        self.__resume_gateway_url: str = dispatch_event.resume_gateway_url
        self.__session_id: str = dispatch_event.session_id
      await self._client._Client__event_manager.dispatch(dispatch_event)

  async def heartbeat(self) -> None:
    """Send a :attr:`~discord.enums.OpCode.HEARTBEAT` event"""
    await self.send(self.__heartbeat_payload())

  async def heartbeat_ack(self) -> None:
    if self._keep_alive:
      self._keep_alive.ack()

  async def hello(self, *, heartbeat_interval: int) -> None:
    """Handler for :attr:`~discord.enums.OpCode.HELLO` event"""
    if not isinstance(heartbeat_interval, int):
      raise TypeError(f"heartbeat_interval: Must be an instance of {int}; not {heartbeat_interval.__class__}")
    if heartbeat_interval < 0:
      raise ValueError(f"heartbeat_interval: Must be greater than or equal to 0")
    self._keep_alive: threading.Thread = KeepAliveThread(self, interval = heartbeat_interval)
    await self.heartbeat()
    self._keep_alive.start()

  async def identify(self) -> None:
    """Send an :attr:`~discord.enums.OpCode.IDENTIFY` event"""
    event: GatewayEvent = GatewayEvent.IDENTIFY(
      token = self._client._Client__token,
      intents = self._client.intents
    )
    await self.send(event)

  async def receive(self) -> Nullable[GatewayEvent]:
    """Poll an event from the gateway"""
    if not self.__connection:
      raise RuntimeError("No websocket connection found")
    message: WSMessage = await self.__connection.receive()
    match message.type:
      case WSMsgType.CLOSE: await self.close(message.data)
      case _:
        event: GatewayEvent = GatewayEvent(**message.json())
        if event.op is not OpCode.DISPATCH:
          Logger.debug(f"Gateway event received: {event.op!r}")
        if event.s is not None:
          self.__last_sequence: int = event.s
        if self._keep_alive:
          self._keep_alive.tick()
        return event

  async def reconnect(self) -> None:
    """Initiate a reconnect with the Discord gateway API"""
    with Logger.debug("Discord websocket connection reconnected"):
      await self.disconnect()
      if not self.__resume_gateway_url:
        raise ValueError("'resume_gateway_url' is not yet received")
      await self.connect(self.__resume_gateway_url)
      await self.resume()

  async def resume(self) -> None:
    """Send a :attr:`~discord.enums.OpCode.RESUME` event"""
    event: GatewayEvent = GatewayEvent.RESUME(
      token = self._client._Client__token,
      session_id = self.__session_id,
      sequence = self.__last_sequence
    )
    await self.send(event)

  async def send(self, event: GatewayEvent, /) -> None:
    if not isinstance(event, GatewayEvent):
      raise TypeError(f"event: Must be an instance of {GatewayEvent}; not {event.__class__}")
    with Logger.debug(f"Gateway event sent: {event.op!r}"):
      await self.__connection.send_json(event.to_dict())