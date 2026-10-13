__all__ = (
  "DiscordWebSocket",
  "GatewayEvent"
)


from ..enums import OpCode, StatusType
from ..flags import GatewayCapabilities, GatewayIntents
from ..logging import Logger
from ..objects.activity import Activity
from ..snowflake import Snowflake
from ..types import MISSING, Nullable, Optional
from .events._base import DispatchEvent
from aiohttp import ClientWebSocketResponse, WSMessage, WSMsgType
from collections.abc import Callable, Coroutine
from inspect import iscoroutinefunction
from typing import Any, Self, TYPE_CHECKING, Union
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


  @classmethod
  def HEARTBEAT(cls: type[Self], s: Nullable[int], /) -> Self:
    """Generate an :attr:`OpCode.HEARTBEAT <discord.enums.OpCode.HEARTBEAT>` event payload.

    :param s: Last received sequence number.
    """
    if s is not None and not isinstance(s, int):
      raise TypeError(f"s: Must be an instance of {int}; not {s.__class__}.")
    return cls(
      op = OpCode.HEARTBEAT.value,
      d = s
    )

  
  @classmethod
  def IDENTIFY(cls: type[Self], *, intents: GatewayIntents, token: str, capabilities: Optional[GatewayCapabilities] = MISSING, compress: bool = False, large_threshold: int = 50, presence: Optional[GatewayEvent] = MISSING, shard: Optional[list[int, int]] = MISSING) -> Self:
    """Generate an :attr:`OpCode.IDENTIFY <discord.enums.OpCode.IDENTIFY>` event payload.

    :param capabilities: Bitfield representing capabilities of your gateway client.
    :param compress: Whether this connection supports compression of packets. Defaults to ``False``
    :param intents: Gateway events you wish to receive.
    :param large_threshold: Value between ``50`` and ``250``; total number of members where the gateway will stop sending offline members in the guild member list.
    :param presence: :attr:`GatewayEvent.PRESENCE_UPDATE() <discord.gateway.GatewayEvent.PRESENCE_UPDATE>` structure for initial presence information.
    :param shard: Used for Guild Sharding.
    :param token: Discord application authentication token.
    """
    if capabilities is not MISSING:
      if not isinstance(capabilities, GatewayCapabilities):
        raise TypeError(f"capabilities: Must be an instance of {GatewayCapabilities}; not {capabilities.__class__}")
    if not isinstance(compress, bool):
      raise TypeError(f"compress: Must be an instance of {bool}; not {compress.__class__}")
    if not isinstance(intents, GatewayIntents):
      raise TypeError(f"intents: Must be an instance of {GatewayIntents}; not {intents.__class__}.")
    if not isinstance(large_threshold, int):
      raise TypeError(f"large_threshold: Must be an instance of {int}; not {large_threshold.__class__}")
    if not (50 <= large_threshold <= 250):
      raise ValueError(f"large_threshold: Value must be between 50 and 250")
    if presence is not MISSING:
      if not isinstance(presence, GatewayEvent):
        raise TypeError(f"presence: Must be an instance of {GatewayEvent}; not {presence.__class__}")
      if not (presence.op is OpCode.PRESENCE_UPDATE):
        raise ValueError(f"presence.op: Must be {OpCode.PRESENCE_UPDATE}")
    if shard is not MISSING:
      if not isinstance(shard, list):
        raise TypeError(f"shard: Must be an instance of {list}; not {shard.__class__}")
      if len(shard) != 2:
        raise ValueError(f"shard: Must be an array of two integers (shard_id, num_shards)")
      for index, item in enumerate(shard):
        if not isinstance(item, int):
          raise TypeError(f"shard[{index}]: Must be an instance of {int}; not {item.__class__}")
        if item < 0:
          raise ValueError(f"shard[{index}]: Must be a positive integer")
    if not isinstance(token, str):
      raise TypeError(f"token: Must be an instance of {str}; not {token.__class__}.")
    if not token:
      raise ValueError(f"token: Must not be an empty string.")
    data: dict[str, Any] = {
      "compress": compress,
      "intents": intents.value,
      "properties": {
        "os": "windows",
        "browser": "demoutrei.discord",
        "device": "demoutrei.discord"
      },
      "token": token
    }
    if capabilities is not MISSING:
      data["capabilities"]: int = capabilities.value
    if presence is not MISSING:
      data["presence"]: dict[str, Any] = presence.to_dict()["d"]
    if shard is not MISSING:
      data["shard"]: list[int, int] = shard
    return cls(
      op = OpCode.IDENTIFY.value,
      d = data
    )


  @property
  def op(self) -> OpCode:
    """Gateway opcode, which indicates the payload type."""

    return OpCode(self.__op)


  @classmethod
  def PRESENCE_UPDATE(cls: type[Self], *, activities: list[Activity], afk: bool, status: StatusType, since: Nullable[int] = None) -> Self:
    """Generate an :attr:`OpCode.PRESENCE_UPDATE <discord.enums.OpCode.PRESENCE_UPDATE>` event.

    :param activities: User's activities.
    :param afk: Whether or not the client is AFK.
    :param since: Unix time (in milliseconds) of when the client went idle, or null if the client is not idle.
    :param status: User's new status.
    """
    if not isinstance(activities, list):
      raise TypeError(f"activities: Must be an instance of {list}; not {activities.__class__}")
    for index, item in enumerate(activities):
      if not isinstance(item, Activity):
        raise TypeError(f"activities[{index}]: Must be an instance of {Activity}; not {item.__class__}")
    if not isinstance(afk, bool):
      raise TypeError(f"afk: Must be an instance of {bool}; not {afk.__class__}")
    if not isinstance(status, StatusType):
      raise TypeError(f"status: Must be an instance of {StatusType}; not {status.__class__}")
    if since is not None:
      if not isinstance(since, int):
        raise TypeError(f"since: Must be an instance of {int}; not {since.__class__}")
      if since < 0:
        raise ValueError(f"since: Must be greater than or equal to 0")
    data: dict[str, Any] = {
      "activities": [activity._to_dict() for activity in activities],
      "afk": afk,
      "since": since,
      "status": status
    }
    return cls(
      op = OpCode.PRESENCE_UPDATE.value,
      d = data
    )


  @classmethod
  def REQUEST_CHANNEL_INFO(cls: type[Self], *, guild_id: Snowflake, fields: list[str]) -> Self:
    """Requests ephemeral channel data for channels in a guild. The server will send an :attr:`OpCode.CHANNEL_INFO <discord.enums.OpCode.CHANNEL_INFO>` event in response.

    :param fields: The fields to request. The current available fields are ``status`` and ``voice_start_time``.
    :param guild_id: The guild ID to request channel info for.
    """
    if not isinstance(guild_id, (_ := Snowflake)):
      raise TypeError(f"guild_id: Must be an instance of {_}; not {guild_id.__class__}")
    if not isinstance(fields, (_ := list)):
      raise TypeError(f"fields: Must be an instance of {_}; not {fields.__class__}")
    if not fields:
      raise ValueError(f"fields: Must not be an empty string.")
    for index, item in enumerate(fields):
      if not isinstance(item (_ := str)):
        raise TypeError(f"fields[{index}]: Must be an instance of {_}; not {item.__class__}")
      if item not in ("status", "voice_start_time"):
        raise ValueError(f"fields[{index}]: The current available fields are 'status' and 'voice_start_time'.")
    return cls(
      op = OpCode.REQUEST_CHANNEL_INFO.value,
      d = {
        "guild_id": str(snowflake),
        "fields": fields
      }
    )


  @classmethod
  def REQUEST_GUILD_MEMBERS(cls: type[Self], *, guild_id: Snowflake, limit: int, nonce: Optional[str] = MISSING, presences: Optional[bool] = MISSING, query: Optional[str] = MISSING, user_ids: Optional[Union[Snowflake, list[Snowflake]]] = MISSING) -> Self:
    """Used to request all members for a guild or a list of guilds.
    
    When initially connecting, if you don't have the :attr:`GatewayIntents.GUILD_PRESENCES <discord.flags.GatewayIntents.GUILD_PRESENCES>`, or if the guild is over 75k members, it will only send members who are in voice, plus the member for you (the connecting user). Otherwise, if a guild has over ``large_threshold`` members (value in the :meth:`GatewayEvent.IDENTIFY() <discord.gateway.GatewayEvent.IDENTIFY>`), it will only send members who are online, have a role, have a nickname, or are in a voice channel; and if it has under ``large_threshold`` members, it will send all members.
    
    If the client wishes to receive additional members, they need to explicitly request them via this operation. The server will send :meth:`GatewayEvent.GUILD_MEMBERS_CHUNK() <discord.gateway.GatewayEvent.GUILD_MEMBERS_CHUNK>` in response with up to 1000 members per chunk until all members that match the request have been sent.

    .. important::

        Due to our privacy and infrastructural concerns with this feature, there are some limitations that apply:

        - :attr:`GatewayIntents.GUILD_PRESENCES <discord.flags.GatewayIntents.GUILD_PRESENCES>` is required to set ``presences = True``. Otherwise, it will always be ``False``.

        - :attr:`GatewayIntents.GUILD_MEMBERS <discord.flags.GatewayIntents.GUILD_MEMBERS>` is required to request the entire member list---``(query = '', limit = 0 <= n)``.

        - You will be limited to requesting 1 ``guild_id`` per request.

        - Requesting a prefix (``query`` parameter) will return a maximum of 100 members.

        - Requesting ``user_ids`` will continue to be limited to returning 100 members.

    :param guild_id: ID of the guild to get members for.
    :param limit: Maximum number of members to send matching the ``query``; a limit of ``0`` can be used with an empty string ``query`` to return all members.
    :param nonce: Nonce to identify the :class:`OpCode.GUILD_MEMBERS_CHUNK <discord.enums.OpCode.GUILD_MEMBERS_CHUNK>` response.
    :param presences: Used to specify if we want the presences of the matched members.
    :param query: String that username starts with, or an empty string to return all members.
    :param user_ids: Used to specify which users you wish to fetch.
    """
    if not isinstance(guild_id, Snowflake):
      raise TypeError(f"guild_id: Must be an instance of {Snowflake}; not {guild_id.__class__}")
    if not isinstance(limit, int):
      raise TypeError(f"limit: Must be an instance of {int}; not {limit.__class__}")
    if limit < 0:
      raise ValueError(f"limit: Must be greater than or equal to 0")
    if nonce is not MISSING:
      if not isinstance(nonce, str):
        raise TypeError(f"nonce: Must be an instance of {str}; not {nonce.__class__}")
    if presences is not MISSING:
      if not isinstance(presences, (_ := bool)):
        raise TypeError(f"presences: Must be an instance of {_}; not {presences.__class__}")
    if query is not MISSING:
      if not isinstance(query, (_ := str)):
        raise TypeError(f"query: Must be an instance of {_}; not {query.__class__}")
    if not isinstance(user_ids, MISSING):
      if isinstance(user_ids, list):
        for index, item in enumerate(user_ids):
          if not isinstance(item, (_ := Snowflake)):
            raise TypeError(f"user_ids[{index}]: Must be an instance of {_}; not {item.__class__}")
      if not isinstance(user_ids, (_ := Snowflake)):
        raise TypeError(f"user_id: Must be an instance of {_}; not {user_ids.__class__}")
    data: dict[str, Any] = {
      "guild_id": guild_id,
      "limit": limit
    }
    if nonce is not MISSING:
      data["nonce"]: str = nonce
    if presences is not MISSING:
      data["presences"]: bool = presences
    if query is not MISSING:
      data["query"]: str = query
    if user_ids is not MISSING:
      data["user_ids"]: Union[Snowflake, list[Snowflake]] = user_ids
    return cls(
      op = OpCode.REQUEST_GUILD_MEMBERS.value,
      d = data
    )


  @classmethod
  def REQUEST_SOUNDBOARD_SOUNDS(cls: type[Self], *, guild_ids: list[Snowflake]) -> Self:
    """Used to request soundboard sounds for a list of guilds. The server will send :attr:`OpCode.SOUNDBOARD_SOUNDS <discord.enums.OpCode.SOUNDBOARD_SOUNDS>` events for each guild in response.

    :param guild_ids: IDs of the guilds to get soundboard sounds for.
    """
    if not isinstance(guild_ids, (_ := list)):
      raise TypeError(f"guild_ids: Must be an instance of {_}; not {guild_ids.__class__}")
    for index, item in enumerate(guild_ids):
      if not isinstance(item, (_ := Snowflake)):
        raise TypeError(f"guild_ids[{index}]: Must be an instance of {_}; not {item.__class__}")
    return cls(
      op = OpCode.REQUEST_SOUNDBOARD_SOUNDS.value,
      d = {
        "guild_ids": [str(snowflake) for snowflake in guild_ids]
      }
    )


  @classmethod
  def RESUME(cls: type[Self], *, token: str, session_id: str, sequence: Nullable[int]) -> Self:
    """Generate an :attr:`OpCode.RESUME <discord.enums.OpCode.RESUME>` event.

    :param token: Session token.
    :param session_id: Session ID.
    :param sequence: Last sequence number received.
    """
    if not isinstance(token, str):
      raise TypeError(f"token: Must be an instance of {str}; not {token.__class__}")
    if not token:
      raise ValueError(f"token: Must not be an empty string.")
    if not isinstance(session_id, str):
      raise TypeError(f"session_id: Must be an instance of {str}; not {session_id.__class__}")
    if not session_id:
      raise ValueError(f"session_id: Must not be an empty string.")
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


  @classmethod
  def VOICE_STATE_UPDATE(cls, *, guild_id: Snowflake, channel_id: Nullable[Snowflake], self_mute: bool, self_deaf: bool) -> Self:
    """Sent when a client wants to join, move, or disconnect from a voice channel.

    :param channel_id: ID of the voice channel the client wants to join (``None`` is disconnecting).
    :param guild_id: ID of the guild.
    :param self_deaf: Whether the client is deafened.
    :param self_mute: Whether the client is muted.
    """
    if not isinstance(guild_id, (_ := Snowflake)):
      raise TypeError(f"guild_id: Must be an instance of {_}; not {guild_id.__class__}")
    if channel_id is not None:
      if not isinstance(channel_id, (_ := Snowflake)):
        raise TypeError(f"channel_id: Must be an instance of {_}; not {channel_id.__class__}")
    if not isinstance(self_mute, (_ := bool)):
      raise TypeError(f"self_mute: Must be an instance of {_}; not {self_mute.__class__}")
    if not isinstance(self_deaf, (_ := bool)):
      raise TypeError(f"self_deaf: Must be an instance of {_}; not {self_deaf.__class__}")
    data: dict[str, Any] = {
      "guild_id": str(guild_id),
      "self_mute": self_mute,
      "self_deaf": self_deaf
    }
    if channel_id is not None:
      data["channel_id"]: str = str(channel_id)
    return cls(
      op = OpCode.VOICE_STATE_UPDATE.value,
      d = data
    )


class EventManager:
  def __init__(self, socket: "DiscordWebSocket", /) -> None:
    self.__socket: DiscordWebSocket = socket
    self.__listeners: dict[type[DispatchEvent], list[Callable[..., Coroutine]]] = dict()


  def add_listener(self, name: str, callback: Callable[..., Coroutine], /) -> None:
    if not isinstance(name, str):
      raise TypeError(f"name: Must be an instance of {str}; not {name.__class__}")
    name: str = name.strip()
    if not name:
      raise ValueError("name: Must not be an empty string.")
    if not iscoroutinefunction(callback):
      raise TypeError(f"callback: Must be a coroutine function.")
    event_cls: Optional[DispatchEvent] = DispatchEvent[name]
    if not event_cls: return
    if event_cls not in self.__listeners:
      self.__listeners[event_cls]: list[Callable[..., Coroutine]] = list()
    self.__listeners[event_cls].append(callback)


  async def dispatch(self, event: DispatchEvent, /) -> None:
    if event.__class__ not in self.__listeners: return
    await asyncio.gather(*[listener(self.__socket.client, event) for listener in self.__listeners[event.__class__]])


class KeepAliveThread(threading.Thread):
  def __init__(self, socket: "DiscordWebSocket", /, *, interval: int) -> None:
    if not isinstance(interval, int):
      raise TypeError(f"interval: Must be an instance of {int}; not {interval.__class__}.")
    if interval < 0:
      raise ValueError(f"interval: Must be greater than or equal to 0.")
    super().__init__(daemon = True)
    self.__heartbeat_timeout: float = 60.0
    self.__interval: int = interval
    self.__last_ack: float = time.perf_counter()
    self.__last_receive: float = time.perf_counter()
    self.__last_send: float = time.perf_counter()
    self.__socket: DiscordWebSocket = socket
    self.__stop_event: threading.Event = threading.Event()


  def run(self) -> None:
    while not self.__stop_event.wait(self.__interval / 1_000):
      if self.__last_receive + self.__heartbeat_timeout < time.perf_counter():
        with Logger.debug("Attempted a restart."):
          future: asyncio.Future = asyncio.run_coroutine_threadsafe(self.__socket.client.close(4000), loop = self.__socket.client._loop)
          try: future.result()
          except BaseException as exception: raise exception
          finally: self.stop()
          return
      future: asyncio.Future = asyncio.run_coroutine_threadsafe(self.__socket.send(GatewayEvent.HEARTBEAT(self.__socket.last_sequence)), loop = self.__socket.client._loop)
      try:
        total: int = 0
        while True:
          try:
            future.result(10)
            break
          except BaseException as exception: raise exception
      except Exception: self.stop()
      else: self.__last_send: float = time.perf_counter()


  def stop(self) -> None:
    self.__stop_event.set()


  def tick(self) -> None:
    self.__last_receive: float = time.perf_counter()


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
      from ..client import Client
      if not isinstance(client, Client):
        raise TypeError(f"client: Must be an instance of {Client}; not {client.__class__}")
      instance: Self = super().__new__(cls)
      instance.__client: Client = client
      instance.__connection: Optional[ClientWebSocketResponse] = MISSING
      instance.__event_manager: EventManager = EventManager(instance)
      instance.__keep_alive_thread: Optional[KeepAliveThread] = MISSING
      instance.__last_sequence: Nullable[int] = None
      instance.__latency: float = float("inf")
      cls.__instance: Self = instance
    return cls.__instance


  def ack(self) -> None:
    """:meta private:"""
    if self.__keep_alive_thread:
      ack_time: float = time.perf_counter()
      self.__keep_alive_thread._KeepAliveThread__last_ack: float = ack_time
      self.__latency: float = ack_time - self.__keep_alive_thread._KeepAliveThread__last_send


  async def close(self, code: int, /) -> None:
    """Close the connection.

    :param code: Close code.
    """

    if self.__connection:
      with Logger.debug(f"Connection closed with code: {code}"):
        await self.__connection.close(code = code)
        self.__connection: Optional[ClientWebSocketResponse] = MISSING


  @property
  def client(self) -> Client:
    """The associated Discord client."""

    return self.__client


  async def connect(self, url: str, /) -> None:
    """Initiate a WebSocket connection to the Discord Gateway API.

    :param url: WSS URL to use for connecting to the gateway.
    """

    if not isinstance(url, str):
      raise TypeError(f"url: Must be an instance of {str}; not {url.__class__}")
    if not url:
      raise ValueError(f"url: Must not be an empty string.")
    with Logger.debug("Connected to gateway."):
      url: str = url.strip()
      if not url:
        raise ValueError("url: Must not be an empty string.")
      self.__connection: ClientWebSocketResponse = await self.__client._session.ws_connect(url)
    while self.__connection:
      event: Nullable[GatewayEvent] = await self.receive()
      if not event: continue
      hook_name: Optional[str] = MISSING
      match event.op:
        case OpCode.DISPATCH:
          event_cls: Optional[type[DispatchEvent]] = DispatchEvent[event.t]
          if event_cls:
            dispatch_event: DispatchEvent = event_cls(**event.d)
            await self.__event_manager.dispatch(dispatch_event)
          continue
        case OpCode.HEARTBEAT_ACK:
          hook_name: str = f"on_{event.op.name.lower()}"
          self.ack()
        case _: hook_name: str = f"on_{event.op.name.lower()}"
      if hook_name and hasattr(self, hook_name):
        await getattr(self, hook_name)(event)


  async def disconnect(self) -> None:
    """Disconnect the connection with the Discord Gateway API."""
    if self.__keep_alive_thread:
      self.__keep_alive_thread.stop()
      self.__keep_alive_thread: Optional[KeepAliveThread] = MISSING
    if self.__connection is not None:
      with Logger.debug("Discord WebSocket connection disconnected."):
        await self.__connection.close()
        self.__connection: Optional[ClientWebSocketResponse] = MISSING


  def dispatch(self, name: str, /) -> None:
    """A factory decorator for registering an :attr:`OpCode.DISPATCH <discord.enums.OpCode.DISPATCH>` Gateway event listener.

    :param name: Name of the Dispatch event.
    """
    def wrapper(function: Callable[..., Coroutine]) -> None:
      self.__event_manager.add_listener(name, function)
    return wrapper


  def keep_alive(self, *, interval: int) -> None:
    """Construct a keep-alive thread for the socket.
    
    :param interval: The interval to send heartbeats to the gateway.
    """
    self.__keep_alive_thread: KeepAliveThread = KeepAliveThread(self, interval = interval)
    self.__keep_alive_thread.start()


  @property
  def last_sequence(self) -> Nullable[int]:
    """The last received sequence number."""
    return self.__last_sequence


  @property
  def latency(self) -> float:
    """The Gateway API latency."""
    return self.__latency


  async def on_heartbeat(self, event: GatewayEvent, /) -> None:
    """Asynchronous hook for receiving :attr:`OpCode.HEARTBEAT <discord.enums.OpCode.HEARTBEAT>` Gateway events.

    :param event: The received Gateway event payload.
    """
    pass


  async def on_hello(self, event: GatewayEvent, /) -> None:
    """Asynchronous hook for receiving :attr:`OpCode.HELLO <discord.enums.OpCode.HELLO>` Gateway events.

    :param event: The received Gateway event payload.
    """
    pass


  async def on_heartbeat_ack(self, event: GatewayEvent, /) -> None:
    """Asynchronous hook for receiving :attr:`OpCode.HEARTBEAT_ACK <discord.enums.OpCode.HEARTBEAT_ACK>` Gateway events.

    :param event: The received Gateway event payload.
    """
    pass


  async def on_invalid_session(self, event: GatewayEvent, /) -> None:
    """Asynchronous hook for receiving :attr:`OpCode.INVALID_SESSION <discord.enums.OpCode.INVALID_SESSION>` Gateway events.

    :param event: The received Gateway event payload.
    """
    pass


  async def on_reconnect(self, event: GatewayEvent, /) -> None:
    """Asynchronous hook for receiving :attr:`OpCode.RECONNECT <discord.enums.OpCode.RECONNECT>` Gateway events.

    :param event: The received Gateway event payload.
    """
    pass


  async def receive(self) -> Nullable[GatewayEvent]:
    """Poll an event from the gateway.

    :meta private:
    """

    if not self.__connection:
      raise RuntimeError("No WebSocket connection found.")
    message: WSMessage = await self.__connection.receive()
    match message.type:
      case WSMsgType.CLOSE:
        await self.close(message.data)
      case _:
        event: GatewayEvent = GatewayEvent(**message.json())
        Logger.debug(f"Gateway event received: {event.op!r}", str(message.json()))
        if event.s is not None:
          self.__last_sequence: int = event.s
        if self.__keep_alive_thread:
          self.__keep_alive_thread.tick()
        return event


  async def send(self, event: GatewayEvent, /) -> None:
    """Send an event to the Discord Gateway API.

    :param event: The Gateway event to send.
    """
    if not isinstance(event, GatewayEvent):
      raise TypeError(f"event: Must be an instance of {GatewayEvent}; not {event.__class__}")
    with Logger.debug(f"Gateway event sent: {event.op!r}", str(event.to_dict())):
      await self.__connection.send_json(event.to_dict())

    
  async def setup(self) -> None:
    """Asynchronous hook for initializing connection to the Discord API."""

    pass