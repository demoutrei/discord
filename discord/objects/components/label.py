from ...utils import Optional
from ._base import Component, LabelChildComponent


class LabelComponent(Component):
  """A label is a top-level layout component. Labels wrap modal components with text as a label and optional description.

  .. note::
      The :attr:`~.description` may display above or below the :attr:`~.component` depending on the platform.
  """

  component: LabelChildComponent
  """The component within the label."""

  description: Optional[str]
  """An optional description text for the label; max 100 characters."""

  label: str
  """The label text; max 45 characters."""