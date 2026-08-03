from .._dataclass import dataclass
from ..snowflake import Snowflake
from ..utils import Nullable


@dataclass
class UserPrimaryGuild:
  badge: Nullable[str]
  """The server tag badge hash"""
  
  identity_enabled: Nullable[bool]
  """Whether the user is displaying the primary guild's server tag. This can be ``None`` if the system clears the identity, e.g. the server no longer supports tags. This will be ``False`` if the user manually removes their tag."""
  
  identity_guild_id: Nullable[Snowflake]
  """The id of the user's primary guild"""

  tag: Nullable[str]
  """The text of the user's server tag. Limited to 4 characters"""