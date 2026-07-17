from enum import IntEnum, unique


@unique
class OpCode(IntEnum):
  DISPATCH: int = 0
  """An event was dispatched."""

  HEARTBEAT: int = 1
  """Fired periodically by the client to keep the connection alive."""

  IDENTIFY: int = 2
  """Starts a new session during the initial handshake."""

  PRESENCE_UPDATE: int = 3
  """Update the client's presence."""

  VOICE_STATE_UPDATE: int = 4
  """Used to join/leave or move between voice channels."""

  RESUME: int = 6
  """Resume a previous session that was disconnected."""

  RECONNECT: int = 7
  """You should attempt to reconnect and resume immediately."""

  REQUEST_GUILD_MEMBERS: int = 8
  """Request information about offline guild members in a large guild."""

  INVALID_SESSION: int = 9
  """The session has been invalidated. You should reconnect and identify/resume accordingly."""

  HELLO: int = 10
  """Sent immediately after connecting, contains the ``heartbeat_interval`` to use."""

  HEARTBEAT_ACK: int = 11
  """Sent in response to receiving a heartbeat to acknowledge that it has been received."""

  REQUEST_SOUNDBOARD_SOUNDS: int = 31
  """Request information about soundboard sounds in a set of guilds."""

  REQUEST_CHANNEL_INFO: int = 43
  """Request ephemeral channel data for channels in a guild."""