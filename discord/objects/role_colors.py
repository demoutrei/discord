from .._dataclass import dataclass
from ..types import Nullable


@dataclass
class RoleColors:
  @property
  def primary_color(self) -> int:
    """The primary color for the role."""
    return self.__dict__["primary_color"]

  @property
  def secondary_color(self) -> Nullable[int]:
    """The secondary color for the role, this will make the role a gradient between the other provided colors."""
    return self.__dict__["secondary_color"]

  @property
  def tertiary_color(self) -> Nullable[int]:
    """The tertiary color for the role, this will turn the gradient into a holographic style."""
    return self.__dict__["tertiary_color"]