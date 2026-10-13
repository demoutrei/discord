from .._dataclass import dataclass
from ..types import Nullable
from .welcome_screen_channel import WelcomeScreenChannel


@dataclass
class WelcomeScreen:
  @property
  def description(self) -> Nullable[str]:
    """The server description shown in the welcome screen."""
    return self.__dict__["description"]

  @property
  def welcome_channels(self) -> list[WelcomeScreenChannel]:
    """The channels shown in the welcome screen, up to 5."""
    return [WelcomeScreenChannel(**data) for data in self.__dict__["welcome_channels"]]