__all__ = (
  "Client",
  "enums", "exceptions",
  "flags",
  "Logger", "LogType",
  "objects",
  "Snowflake",
  "utils"
)


__author__ = "demoutrei"
__copyright__ = "Copyright 2026-present demoutrei"
__license__ = "MIT"
__title__ = "demoutrei.discord"
__version__ = "26.1.2"


DISCORD_EPOCH: int = 1420070400000


from ._logging import LogType, Logger
from .client import Client
from .snowflake import Snowflake
from . import enums, exceptions, flags, objects, utils