from .._dataclass import dataclass
from ..utils import ISO8601Timestamp, Nullable, Optional


@dataclass
class IncidentsData:
  dms_disabled_until: Nullable[ISO8601Timestamp]
  """When direct messages get enabled again"""

  dm_spam_detected_at: Optional[Nullable[ISO8601Timestamp]]
  """When the dm spam was detected"""
  
  invites_disabled_until: Nullable[ISO8601Timestamp]
  """When invites get enabled again"""

  raid_detected_at: Optional[Nullable[ISO8601Timestamp]]
  """When the raid was detected"""