from enum import IntEnum, unique


@unique
class OpCode(IntEnum):
  DISPATCH: int = 0
  """An event was dispatched."""

  HEARTBEAT: int = 1
  """Fired periodically by the client to keep the connection alive."""

  HELLO: int = 10
  """Sent immediately after connecting, contains the ``heartbeat_interval`` to use."""

  HEARTBEAT_ACK: int = 11
  """Sent in response to receiving a heartbeat to acknowledge that it has been received."""