from .._dataclass import dataclass
from ..flags import AttachmentFlags
from ..snowflake import Snowflake
from ..utils import ISO8601Timestamp, Nullable, Optional
from .application import Application
from .user import User


@dataclass
class Attachment:
  application: Optional[Nullable[Application]]
  """For Clips, the application in the stream, if recognized."""
  
  clip_created_at: Optional[ISO8601Timestamp]
  """For Clips, when the clip was created."""
  
  clip_participants: Optional[list[User]]
  """For Clips, array of users who were in the stream."""
  
  content_type: Optional[str]
  """The attachment's media type."""
  
  description: Optional[str]
  """Description (alt text) for the file (max 1024 characters)."""
  
  duration_secs: Optional[float]
  """The duration of the audio or video file."""
  
  ephemeral: Optional[bool]
  """Whether this attachment is ephemeral.

  .. hint::
      Ephemeral attachments will automatically be removed after a set period of time. Ephemeral attachments on messages are guaranteed to be available as long as the message itself exists.
  """
  
  filename: str
  """Name of file attached."""

  flags: Optional[AttachmentFlags]
  """Attachment flags combiend as a bitfield."""
  
  height: Optional[Nullable[int]]
  """Height of file (if image or video)."""
  
  id: Snowflake
  """Attachment ID."""

  placeholder: Optional[str]
  """Thumbhash placeholder (if image or video)."""

  placeholder_version: Optional[int]
  """Version of the placeholder (if image or video)."""

  proxy_url: str
  """A proxied URL of file."""

  size: int
  """Size of file in bytes."""

  title: Optional[str]
  """The title of the file."""

  url: str
  """Source URL of file."""

  waveform: Optional[str]
  """Base64-encoded bytearray representing a sampled waveform (currently for voice messages)."""

  width: Optional[Nullable[int]]
  """Width of file (if image or video)."""