from datetime import datetime, UTC
from enum import StrEnum
from os import environ, getcwd, getenv, get_terminal_size
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
  __debug: bool = False
  __instance: Optional[Self] = None

  def __new__(cls: type[Self], *args, **kwargs) -> Optional[Self]:
    if getenv("demoutrei.discord::with_logger") is None:
      return None
    if cls.__instance is None:
      cls.__instance: Self = super().__new__(cls)
      cls.__debug: bool = bool(getenv("demoutrei.discord::debug_enabled", False))
    return cls.__instance

  @property
  def character_limit(self) -> int:
    return max(self.columns - (len(str(self.timestamp)) + 11), 75)

  @property
  def columns(self) -> int:
    return get_terminal_size().columns

  @staticmethod
  def debug(*messages: str) -> None:
    if not Logger(): return
    try:
      if not messages: return
      for index, message in enumerate(messages):
        if not isinstance(message, str):
          raise TypeError(f"messages[{index}]: Must be an instance of {str}; not {message.__class__}")
      if not Logger._Logger__debug: return
      Logger._Logger__instance.log(tuple(Logger._Logger__instance.split(message.strip(), log_type = LogType.DEBUG) for message in messages), log_type = LogType.DEBUG)
    except Exception as exception:
      Logger.error(exception)

  @staticmethod
  def error(exception: Exception) -> None:
    if not Logger(): return
    try:
      if not isinstance(exception, Exception):
        raise TypeError(f"exception: Must be an instance of {Exception}; not {exception.__class__}")
      traceback: TracebackException = TracebackException.from_exception(exception, capture_locals = True, max_group_depth = 100, max_group_width = 100)
      frame: FrameSummary = None
      for stack in traceback.stack[::-1]:
        if stack.filename.startswith(getcwd()) and not (stack.filename.startswith(f"{getcwd()}\\\\venv") or stack.filename.startswith(f"{getcwd()}\\venv")):
          frame: FrameSummary = stack
          break
      if not frame:
        frame: FrameSummary = traceback.stack[-1]
      log_message: str = f"{frame.filename.replace(f"{getcwd()}\\".replace("\\\\", ""), "")}:{frame.lineno}\n" \
        f"{Logger._Logger__instance.split(frame.line, log_type = LogType.ERROR, indent = False, indent_space = 2)}\n" \
        f"{exception.__class__.__name__}: {traceback}"
      Logger._Logger__instance.log((log_message.replace("\n", f"\n{Logger._Logger__instance.get_prefix(LogType.ERROR, with_level = False, with_timestamp = False)} "), ), log_type = LogType.ERROR)
    except Exception as exception:
      Logger.error(exception)

  def get_prefix(self, log_type: LogType, *, with_level: bool = True, with_timestamp: bool = True) -> str:
    if not isinstance(log_type, LogType):
      raise TypeError(f"log_type: Must be an instance of {LogType}; not {log_type.__class__}")
    if not isinstance(with_level, bool):
      raise TypeError(f"with_level: Must be an instance of {bool}; not {with_level.__class__}")
    if not isinstance(with_timestamp, bool):
      raise TypeError(f"with_timestamp: Must be an instance of {bool}; not {with_timestamp.__class__}")
    level: str = f"[{f"{log_type}":^5}]"
    if not with_level:
      level: str = " " * len(level)
    timestamp: str = self.timestamp
    if not with_timestamp:
      timestamp: str = " " * len(timestamp)
    match log_type:
      case LogType.DEBUG:
        color, bg = LogColor.YELLOW, LogColor.BG_YELLOW
      case LogType.ERROR:
        color, bg = LogColor.RED, LogColor.BG_RED
      case LogType.INFO:
        color, bg = LogColor.CYAN, LogColor.BG_CYAN
      case LogType.WARN:
        color, bg = LogColor.ORANGE, LogColor.BG_ORANGE
    return f"{color}{timestamp} {bg} {LogColor.RESET}{color} {level}{LogColor.RESET}"

  @staticmethod
  def info(*messages: str) -> None:
    if not Logger(): return
    try:
      if not messages: return
      for index, message in enumerate(messages):
        if not isinstance(message, str):
          raise TypeError(f"messages[{index}]: Must be an instance of {str}; not {message.__class__}")
      Logger._Logger__instance.log(tuple(Logger._Logger__instance.split(message.strip(), log_type = LogType.INFO) for message in messages), log_type = LogType.INFO)
    except Exception as exception:
      Logger.error(exception)

  @property
  def lines(self) -> int:
    return get_terminal_size().lines

  def log(self, messages: tuple[str], *, log_type: LogType = LogType.INFO) -> None:
    try:
      if not isinstance(messages, tuple):
        raise TypeError(f"messages: Must be an instance of {tuple}; not {messages.__class__}")
      if not messages: return
      for index, message in enumerate(messages):
        if not isinstance(message, str):
          raise TypeError(f"messages[{index}]: Must be an instance of {str}; not {message.__class__}")
      if not isinstance(log_type, LogType):
        raise TypeError(f"log_type: Must be an instance of {LogType}; not {log_type.__class__}")
      print(f"{self.get_prefix(log_type)} {f"\n{self.get_prefix(log_type, with_level = False, with_timestamp = False)} ".join([message for message in messages])}")
    except Exception as exception:
      self.error(exception)

  def split(self, message: str, *, log_type: LogType, indent: bool = True, indent_space: int = 0) -> str:
    try:
      if not isinstance(message, str):
        raise TypeError(f"message: Must be an instance of {str}; not {message.__class__}")
      if not isinstance(log_type, LogType):
        raise TypeError(f"log_type: Must be an instance of {LogType}; not {log_type.__class__}")
      if not message.strip(): return message
      sections: list[str] = list()
      for i in range((len(message) // self.character_limit) + 1):
        index: int = (self.character_limit - indent_space) * i
        position: int = index + (self.character_limit - indent_space)
        section: str = f"{" " * indent_space}{message[index:position]}"
        sections.append(section)
      return f"\n{f"{self.get_prefix(log_type, with_level = False, with_timestamp = False)}" if indent else str()}".join(sections)
    except Exception as exception:
      Logger.error(exception)

  @property
  def timestamp(self) -> str:
    return datetime.now().strftime(r"%Y-%m-%d %H:%M:%S")

  @staticmethod
  def warn(*messages: str) -> None:
    if not Logger(): return
    try:
      if not messages: return
      for index, message in enumerate(messages):
        if not isinstance(message, str):
          raise TypeError(f"message[{index}]: Must be an instance of {str}; not {message.__class__}")
      Logger._Logger__instance.log(tuple(Logger._Logger__instance.split(message.strip(), log_type = LogType.WARN) for message in messages), log_type = LogType.WARN)
    except Exception as exception:
      Logger.error(exception)