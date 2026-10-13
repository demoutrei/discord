from .._dataclass import dataclass
from ..flags import PermissionFlags, RoleFlags
from ..snowflake import Snowflake
from ..types import MISSING, Nullable, Optional
from .role_colors import RoleColors
from .role_tags import RoleTags


@dataclass
class Role:
  """Roles represent a set of permissions attached to a group of users."""

  @property
  def color(self) -> int:
    """**Deprecated**. Integer representation of hexadecimal color code.

    .. attention::
        :attr:`~.color` will still be returned by the API, but using the :attr:`~.colors` field is recommended when doing requests.
    """
    return self.__dict__["color"]

  @property
  def colors(self) -> RoleColors:
    """The role's colors."""
    return RoleColors(**self.__dict__["colors"])

  @property
  def flags(self) -> RoleFlags:
    """Role flags combined as a bitfield."""
    return RoleFlags(self.__dict__["flags"])

  @property
  def hoist(self) -> bool:
    """If this role is pinned in the user listing."""
    return self.__dict__["hoist"]

  @property
  def icon(self) -> Optional[Nullable[str]]:
    """Role icon hash."""
    return self.__dict__.get("icon", MISSING)

  @property
  def id(self) -> Snowflake:
    """Role ID."""
    return Snowflake(self.__dict__["id"])

  @property
  def managed(self) -> bool:
    """Whether this role is managed by an integration."""
    return self.__dict__["managed"]

  @property
  def mentionable(self) -> bool:
    """Whether this role is mentionable."""
    return self.__dict__["mentionable"]

  @property
  def name(self) -> str:
    """Role name."""
    return self.__dict__["name"]

  @property
  def permissions(self) -> PermissionFlags:
    """Permission bit set."""
    return PermissionFlags(int(self.__dict__["permissions"]))

  @property
  def position(self) -> int:
    """Position of this role (roles with the same position are sorted by ID)."""
    return self.__dict__["position"]

  @property
  def tags(self) -> Optional[RoleTags]:
    """The tags this role has."""
    if (data := self.__dict__.get("tags", MISSING)) is MISSING: return data
    return RoleTags(**data)

  @property
  def unicode_emoji(self) -> Optional[Nullable[str]]:
    """Role unicode emoji."""
    return self.__dict__.get("unicode_emoji", MISSING)