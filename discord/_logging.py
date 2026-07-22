from datetime import datetime, UTC
from enum import StrEnum
from os import environ, getcwd, getenv, get_terminal_size
from sys import settrace
from traceback import FrameSummary, print_exc, TracebackException
from typing import Optional, Self


class LogColor(StrEnum):
  BG_CYAN: str     = "\033[46m"
  BG_ORANGE: str   = "\033[48;5;208m"
  BG_RED: str      = "\033[101m"
  BG_YELLOW: str   = "\033[103m"
  CYAN: str        = "\033[96m"
  ORANGE: str      = "\033[38;5;208m"
  RED: str         = "\033[91m"
  RESET: str       = "\033[0m"
  YELLOW: str      = "\033[93m"


class LogType(StrEnum):
  DEBUG: str = "DEBUG"
  ERROR: str = "ERROR"
  INFO: str  = " INFO"
  WARN: str  = " WARN"


class Logger:
  """Singleton logger instance"""
  
  __allow_logging: bool = getenv("demoutrei.discord::with_logger") is not None
  __debug_flag: bool = bool(getenv("demoutrei.discord::debug_enabled", False))

  def __enter__(self) -> Self:
    self.__in_context_manager: bool = True
    settrace(None)
    return self

  def __exit__(self, exception_type: Optional[type[BaseException]], exception: Optional[BaseException], traceback: Optional[TracebackException]) -> bool:
    if exception is not None and exception_type is not KeyboardInterrupt:
      self.error(exception)
      return True
    self.log()

  def __context_manager_check(self, frame, event, argument):
    if not self.__in_context_manager and event == "return":
      self.log()
      settrace(None)
    return self.__context_manager_check

  @property
  def character_limit(self) -> int:
    """:meta private:"""
    return max(self.columns - (len(str(self.timestamp)) + 11), 75)

  @property
  def columns(self) -> int:
    """:meta private:"""
    return get_terminal_size().columns

  @classmethod
  def debug(cls, *messages: str) -> Self:
    """:param messages: Messages to log as DEBUG level"""
    if not messages:
      raise ValueError(f"messages: Must pass at least one message")
    messages: list[str] = list(messages)
    for index, message in enumerate(messages):
      if not isinstance(message, str):
        raise TypeError(f"messages[{index}]: Must be an instance of {str}; not {message.__class__}")
      messages[index]: str = message.strip()
    instance: Self = super().__new__(cls)
    instance.__in_context_manager: bool = False
    instance.__messages: list[str] = messages
    instance.__type: LogType = LogType.DEBUG
    settrace(instance._Logger__context_manager_check)
    return instance

  @classmethod
  def error(cls, exception: BaseException, /) -> Self:
    """:param exception: Exception to log as ERROR level"""
    if not isinstance(exception, BaseException):
      raise TypeError(f"exception: Must be an instance of {BaseException}; not {exception.__class__}")
    instance: Self = super().__new__(cls)
    instance.__exception: BaseException = exception
    instance.__in_context_manager: bool = False
    instance.__type: LogType = LogType.ERROR
    settrace(instance._Logger__context_manager_check)
    return instance

  def get_prefix(self, *, with_level: bool = True, with_timestamp: bool = True) -> str:
    """:meta private:"""
    if not isinstance(self.log_type, LogType):
      raise TypeError(f"Logger.log_type: Must be an instance of {LogType}; not {self.log_type.__class__}")
    if not isinstance(with_level, bool):
      raise TypeError(f"with_level: Must be an instance of {bool}; not {with_level.__class__}")
    if not isinstance(with_timestamp, bool):
      raise TypeError(f"with_timestamp: Must be an instance of {bool}; not {with_timestamp.__class__}")
    level: str = f"[{f"{self.log_type}":^5}]"
    if not with_level:
      level: str = " " * len(level)
    timestamp: str = self.timestamp
    if not with_timestamp:
      timestamp: str = " " * len(timestamp)
    match self.log_type:
      case LogType.DEBUG:
        color, bg = LogColor.YELLOW, LogColor.BG_YELLOW
      case LogType.ERROR:
        color, bg = LogColor.RED, LogColor.BG_RED
      case LogType.INFO:
        color, bg = LogColor.CYAN, LogColor.BG_CYAN
      case LogType.WARN:
        color, bg = LogColor.ORANGE, LogColor.BG_ORANGE
    return f"{color}{timestamp} {bg} {LogColor.RESET}{color} {level}{LogColor.RESET}"

  @classmethod
  def info(cls, *messages: str) -> Self:
    """:param messages: Messages to log as INFO level"""
    if not messages:
      raise ValueError(f"messages: Must pass at least one message")
    messages: list[str] = list(messages)
    for index, message in enumerate(messages):
      if not isinstance(message, str):
        raise TypeError(f"messages[{index}]: Must be an instance of {str}; not {message.__class__}")
      messages[index]: str = message.strip()
    instance: Self = super().__new__(cls)
    instance.__in_context_manager: bool = False
    instance.__messages: list[str] = messages
    instance.__type: LogType = LogType.INFO
    settrace(instance._Logger__context_manager_check)
    return instance

  @property
  def lines(self) -> int:
    """:meta private:"""
    return get_terminal_size().lines

  def log(self) -> None:
    """:meta private:"""
    print(f"{self.get_prefix()} {f"\n{self.get_prefix(with_level = False, with_timestamp = False)} ".join([message for message in self.messages])}")

  @property
  def log_type(self) -> LogType:
    """:meta private:"""
    return self.__type

  @property
  def messages(self) -> list[str]:
    """:meta private:"""
    if self.log_type is LogType.ERROR:
      traceback: TracebackException = TracebackException.from_exception(self.__exception, capture_locals = True, max_group_depth = 100, max_group_width = 100)
      frame: FrameSummary = None
      for stack in traceback.stack[::-1]:
        if stack.filename.startswith(getcwd()) and not (stack.filename.startswith(f"{getcwd()}\\\\venv") or stack.filename.startswith(f"{getcwd()}\\venv")):
          frame: FrameSummary = stack
          break
      if not frame:
        frame: FrameSummary = traceback.stack[-1]
      message: str = f"{frame.filename.replace(f"{getcwd()}\\".replace("\\\\", ""), "")}:{frame.lineno}\n" \
        f"{self.split(frame.line, indent = False, indent_space = 2)}\n" \
        f"{self.__exception.__class__.__name__}: {traceback}"
      message: str = message.replace("\n", f"\n{self.get_prefix(with_level = False, with_timestamp = False)} ")
      return [message]
    return [self.split(message) for message in self.__messages]

  def split(self, message: str, /, *, indent: bool = True, indent_space: int = 0) -> str:
    """:meta private:"""
    if not isinstance(message, str):
      raise TypeError(f"message: Must be an instance of {str}; not {message.__class__}")
    if not isinstance(indent, bool):
      raise TypeError(f"indent: Must be an instance of {bool}; not {indent.__class__}")
    if not isinstance(indent_space, int):
      raise TypeError(f"indent_space: Must be an instance of {int}; not {indent_space.__class__}")
    if indent_space < 0:
      raise ValueError(f"indent_space: Must be greater than or equal to 0")
    if not message.strip(): return message
    sections: list[str] = list()
    for i in range((len(message) // self.character_limit) + 1):
      index: int = (self.character_limit - indent_space) * i
      position: int = index + (self.character_limit - indent_space)
      section: str = f"{" " * indent_space}{message[index:position]}"
      sections.append(section)
    return f"\n{f"{self.get_prefix(with_level = False, with_timestamp = False)}" if indent else str()}".join(sections)

  @property
  def timestamp(self) -> str:
    """:meta private:"""
    return datetime.now().strftime(r"%Y-%m-%d %H:%M:%S")

  @classmethod
  def warn(cls, *messages: str) -> Self:
    """:param messages: Messages to log as WARN level"""
    if not messages:
      raise ValueError(f"messages: Must pass at least one message")
    messages: list[str] = list(messages)
    for index, message in enumerate(messages):
      if not isinstance(message, str):
        raise TypeError(f"messages[{index}]: Must be an instance of {str}; not {message.__class__}")
      messages[index]: str = message.strip()
    instance: Self = super().__new__(cls)
    instance.__in_context_manager: bool = False
    instance.__messages: list[str] = messages
    instance.__type: LogType = LogType.WARN
    settrace(instance._Logger__context_manager_check)
    return instance