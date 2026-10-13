from .._dataclass import dataclass
from ..enums import PremiumType
from ..flags import UserFlags
from ..snowflake import Snowflake
from ..types import MISSING, Nullable, Optional
from .avatar_decoration_data import AvatarDecorationData
from .collectible import Collectible
from .user_primary_guild import UserPrimaryGuild


@dataclass
class User:
  """Represents a Discord user."""
  
  @property
  def accent_color(self) -> Optional[Nullable[int]]:
    """The user's banner color encoded as an integer representation of hexadecimal color code."""
    return self.__dict__.get("accent_color", MISSING)
  
  @property
  def avatar(self) -> Nullable[str]:
    """The user's avatar hash."""
    return self.__dict__["avatar"]

  @property
  def avatar_decoration_data(self) -> Optional[Nullable[AvatarDecorationData]]:
    """Data for the user's avatar decoration."""
    if (data := self.__dict__.get("avatar_decoration_data", MISSING)) in (MISSING, None): return data
    return AvatarDecorationData(**data)
  
  @property
  def banner(self) -> Optional[Nullable[str]]:
    """The user's banner hash."""
    return self.__dict__.get("banner", MISSING)
  
  @property
  def bot(self) -> Optional[bool]:
    """Whether the user belongs to an OAuth2 application."""
    return self.__dict__.get("bot", MISSING)

  @property
  def collectibles(self) -> Optional[Nullable[Collectible]]:
    """Data for the user's collectibles."""
    if (data := self.__dict__.get("collectibles", MISSING)) in (MISSING, None): return data
    return Collectible(**data)
  
  @property
  def discriminator(self) -> str:
    """The user's Discord-tag."""
    return self.__dict__["discriminator"]
  
  @property
  def email(self) -> Optional[Nullable[str]]:
    """The user's email."""
    return self.__dict__.get("email", MISSING)
  
  @property
  def flags(self) -> Optional[UserFlags]:
    """The flags on a user's account."""
    if (data := self.__dict__.get("flags", MISSING)) is MISSING: return data
    return UserFlags(data)
  
  @property
  def global_name(self) -> Nullable[str]:
    """The user's display name, if it is set."""
    return self.__dict__["global_name"]
  
  @property
  def id(self) -> Snowflake:
    """The user's id."""
    return Snowflake(self.__dict__["id"])

  @property
  def locale(self) -> Optional[str]:
    """The user's chosen language option."""
    return self.__dict__.get("locale", MISSING)

  @property
  def mfa_enabled(self) -> Optional[bool]:
    """Whether the user has two factor enabled on their account."""
    return self.__dict__.get("mfa_enabled", MISSING)

  @property
  def premium_type(self) -> Optional[PremiumType]:
    """The type of Nitro subscription on a user's account."""
    if (data := self.__dict__.get("premium_type", MISSING)) is MISSING: return data
    return PremiumType(data)

  @property
  def primary_guild(self) -> Optional[Nullable[UserPrimaryGuild]]:
    """The user's primary guild."""
    if (data := self.__dict__.get("primary_guild", MISSING)) in (MISSING, None): return data
    return UserPrimaryGuild(**data)

  @property
  def public_flags(self) -> Optional[UserFlags]:
    """The public flags on a user's account."""
    if (data := self.__dict__.get("public_flags", MISSING)) is MISSING: return data
    return UserFlags(data)

  @property
  def system(self) -> Optional[bool]:
    """Whether the user is an Official Discord System user (part of the urgent message system)."""
    return self.__dict__.get("system", MISSING)

  @property
  def username(self) -> str:
    """The user's username, not unique across the platform."""
    return self.__dict__["username"]

  @property
  def verified(self) -> Optional[bool]:
    """Whether the email on this account has been verified."""
    return self.__dict__.get("verified", MISSING)