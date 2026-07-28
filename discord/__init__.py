__all__ = (
  "Client",
  "enums", "exceptions",
  "flags",
  "Logger",
  "objects",
  "Snowflake",
  "utils"
)


__author__: str = "demoutrei"
__copyright__: str = "Copyright 2026-present demoutrei"
__license__: str = "MIT"
__title__: str = "demoutrei.discord"
__version__: str = "26.1.8-dev2"
"""``demoutrei.discord`` package version"""


DISCORD_EPOCH: int = 1420070400000
"""Milliseconds since the first second of 2015"""


from ._logging import Logger
from .client import Client
from .snowflake import Snowflake
from . import enums, exceptions, flags, objects, utils