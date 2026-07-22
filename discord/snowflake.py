from . import DISCORD_EPOCH
from datetime import datetime
from typing import Self, Union


class Snowflake:
  """Represents a Discord snowflake"""

  def __eq__(self, other: Union[type[Self], int, str]) -> bool:
    if not isinstance(other, (self.__class__, int, str)): return False
    return str(other) == str(self)

  def __hash__(self) -> int:
    return self.__value

  def __init__(self, value: Union[str, int], /) -> None:
    if not isinstance(value, (str, int)):
      raise TypeError(f"value: Must be an instance of either: {str}, or {int}; not {value.__class__}")
    self.__value: Union[str, int] = int(value)

  def __int__(self) -> int:
    return self.__value

  def __str__(self) -> str:
    return str(self.__value)

  @property
  def increment(self) -> int:
    """For every ID that is generated on that process, this number is incremented"""
    return self.__value & 0xFFF

  @property
  def internal_process_id(self) -> int:
    return (self.__value & 0x1F000) >> 12

  @property
  def internal_worker_id(self) -> int:
    return (self.__value & 0x3E0000) >> 17

  @property
  def timestamp(self) -> int:
    """Milliseconds since Discord Epoch, the first second of 2015 or ``1420070400000``"""
    return (self.__value >> 22) + DISCORD_EPOCH

  def to_datetime(self) -> datetime:
    """Returns the corresponding :class:`datetime.datetime` object"""
    return datetime.fromtimestamp(self.timestamp)