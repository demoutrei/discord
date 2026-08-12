from .._dataclass import dataclass
from .poll_answer_count import PollAnswerCount


@dataclass
class PollResults:
  answer_counts: list[PollAnswerCount]
  """The counts for each answer."""
  
  is_finalized: bool
  """Whether the votes have been precisely counted."""