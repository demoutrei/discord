from ...utils import Optional
from ._base import Component, InteractiveComponent
from .checkbox_group_option import CheckboxGroupOption


class CheckboxGroupComponent(Component, InteractiveComponent):
  """A checkbox group is an interactive component for selecting one or many options via checkboxes. Checkbox groups are available in modals and must be placed inside a :class:`~discord.objects.components.LabelComponent`."""

  max_values: Optional[int]
  """Maximum number of items that can be chosen; min 1, max 10 (defaults to the number of options)."""

  min_values: Optional[int]
  """Minimum number of items that must be chosen; min 0, max 10 (defaults to 1).

  .. important::
      Must be either omitted or at least ``1`` if :attr:`~.required` is omitted or ``True``.
  """

  options: list[CheckboxGroupOption]
  """List of options to show; min 1, max 10."""

  required: Optional[bool]
  """Whether selecting within the group is required (defaults to ``True``)."""