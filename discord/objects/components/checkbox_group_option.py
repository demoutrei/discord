from ..._dataclass import dataclass
from ...utils import Optional


@dataclass
class CheckboxGroupOption:
  default: Optional[bool]
  """Shows the option as selected by default."""
  
  description: Optional[str]
  """Optional description for the option; max 100 characters."""
  
  label: str
  """User-facing label of the option; max 100 characters."""
  
  value: str
  """Dev-defined value of the option; max 100 characters."""