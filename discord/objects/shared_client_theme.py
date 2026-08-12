from .._dataclass import dataclass
from ..enums import BaseThemeType
from ..utils import Nullable, Optional


@dataclass
class SharedClientTheme:
  base_mix: int
  """The intensity of the theme's colors (max of 100)."""

  base_theme: Optional[Nullable[BaseThemeType]]
  """The mode of the theme."""
  
  colors: list[str]
  """The hexadecimal-encoded colors of the theme (max of 5)."""

  gradient_angle: int
  """The direction of the theme's colors (max of 360)."""