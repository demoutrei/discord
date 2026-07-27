from ..objects import Channel
from ..utils import Optional


class ThreadCreateEvent(Channel):
  newly_created: Optional[bool]