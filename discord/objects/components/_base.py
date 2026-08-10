from .._dataclass import dataclass
from ..enums import ComponentType
from ..utils import MISSING, Optional


@dataclass
class Component:
  id: Optional[int]
  """32-bit integer used as an optional identifier for component."""
  
  type: ComponentType
  """The type of the component."""
  
  def __class_getitem__(cls, component_type: int) -> Optional[type]:
    """:meta private:"""
    if not isinstance(component_type, int):
      raise TypeError(f"component_type: Must be an instance of {int}; not {component_type.__class__}")
    if component_type < 0:
      raise ValueError(f"component_type: Must be greater than or equal to 0")
    match component_type:
      case ComponentType.ACTION_ROW:
        from .action_row import ActionRowComponent
        return ActionRowComponent
      case ComponentType.BUTTON:
        from .button import ButtonComponent
        return ButtonComponent
      case ComponentType.STRING_SELECT:
        from .string_select import StringSelectComponent
        return StringSelectComponent
      case ComponentType.TEXT_INPUT:
        from .text_input import TextInputComponent
        return TextInputComponent
      case ComponentType.USER_SELECT:
        from .user_select import UserSelectComponent
        return UserSelectComponent
      case ComponentType.ROLE_SELECT:
        from .role_select import RoleSelectComponent
        return RoleSelectComponent
      case ComponentType.MENTIONABLE_SELECT:
        from .mentionable_select import MentionableSelectComponent
        return MentionableSelectComponent
      case ComponentType.CHANNEL_SELECT:
        from .channel_select import ChannelSelectComponent
        return ChannelSelectComponent
      case ComponentType.SECTION:
        from .section import SectionComponent
        return SectionComponent
      case ComponentType.TEXT_DISPLAY:
        from .text_display import TextDisplayComponent
        return TextDisplayComponent
      case ComponentType.THUMBNAIL:
        from .thumbnail import ThumbnailComponent
        return ThumbnailComponent
      case ComponentType.MEDIA_GALLERY:
        from .media_gallery import MediaGalleryComponent
        return MediaGalleryComponent
      case ComponentType.FILE:
        from .file import FileComponent
        return FileComponent
      case ComponentType.SEPARATOR:
        from .separator import SeparatorComponent
        return SeparatorComponent
      case ComponentType.CONTAINER:
        from .container import ContainerComponent
        return ContainerComponent
      case ComponentType.LABEL:
        from .label import LabelComponent
        return LabelComponent
      case ComponentType.FILE_UPLOAD:
        from .file_upload import FileUploadComponent
        return FileUploadComponent
      case ComponentType.RADIO_GROUP:
        from .radio_group import RadioGroupComponent
        return RadioGroupComponent
      case ComponentType.CHECKBOX_GROUP:
        from .checkbox_group import CheckboxGroupComponent
        return CheckboxGroupComponent
      case ComponentType.CHECKBOX:
        from .checkbox import CheckboxComponent
        return CheckboxComponent
    return MISSING


@dataclass
class InteractiveComponent:
  custom_id: str
  """Developer-defined identifier (1-100 characters)."""