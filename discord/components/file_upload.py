from ..utils import Optional
from ._base import Component, InteractiveComponent


class FileUploadComponent(Component, InteractiveComponent):
  """File upload is an interactive component that allows users to upload files in modals. File Uploads can be configured to have a minimum and maximum number of files between 0 and 10, along with :attr:`~.required` for if the upload is required to submit the modal. The max file size a user can upload is based on the user's upload limit in that channel.

  File uploads are available on modals. They must be placed in a :class:`~discord.objects.components.LabelComponent`.
  """

  file_types: Optional[list[str]]
  """File types to filter for: can be ``image``, ``video``, ``audio``, or any dot-prefixed extension such as ``.pdf``; max 10.

  .. note::
      Only matches against the file extension.
  """

  max_values: Optional[int]
  """Maximum number of items that can be uploaded (defaults to 1); max 10."""

  min_values: Optional[int]
  """Minimum number of items that must be uploaded (defaults to 1); min 0, max 10.

  .. important::
      Must be either omitted or at least ``1`` if :attr:`~.required` is omitted or ``True``.
  """

  required: Optional[bool]
  """Whether the file upload requires files to be uploaded before submitting the modal (defaults to ``True``)."""