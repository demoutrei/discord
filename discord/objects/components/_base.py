from ..._dataclass import dataclass
from ...enums import ComponentType
from ...utils import MISSING, Optional
from typing import Any


@dataclass
class Component[T]:
  id: Optional[int]
  """32-bit integer used as an optional identifier for component."""
  
  type: ComponentType
  """The type of the component."""
  
  def __new__(cls, **data: dict[str, Any]) -> Optional[T]:
    """:meta private:"""
    match data["type"]:
      case ComponentType.ACTION_ROW:
        from .action_row import ActionRowComponent
        component_cls: T = ActionRowComponent
      case ComponentType.BUTTON:
        from .button import ButtonComponent
        component_cls: T = ButtonComponent
      case ComponentType.STRING_SELECT:
        from .string_select import StringSelectComponent
        component_cls: T = StringSelectComponent
      case ComponentType.TEXT_INPUT:
        from .text_input import TextInputComponent
        component_cls: T = TextInputComponent
      case ComponentType.USER_SELECT:
        from .user_select import UserSelectComponent
        component_cls: T = UserSelectComponent
      case ComponentType.ROLE_SELECT:
        from .role_select import RoleSelectComponent
        component_cls: T = RoleSelectComponent
      case ComponentType.MENTIONABLE_SELECT:
        from .mentionable_select import MentionableSelectComponent
        component_cls: T = MentionableSelectComponent
      case ComponentType.CHANNEL_SELECT:
        from .channel_select import ChannelSelectComponent
        component_cls: T = ChannelSelectComponent
      case ComponentType.SECTION:
        from .section import SectionComponent
        component_cls: T = SectionComponent
      case ComponentType.TEXT_DISPLAY:
        from .text_display import TextDisplayComponent
        component_cls: T = TextDisplayComponent
      case ComponentType.THUMBNAIL:
        from .thumbnail import ThumbnailComponent
        component_cls: T = ThumbnailComponent
      case ComponentType.MEDIA_GALLERY:
        from .media_gallery import MediaGalleryComponent
        component_cls: T = MediaGalleryComponent
      case ComponentType.FILE:
        from .file import FileComponent
        component_cls: T = FileComponent
      case ComponentType.SEPARATOR:
        from .separator import SeparatorComponent
        component_cls: T = SeparatorComponent
      case ComponentType.CONTAINER:
        from .container import ContainerComponent
        component_cls: T = ContainerComponent
      case ComponentType.LABEL:
        from .label import LabelComponent
        component_cls: T = LabelComponent
      case ComponentType.FILE_UPLOAD:
        from .file_upload import FileUploadComponent
        component_cls: T = FileUploadComponent
      case ComponentType.RADIO_GROUP:
        from .radio_group import RadioGroupComponent
        component_cls: T = RadioGroupComponent
      case ComponentType.CHECKBOX_GROUP:
        from .checkbox_group import CheckboxGroupComponent
        component_cls: T = CheckboxGroupComponent
      case ComponentType.CHECKBOX:
        from .checkbox import CheckboxComponent
        component_cls: T = CheckboxComponent
    component_cls: Optional[T] = MISSING
    return super().__new__(component_cls) if component_cls else MISSING


@dataclass
class InteractiveComponent:
  custom_id: str
  """Developer-defined identifier (1-100 characters)."""


class LabelChildComponent[T]:
  def __new__(cls, **data: dict[str, Any]) -> Optional[T]:
    """:meta private:"""
    match data["type"]:
      case ComponentType.TEXT_INPUT:
        from .text_input import TextInputComponent
        component_cls: T = TextInputComponent
      case ComponentType.STRING_SELECT:
        from .string_select import StringSelectComponent
        component_cls: T = StringSelectComponent
      case ComponentType.USER_SELECT:
        from .user_select import UserSelectComponent
        component_cls: T = UserSelectComponent
      case ComponentType.ROLE_SELECT:
        from .role_select import RoleSelectComponent
        component_cls: T = RoleSelectComponent
      case ComponentType.MENTIONABLE_SELECT:
        from .mentionable_select import MentionableSelectComponent
        component_cls: T = MentionableSelectComponent
      case ComponentType.CHANNEL_SELECT:
        from .channel_select import ChannelSelectComponent
        component_cls: T = ChannelSelectComponent
      case ComponentType.FILE_UPLOAD:
        from .file_upload import FileUploadComponent
        component_cls: T = FileUploadComponent
      case ComponentType.RADIO_GROUP:
        from .radio_group import RadioGroupComponent
        component_cls: T = RadioGroupComponent
      case ComponentType.CHECKBOX_GROUP:
        from .checkbox_group import CheckboxGroupComponent
        component_cls: T = CheckboxGroupComponent
      case ComponentType.CHECKBOX:
        from .checkbox import CheckboxComponent
        component_cls: T = CheckboxComponent
    component_cls: Optional[T] = MISSING
    return super().__new__(component_cls) if component_cls else MISSING