from .._dataclass import dataclass


@dataclass
class ActivityButton:
  """When received over the gateway, the :attr:`~discord.objects.Activity.buttons` field is an array of strings, which are the button labels. Bots cannot access a user's activity button URLs. When sending, the :attr:`~discord.objects.Activity.buttons` field must be an array of the below object:"""
  
  label: str
  """Text shown on the button (1-32 characters)."""

  url: str
  """URL opened when clicking the button (1-512 characters)."""