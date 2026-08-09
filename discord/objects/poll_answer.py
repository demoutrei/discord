from .._dataclass import dataclass
from .poll_media import PollMedia


@dataclass
class PollAnswer:
  answer_id: int
  """The ID of the answer.

  .. note::
      Only sent as part of responses from Discord's API/Gateway.
  """

  poll_media: PollMedia
  """The data of the answer."""