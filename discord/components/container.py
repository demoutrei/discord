from ..utils import Nullable, Optional
from ._base import Component, ContainerChildComponent


class ContainerComponent(Component):
  """A container is a top-level layout component. Containers offer the ability to visually encapsulate a collection of components and have an optional customizable accent color bar.

  Containers are currently only available in messages.

  .. important::
      To use this component in messages you must sent the :attr:`~discord.flags.MessageFlags.IS_COMPONENTS_V2` flag which can be activated on a per-message basis.
  """

  accent_color: Optional[Nullable[int]]
  """Color for the accent on the container sa RGB from ``0x000000`` to ``0xFFFFFF``."""

  components: list[ContainerChildComponent]
  """Child components that are encapsulated within the Container."""

  spoiler: Optional[bool]
  """Whether the container should be a spoiler (or blurred out). Defaults to ``False``."""