from ..utils import Optional
from ._base import Component, InteractiveComponent


class CheckboxComponent(Component, InteractiveComponent):
  """A checkbox is a single interactive component for simple yes/no style questions. Checkboxes are available in modals and must be placed inside a :class:`~discord.objects.components.LabelComponent`.

  .. tip::
      While you can't set a checkbox as required, you can use a :class:`~discord.objects.components.CheckboxGroupComponent` with a single option and :attr:`~discord.objects.components.CheckboxGroupComponent.required` to achieve similar functionality.
  """

  default: Optional[bool]
  """Whether the checkbox is selected by default."""