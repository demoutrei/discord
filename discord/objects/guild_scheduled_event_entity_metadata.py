from .._dataclass import dataclass
from ..utils import Optional


@dataclass
class GuildScheduledEventEntityMetadata:
  location: Optional[str]
  """Location of the event (1-100 characters).

  .. important::
      Required for events with ``'entity_type': EXTERNAL``.
  """