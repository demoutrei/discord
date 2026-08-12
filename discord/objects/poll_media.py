from .._dataclass import dataclass
from ..utils import Optional
from .emoji import Emoji


@dataclass
class PollMedia:
  emoji: Optional[Emoji]
  """The emoji of the field."""
  
  text: Optional[str]
  """The text of the field."""