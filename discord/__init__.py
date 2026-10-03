__all__ = (
  "Client",
  "enums", "exceptions",
  "flags",
  "gateway",
  "http",
  "Logger",
  "types"
)


__author__: str = "demoutrei"
__copyright__: str = "Copyright 2026-Present demoutrei"
__license__: str = "MIT"
__title__: str = "demoutrei.discord"
__version__: str = "26.0.0-dev"


DISCORD_EPOCH: int = 1_420_070_400_000
"""Milliseconds since the first second of 2015."""


from . import enums, exceptions, flags, gateway, http, types
from .logging import Logger
from .client import Client