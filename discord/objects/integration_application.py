from .._dataclass import dataclass
from ..snowflake import Snowflake
from ..utils import Nullable, Optional
from .user import User


@dataclass
class IntegrationApplication:
  bot: Optional[User]
  """The bot associated with this application."""
  
  description: str
  """The description of the app."""
  
  icon: Nullable[str]
  """The icon hash of the app."""
  
  id: Snowflake
  """The ID of the app."""

  name: str
  """The name of the app."""