from ..utils import Optional
from ._base import DispatchEvent
from collections.abc import Awaitable, Callable
from inspect import iscoroutinefunction
from typing import TYPE_CHECKING
import asyncio

if TYPE_CHECKING:
  from ..client import Client


class EventManager:
  def __init__(self, client: "Client", /) -> None:
    self.__client: Client = client
    self.__listeners: dict[type[DispatchEvent], list[Callable[..., Awaitable]]] = dict()

  @property
  def _client(self) -> "Client":
    return self.__client

  def add_listener(self, name: str, callback: Callable[..., Awaitable]) -> None:
    if not isinstance(name, str):
      raise TypeError(f"name: Must be an instance of {str}; not {name.__class__}")
    name: str = name.strip()
    if not name: raise ValueError(f"name: Must not be an empty string")
    if not iscoroutinefunction(callback):
      raise TypeError(f"callback: Must be a coroutine function")
    event_cls: Optional[DispatchEvent] = DispatchEvent[name]
    if not event_cls: return
    if event_cls not in self.__listeners:
      self.__listeners[event_cls]: list[Callable[..., Awaitable]] = list()
    self.__listeners[event_cls].append(callback)

  async def dispatch(self, event: DispatchEvent) -> None:
    if event.__class__ not in self.__listeners: return
    await asyncio.gather(*[listener(event) for listener in self.__listeners[event.__class__]])