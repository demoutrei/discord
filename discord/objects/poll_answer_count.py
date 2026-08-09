from .._dataclass import dataclass


@dataclass
class PollAnswerCount:
  count: int
  """The number of votes for this answer."""
  
  id: int
  """The answer ID."""

  me_voted: bool
  """Whether the current user voted for this answer."""