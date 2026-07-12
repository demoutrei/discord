from .utils import MISSING, Nullable, Optional
from aiohttp import ClientResponse, ClientSession
from enum import StrEnum
from typing import Any, Self, TYPE_CHECKING

if TYPE_CHECKING:
  from .client import Client


class RequestMethod(StrEnum):
  """String enum of request methods"""

  GET: str = "GET"


class HTTPResponse:
  """Represents an HTTP response"""

  def __init__(self, payload: dict[str, Any], /, *, status: int, reason: str) -> None:
    """

    :param payload: JSON-parsed payload from the response body
    :param status: HTTP status code of the response
    :param reason: HTTP status reason of the response
    
    :meta private:"""
    if not isinstance(payload, dict):
      raise TypeError(f"payload: Must be an instance of {dict}; not {payload.__class__}")
    for index, key in enumerate(list(payload.keys())):
      if not isinstance(key, str):
        raise TypeError(f"payload.keys()[{index}]: Must be an instance of {str}; not {key.__class__}")
    if not isinstance(status, int):
      raise TypeError(f"status: Must be an instance of {int}; not {status.__class__}")
    if not isinstance(reason, str):
      raise TypeError(f"reason: Must be an instance of {str}; not {reason.__class__}")
    self.__payload: dict[str, Any] = payload
    self.__reason: str = reason.strip()
    self.__status: int = status

  @property
  def payload(self) -> dict[str, Any]:
    """JSON-parsed payload from the response body"""
    return self.__payload

  @property
  def reason(self) -> str:
    """HTTP status reason of the response"""
    return self.__reason

  @property
  def status(self) -> int:
    """HTTP status code of the response"""
    return self.__status


class HTTP:
  """Represents an HTTP/S connection to the Discord API"""

  __BASE_URL: str = f"https://discord.com/api/v10/"
  """Discord API base URL

  :meta private:
  """

  __instance: Optional[Self] = MISSING
  """Singleton HTTP instance

  :meta private:
  """

  def __new__(cls: type[Self], client: Client, /) -> Self:
    """HTTP constructor

    :param client: The underlying Discord client
    """
    if not cls.__instance:
      from .client import Client
      if not isinstance(client, Client):
        raise TypeError(f"client: Must be an instance of {Client}; not {client.__class__}")
      instance: Self = super().__new__(cls)
      instance.__client: Client = client
      instance.__session: ClientSession = MISSING
      cls.__instance: Self = instance
    return cls.__instance

  @property
  def _client(self) -> Client:
    """The underlying Discord client"""
    return self.__client

  async def _request(self, method: RequestMethod, endpoint: str, /, *, payload: Nullable[dict[str, Any]] = None) -> HTTPResponse:
    """Performs an HTTP request to the Discord API

    :param method: Method of the request
    :param endpoint: Target endpoint of the request
    :param payload: Payload to include in the request
    """
    if not isinstance(method, RequestMethod):
      raise TypeError(f"method: Must be an instance of {RequestMethod}; not {method.__class__}")
    if not isinstance(endpoint, str):
      raise TypeError(f"endpoint: Must be an instance of {str}; not {endpoint.__class__}")
    endpoint: str = endpoint.strip()
    if not endpoint:
      raise ValueError(f"endpoint: Must not be an empty string")
    if payload is not None:
      if not isinstance(payload, dict):
        raise TypeError(f"payload: Must be an instance of {dict}; not {payload.__class__}")
      for index, key in enumerate(list(payload.keys())):
        if not isinstance(key, str):
          raise TypeError(f"payload.keys()[{index}]: Must be an instance of {str}; not {key.__class__}")
    async with self._session.request(method, endpoint, json = payload) as response:
      payload: dict[str, Any] = await response.json() or dict()
      return HTTPResponse(payload, status = response.status, reason = response.reason)

  @property
  def _session(self) -> ClientSession:
    """The current HTTP/S session"""
    if not self.__session:
      self.__session: ClientSession = ClientSession(base_url = self.__BASE_URL)
    return self.__session

  async def get_gateway(self) -> str:
    """Returns a valid WSS URL which the application can use when connecting to the gateway"""
    response: HTTPResponse = await self._request(RequestMethod.GET, "gateway")
    return response.payload["url"]