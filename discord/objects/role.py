from ..flags import PermissionFlag, RoleFlag
from ..snowflake import Snowflake
from ..utils import Nullable, Optional
from ._base import BaseObject
from .role_colors import RoleColors
from .role_tags import RoleTags


class Role(BaseObject):
  """Roles represent a set of permissions attached to a group of users."""

  color: int
  """**Deprecated**. Integer representation of hexadecimal color code.

  .. attention::
      :attr:```~.color``` will still be returned by the API, but using the :attr:```~.colors``` field is recommended when doing requests.
  """

  colors: RoleColors
  """The role's colors"""

  flags: RoleFlag
  """Role flags combined as a bitfield"""

  hoist: bool
  """If this role is pinned in the user listing"""

  icon: Optional[Nullable[str]]
  """Role icon hash"""

  id: Snowflake
  """Role ID"""

  managed: bool
  """Whether this role is managed by an integration"""

  mentionable: bool
  """Whether this role is mentionable"""

  name: str
  """Role name"""

  permissions: PermissionFlag
  """Permission bit set"""

  position: int
  """Position of this role (roles with the same position are sorted by ID)"""

  tags: Optional[RoleTags]
  """The tags this role has"""

  unicode_emoji: Optional[Nullable[str]]
  """Role unicode emoji"""