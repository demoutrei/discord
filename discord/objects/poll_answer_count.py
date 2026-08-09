from .._dataclass import dataclass


@dataclass
class PollAnswerCount:
  count: int
  """The number of votes for this answer."""
  
  id: int
  """The :attr:`~discord.objects.PollAnswer.answer_id`."""

  me_voted: bool
  """Whether the current user voted for this answer."""