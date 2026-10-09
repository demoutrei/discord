from .._dataclass import dataclass


@dataclass
class ActivityButton:
  label: str
  """Text shown on the button (1--32 characters)."""

  url: str
  """URL opened when clicking the button (1--512 characters)."""