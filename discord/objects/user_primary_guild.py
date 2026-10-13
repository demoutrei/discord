from .._dataclass import dataclass
from ..snowflake import Snowflake
from ..types import Nullable


@dataclass
class UserPrimaryGuild:
  @property
  def badge(self) -> Nullable[str]:
    """The server tag badge hash."""
    return self.__dict__["badge"]
  
  @property
  def identity_enabled(self) -> Nullable[bool]:
    """Whether the user is displaying the primary guild's server tag. This can be ``None`` if the system clears the identity, e.g. the server no longer supports tags. This will be ``False`` if the user manually removes their tag."""
    return self.__dict__["identity_enabled"]
  
  @property
  def identity_guild_id(self) -> Nullable[Snowflake]:
    """The id of the user's primary guild."""
    if (data := self.__dict__["identity_guild_id"]) is None: return data
    return Snowflake(data)

  @property
  def tag(self) -> Nullable[str]:
    """The text of the user's server tag. Limited to 4 characters."""
    return self.__dict__["tag"]