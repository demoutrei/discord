from .._dataclass import dataclass
from ..snowflake import Snowflake
from ..utils import Nullable, Optional
from .emoji import Emoji


@dataclass
class OnboardingPromptOption:
  """
  .. attention::
      When creating or updating a prompt option, the :attr:`~.emoji_id`, :attr:`~.emoji_name`, and :attr:`~.emoji_animated` fields must be used instead of the emoji object.
  """
  
  channel_ids: list[Snowflake]
  """IDs for channels a member is added to when the option is selected."""
  
  description: Nullable[str]
  """Desciption of the option."""
  
  emoji: Optional[Emoji]
  """Emoji of the option."""

  emoji_animated: Optional[bool]
  """Whether the emoji is animated."""

  emoji_id: Optional[Snowflake]
  """Emoji ID of the option."""

  emoji_name: Optional[str]
  """Emoji name of the option."""
  
  id: Snowflake
  """ID of the prompt option."""

  role_ids: list[Snowflake]
  """IDs for roles assigned to a member when the option is selected."""

  title: str
  """Title of the option."""