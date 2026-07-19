from ..utils import Nullable
from ._base import BaseObject
from .welcome_screen_channel import WelcomeScreenChannel


class WelcomeScreen(BaseObject):
  description: Nullable[str]
  """The server description shown in the welcome screen"""

  welcome_channels: list[WelcomeScreenChannel]
  """The channels shown in the welcome screen, up to 5"""