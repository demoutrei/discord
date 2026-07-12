from ._base import BaseObject


class SessionStartLimitObject(BaseObject):
  max_concurrency: int
  """Number of identify requests allowed per 5 seconds"""
  
  remaining: int
  """Remaining number of session starts the current user is allowed"""

  reset_after: int
  """Number of milliseconds after which the limit resets"""
  
  total: int
  """Total number of session starts the current user is allowed"""