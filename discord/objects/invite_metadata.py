from .._dataclass import dataclass
from ..utils import ISO8601Timestamp


@dataclass
class InviteMetadata:
  """Extra information about an invite, will extend the :class:`~discord.objects.Invite` object."""

  created_at: ISO8601Timestamp
  """When this invite was created."""

  max_age: int
  """Duration in (seconds) after which the invite expires."""

  max_uses: int
  """Maximum number of times this invite can be used."""

  temporary: bool
  """Whether this invite only grants temporary membership."""

  uses: int
  """Number of times this invite has been used."""