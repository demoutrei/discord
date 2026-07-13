class DiscordException(Exception):
  """Represents a Discord exception"""
  
  def __init__(self, message: str, /) -> None:
    """
    :param message: Exception message
    """
    if not isinstance(message, str):
      raise TypeError(f"message: Must be an instance of {str}; not {message.__class__}")
    super().__init__(message)
    self.__message: str = message

  @property
  def message(self) -> str:
    """Exception message"""
    return self.__message


class HTTPException(DiscordException):
  """Represents an HTTP request exception"""
  
  def __init__(self, status: int, message: str, /) -> None:
    """
    :param status: HTTP status code of the response
    :param message: HTTP status reason of the response
    """
    if not isinstance(status, int):
      raise TypeError(f"status: Must be an instance of {int}; not {status.__class__}")
    if not isinstance(message, str):
      raise TypeError(f"message: Must be an instance of {str}; not {message.__class__}")
    super().__init__(message)
    self.__status: int = status

  @property
  def status(self) -> int:
    """HTTP status code of the response"""
    return self.__status