from .._dataclass import dataclass
from ..enums import PremiumType
from ..flags import UserFlags
from ..snowflake import Snowflake
from ..utils import Nullable, Optional
from .avatar_decoration_data import AvatarDecorationData
from .collectible import Collectible
from .user_primary_guild import UserPrimaryGuild


@dataclass
class User:
  """Represents a Discord user"""
  
  accent_color: Optional[Nullable[int]]
  """The user's banner color encoded as an integer representation of hexadecimal color code"""
  
  avatar: Nullable[str]
  """The user's avatar hash"""

  avatar_decoration_data: Optional[Nullable[AvatarDecorationData]]
  """Data for the user's avatar decoration"""
  
  banner: Optional[Nullable[str]]
  """The user's banner hash"""
  
  bot: Optional[bool]
  """Whether the user belongs to an OAuth2 application"""

  collectibles: Optional[Nullable[Collectible]]
  """Data for the user's collectibles"""
  
  discriminator: str
  """The user's Discord-tag"""
  
  email: Optional[Nullable[str]]
  """The user's email"""
  
  flags: Optional[UserFlags]
  """The flags on a user's account"""
  
  global_name: Nullable[str]
  """The user's display name, if it is set"""
  
  id: Snowflake
  """The user's id"""

  locale: Optional[str]
  """The user's chosen language option"""

  mfa_enabled: Optional[bool]
  """Whether the user has two factor enabled on their account"""

  premium_type: Optional[PremiumType]
  """The type of Nitro subscription on a user's account"""

  primary_guild: Optional[Nullable[UserPrimaryGuild]]
  """The user's primary guild"""

  public_flags: Optional[UserFlags]
  """The public flags on a user's account"""

  system: Optional[bool]
  """Whether the user is an Official Discord System user (part of the urgent message system)"""

  username: str
  """The user's username, not unique across the platform"""

  verified: Optional[bool]
  """Whether the email on this account has been verified"""