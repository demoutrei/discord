from ..enums import StickerFormatType, StickerType
from ..snowflake import Snowflake
from ..utils import Nullable, Optional
from ._base import BaseObject
from .user import User


class Sticker(BaseObject):
  """Represents a sticker that can be sent in messages."""

  available: Optional[bool]
  """Whether this guild sticker can be used, may be ``False`` due to loss of Server Boosts"""

  description: Nullable[str]
  """Description of the sticker"""

  format_type: StickerFormatType
  """Type of sticker format"""

  guild_id: Optional[Snowflake]
  """ID of the guild that owns this sticker"""

  id: Snowflake
  """ID of the sticker"""

  name: str
  """Name of the sticker"""

  pack_id: Optional[Snowflake]
  """For standard stickers, id of the pack the sticker is from"""

  sort_value: Optional[int]
  """The standard sticker's sort order within its pack"""

  tags: list[str]
  """Autocomplete/suggestion tags for the sticker (max 200 characters).

  .. note::
      A comma separated list of keywords is the format used in this field by standard stickers, but this is just a convention. Incidentally the client will always use a name generated from an emoji as the value of this field when creating or modifying a guild sticker.
  """

  type: StickerType
  """Type of sticker"""

  user: Optional[User]
  """The user that uploaded the guild sticker"""