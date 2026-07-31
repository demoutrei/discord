from .._dataclass import dataclass
from ..utils import Nullable
from .welcome_screen_channel import WelcomeScreenChannel


@dataclass
class WelcomeScreen:
  description: Nullable[str]
  """The server description shown in the welcome screen"""

  welcome_channels: list[WelcomeScreenChannel]
  """The channels shown in the welcome screen, up to 5"""