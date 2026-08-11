from ..utils import Optional
from ._base import Component, InteractiveComponent
from .radio_group_option import RadioGroupOption


class RadioGroupComponent(Component, InteractiveComponent):
  """A radio group is an interactive component for selecting exactly one option from a defined list. Radio groups are available in modals and must be placed inside a :class:`~discord.objects.components.LabelComponent`."""

  options: list[RadioGroupOption]
  """List of options to show; min 2, max 10."""

  required: Optional[bool]
  """Whether a selection is required to submit the modal (defaults to ``True``)."""