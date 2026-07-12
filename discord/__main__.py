from discord import Logger
from os import environ, system
from pathlib import Path
from sys import argv, executable, modules
import subprocess


if len(argv) < 2:
  raise ValueError("Missing required file")
  
def main() -> None:
  try:
    file_path: str = Path(argv[1])
    if not file_path.exists():
      raise FileNotFoundError(f"{file_path!r} is invalid, inaccessible, or missing")
    _new_ = environ.copy()
    _new_["demoutrei.discord::with_logger"]: str = "true"
    if ("-d" in argv) or ("--debug" in argv):
      _new_["demoutrei.discord::debug_enabled"]: str = "true"
    system("cls")
    subprocess.run([executable, file_path], env = _new_)
  except KeyboardInterrupt: pass
  except Exception as exception:
    Logger.error(exception)