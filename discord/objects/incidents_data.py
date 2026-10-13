from .._dataclass import dataclass
from ..types import ISO8601Timestamp, MISSING, Nullable, Optional
from datetime import datetime


@dataclass
class IncidentsData:
  @property
  def dms_disabled_until(self) -> Nullable[ISO8601Timestamp]:
    """When direct messages get enabled again."""
    if (data := self.__dict__["dms_disabled_until"]) is None: return data
    return datetime.fromisotimestamp(data)

  @property
  def dm_spam_detected_at(self) -> Optional[Nullable[ISO8601Timestamp]]:
    """When the dm spam was detected."""
    if (data := self.__dict__.get("dm_spam_detected_at", MISSING)) in (MISSING, None): return data
    return datetime.fromisotimestamp(data)
  
  @property
  def invites_disabled_until(self) -> Nullable[ISO8601Timestamp]:
    """When invites get enabled again."""
    if (data := self.__dict__["invites_disabled_until"]) is None: return data
    return datetime.fromisotimestamp(data)

  @property
  def raid_detected_at(self) -> Optional[Nullable[ISO8601Timestamp]]:
    """When the raid was detected."""
    if (data := self.__dict__.get("raid_detected_at", MISSING)) in (MISSING, None): return data
    return datetime.fromisotimestamp(data)