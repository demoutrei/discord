from .._dataclass import dataclass
from ..enums import StickerFormatType, StickerType
from ..snowflake import Snowflake
from ..types import MISSING, Nullable, Optional
from .user import User


@dataclass
class Sticker:
  """Represents a sticker that can be sent in messages."""

  @property
  def available(self) -> Optional[bool]:
    """Whether this guild sticker can be used, may be ``False`` due to loss of Server Boosts."""
    return self.__dict__.get("available", MISSING)

  @property
  def description(self) -> Nullable[str]:
    """Description of the sticker."""
    return self.__dict__["description"]

  @property
  def format_type(self) -> StickerFormatType:
    """Type of sticker format."""
    return StickerFormatType(self.__dict__["format_type"])

  @property
  def guild_id(self) -> Optional[Snowflake]:
    """ID of the guild that owns this sticker."""
    if (data := self.__dict__.get("guild_id", MISSING)) is MISSING: return data
    return Snowflake(data)

  @property
  def id(self) -> Snowflake:
    """ID of the sticker."""
    return Snowflake(self.__dict__["id"])

  @property
  def name(self) -> str:
    """Name of the sticker."""
    return self.__dict__["name"]

  @property
  def pack_id(self) -> Optional[Snowflake]:
    """For standard stickers, id of the pack the sticker is from."""
    if (data := self.__dict__.get("pack_id", MISSING)) is MISSING: return data
    return Snowflake(data)

  @property
  def sort_value(self) -> Optional[int]:
    """The standard sticker's sort order within its pack."""
    return self.__dict__.get("sort_value", MISSING)

  @property
  def tags(self) -> list[str]:
    """Autocomplete/suggestion tags for the sticker (max 200 characters).

    .. important::
        A comma separated list of keywords is the format used in this field by standard stickers, but this is just a convention. Incidentally the client will always use a name generated from an emoji as the value of this field when creating or modifying a guild sticker.
    """
    return self.__dict__["tags"]

  @property
  def type(self) -> StickerType:
    """Type of sticker."""
    return StickerType(self.__dict__["type"])

  @property
  def user(self) -> Optional[User]:
    """The user that uploaded the guild sticker."""
    if (data := self.__dict__.get("user", MISSING)) is MISSING: return data
    return User(**data)