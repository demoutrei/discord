from .._dataclass import dataclass


@dataclass
class ActivityButton:
  
  @property
  def label(self) -> str:
    """Text shown on the button (1--32 characters)."""
    return self.__dict__["label"]

  @property
  def url(self) -> str:
    """URL opened when clicking the button (1--512 characters)."""
    return self.__dict__["url"]