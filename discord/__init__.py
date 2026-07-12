__all__ = (
  "Client",
  "Logger", "LogType",
  "utils"
)


__author__ = "demoutrei"
__copyright__ = "Copyright 2026-present demoutrei"
__license__ = "MIT"
__title__ = "demoutrei.discord"
__version__ = "26.0.0"


from ._logging import LogType, Logger
from .client import Client
from . import utils