__all__ = (
  "Client",
  "enums", "exceptions",
  "flags",
  "gateway",
  "http",
  "logging",
  "objects",
  "Snowflake",
  "types"
)


__author__: str = "demoutrei"
__copyright__: str = "Copyright 2026-Present demoutrei"
__license__: str = "MIT"
__title__: str = "demoutrei.discord"
__version__: str = "26.0.1"


DISCORD_EPOCH: int = 1_420_070_400_000
"""Milliseconds since the first second of 2015."""


from . import enums, exceptions, flags, gateway, http, logging, objects, types
from .client import Client
from .snowflake import Snowflake