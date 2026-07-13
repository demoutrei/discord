from .exceptions import HTTPException
from .utils import MISSING, Nullable, Optional
from aiohttp import ClientResponse, ClientSession
from enum import StrEnum
from traceback import TracebackException
from typing import Any, Optional, Self, TYPE_CHECKING

if TYPE_CHECKING:
  from .client import Client


class RequestMethod(StrEnum):
  """String enum of request methods"""

  GET: str = "GET"


class HTTPResponse:
  """Represents an HTTP response"""

  async def __aenter__(self) -> Self:
    return self

  async def __aexit__(self, exception_type: Optional[type], exception: Optional[Exception], traceback: Optional[TracebackException]) -> None:
    if exception is not None:
      from ._logging import Logger
      Logger.error(exception)

  def __getitem__(self, key: Any, /) -> Any:
    return self.__data[key]

  def __init__(self, data: dict[str, Any], /, *, status: int, reason: str) -> None:
    """
    :param data: JSON-parsed payload from the response body
    :param status: HTTP status code of the response
    :param reason: HTTP status reason of the response
    
    :meta private:"""
    if not isinstance(data, dict):
      raise TypeError(f"data: Must be an instance of {dict}; not {data.__class__}")
    for index, key in enumerate(list(data.keys())):
      if not isinstance(key, str):
        raise TypeError(f"data.keys()[{index}]: Must be an instance of {str}; not {key.__class__}")
    if not isinstance(status, int):
      raise TypeError(f"status: Must be an instance of {int}; not {status.__class__}")
    if not isinstance(reason, str):
      raise TypeError(f"reason: Must be an instance of {str}; not {reason.__class__}")
    self.__data: dict[str, Any] = data
    self.__reason: str = reason.strip()
    self.__status: int = status

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

  async def __status_check(response: ClientResponse) -> None:
    match response.status:
      case 400:
        raise HTTPException(400, "The request was improperly formatted, or the server couldn't understand it.")
      case 401:
        raise HTTPException(401, "The 'Authorization' header was missing or invalid.")
      case 403:
        raise HTTPException(403, "The 'Authorization' token you passed did not have permission to the resource.")
      case 404:
        raise HTTPException(404, "The resource at the location specified doesn't exist.")
      case 405:
        raise HTTPException(405, "The HTTP method used is not valid for the location specified.")
      case 429:
        raise HTTPException(429, "You are being rate limited.")
      case 502:
        raise HTTPException(502, "There was not a gateway available to process your request. Wait a bit and retry.")
      case _:
        if 500 <= response.status:
          raise HTTPException(response.status, "The server had an error processing your request.")

  @property
  def _client(self) -> Client:
    """The underlying Discord client"""
    return self.__client

  async def _request(self, method: RequestMethod, endpoint: str, /, *, data: Nullable[dict[str, Any]] = None) -> HTTPResponse:
    """Performs an HTTP request to the Discord API

    :param method: Method of the request
    :param endpoint: Target endpoint of the request
    :param data: Payload to include in the request
    """
    if not isinstance(method, RequestMethod):
      raise TypeError(f"method: Must be an instance of {RequestMethod}; not {method.__class__}")
    if not isinstance(endpoint, str):
      raise TypeError(f"endpoint: Must be an instance of {str}; not {endpoint.__class__}")
    endpoint: str = endpoint.strip()
    if not endpoint:
      raise ValueError(f"endpoint: Must not be an empty string")
    if data is not None:
      if not isinstance(data, dict):
        raise TypeError(f"data: Must be an instance of {dict}; not {data.__class__}")
      for index, key in enumerate(list(data.keys())):
        if not isinstance(key, str):
          raise TypeError(f"data.keys()[{index}]: Must be an instance of {str}; not {key.__class__}")
    async with self._session.request(method, endpoint, json = data) as response:
      payload: dict[str, Any] = await response.json() or dict()
      return HTTPResponse(payload, status = response.status, reason = response.reason)

  @property
  def _session(self) -> ClientSession:
    """The current HTTP/S session"""
    if not self.__session:
      self.__session: ClientSession = ClientSession(base_url = self.__BASE_URL, raise_for_status = self.__status_check)
    return self.__session

  async def get_gateway(self) -> HTTPResponse:
    """Returns an object containing a valid WSS URL which the application can use when connecting to the gateway"""
    return await self._request(RequestMethod.GET, "gateway")

  async def get_gateway_bot(self) -> HTTPResponse:
    """Returns an object based on the information in :meth:`~.get_gateway`, plus additional metadata that can help during the operation of large or sharded bots."""
    async with await self._request(RequestMethod.GET, "gateway/bot") as response:
      from .objects import SessionStartLimitObject
      response["session_start_limit"]: SessionStartLimit = SessionStartLimitObject(**response["session_start_limit"])
      return response