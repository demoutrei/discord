from ..utils import Optional
from ._base import Component


class Separator(Component):
  """A separator is a top-level layout component that adds vertical padding and visual division between other components.

  Separators are currently only available in messages.

  .. important::
      To use this component in messages you must send the :attr:`~discord.flags.MessageFlags.IS_COMPONENTS_V2` message flag which can be activated on a per-message basis.
  """

  divider: Optional[bool]
  """Whether a visual divider should be displayed in the component. Defaults to ``True``."""

  spacing: Optional[int]
  """Size of separator padding--``1`` for small padding, ``2`` for large padding Defaults to ``1``."""