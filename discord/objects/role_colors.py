from ..utils import Nullable
from ._base import BaseObject


class RoleColors(BaseObject):
  primary_color: int
  """The primary color for the role"""

  secondary_color: Nullable[int]
  """The secondary color for the role, this will make the role a gradient between the other provided colors"""

  tertiary_color: Nullable[int]
  """The tertiary color for the role, this will turn the gradient into a holographic style"""