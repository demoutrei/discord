from ._logging import Logger
from .utils import MISSING, Optional
from typing import Self


class Client:
  """Represents a Discord client"""

  __instance: Optional[Self] = MISSING
  """Singleton Discord client instance

  :meta private:
  """

  def __new__(cls: type[Self]) -> Self:
    """Client constructor"""
    if not cls.__instance:
      instance: Self = super().__new__(cls)
      cls.__instance: Self = instance
    return cls.__instance