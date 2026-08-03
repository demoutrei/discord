from .._dataclass import dataclass


@dataclass
class IntegrationAccount:
  id: str
  """ID of the account."""
  
  name: str
  """Name of the account."""