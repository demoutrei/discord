from .._dataclass import dataclass
from ..enums import PollLayoutType
from ..utils import ISO8601Timestamp, Nullable, Optional
from .poll_answer import PollAnswer
from .poll_media import PollMedia
from .poll_results import PollResults


@dataclass
class Poll:
  allow_multiselect: bool
  """Whether a user can select multiple answers."""
  
  answers: list[PollAnswer]
  """Each of the answers available in the poll."""

  expiry: Nullable[ISO8601Timestamp]
  """The time when the poll ends.

  .. hint::
      :attr:`~.expiry` is marked as nullable to support non-expiring polls in the future, but all polls have an expiry currently.
  """

  layout_type: PollLayoutType
  """The layout type of the poll."""
  
  question: PollMedia
  """The question of the poll. Only :attr:`~discord.objects.PollMedia.text` is supported."""

  results: Optional[PollResults]
  """The results of the poll."""