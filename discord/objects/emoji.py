from .._dataclass import dataclass
from ..snowflake import Snowflake
from ..types import MISSING, Nullable, Optional


@dataclass
class Emoji:
  @property
  def animated(self) -> Optional[bool]:
    """Whether this emoji is animated."""
    return self.__dict__.get("animated", MISSING)

  @property
  def available(self) -> Optional[bool]:
    """Whether this emoji can be used, may be ``False`` due to loss of Server Boosts."""
    return self.__dict__.get("available", MISSING)
  
  @property
  def id(self) -> Nullable[Snowflake]:
    """Emoji ID."""
    if (data := self.__dict__["id"]) is None: return data
    return Snowflake(data)

  @property
  def managed(self) -> Optional[bool]:
    """Whether this emoji is managed."""
    return self.__dict__.get("managed", MISSING)

  @property
  def name(self) -> Nullable[str]:
    """Emoji name; can be null only in reaction emoji objects."""
    return self.__dict__["name"]

  @property
  def required_colons(self) -> Optional[bool]:
    """Whether this emoji must be wrapped in colons."""
    return self.__dict__.get("required_colons", MISSING)

  @property
  def roles(self) -> Optional[list[Snowflake]]:
    """Roles allowed to use this emoji."""
    if (data := self.__dict__.get("roles", MISSING)) is MISSING: return data
    return [Snowflake(_) for _ in data]