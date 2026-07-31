from .._dataclass import dataclass
from ..snowflake import Snowflake
from ..utils import Optional


@dataclass
class OptionalAuditEntryInfo:
  application_id: Optional[Snowflake]
  """ID of the app whose permissions were targeted.

  **Event types**: :attr:`~discord.enums.AuditLogEvent.APPLICATION_COMMAND_PERMISSION_UPDATE`
  """

  auto_moderation_rule_name: Optional[str]
  """Name of the Auto Moderation rule that was triggered.

  **Event types**: :attr:`~discord.enums.AuditLogEvent.AUTO_MODERATION_BLOCK_MESSAGE` & :attr:`~discord.enums.AuditLogEvent.AUTO_MODERATION_FLAG_TO_CHANNEL` & :attr:`~discord.enums.AuditLogEvent.AUTO_MODERATION_USER_COMMUNICATION_DISABLED` & :attr:`~discord.enums.AuditLogEvent.AUTO_MODERATION_QUARANTINE_USER`
  """

  auto_moderation_rule_trigger_type: Optional[str]
  """Trigger type of the Auto Moderation rule that was triggered.

  **Event types**: :attr:`~discord.enums.AuditLogEvent.AUTO_MODERATION_BLOCK_MESSAGE` & :attr:`~discord.enums.AuditLogEvent.AUTO_MODERATION_FLAG_TO_CHANNEL` & :attr:`~discord.enums.AuditLogEvent.AUTO_MODERATION_USER_COMMUNICATION_DISABLED` & :attr:`~discord.enums.AuditLogEvent.AUTO_MODERATION_QUARANTINE_USER`
  """

  channel_id: Optional[Snowflake]
  """Channel in which the entities were targeted.

  **Event types**: :attr:`~discord.enums.AuditLogEvent.MEMBER_MOVE` & :attr:`~discord.enums.AuditLogEvent.MESSAGE_PIN` & :attr:`~discord.enums.AuditLogEvent.MESSAGE_UNPIN` & :attr:`~discord.enums.AuditLogEvent.MESSAGE_DELETE` & :attr:`~discord.enums.AuditLogEvent.STAGE_INSTANCE_CREATE` & :attr:`~discord.enums.AuditLogEvent.STAGE_INSTANCE_UPDATE` & :attr:`~discord.enums.AuditLogEvent.STAGE_INSTANCE_DELETE` & :attr:`~discord.enums.AuditLogEvent.AUTO_MODERATION_BLOCK_MESSAGE` & :attr:`~discord.enums.AuditLogEvent.AUTO_MODERATION_BLOCK_MESSAGE` & :attr:`~discord.enums.AuditLogEvent.AUTO_MODERATION_FLAG_TO_CHANNEL` & :attr:`~discord.enums.AuditLogEvent.AUTO_MODERATION_USER_COMMUNICATION_DISABLED` & :attr:`~discord.enums.AuditLogEvent.AUTO_MODERATION_QUARANTINE_USER` & :attr:`~discord.enums.AuditLogEvent.VOICE_CHANNEL_STATUS_CREATE` & :attr:`~discord.enums.AuditLogEvent.VOICE_CHANNEL_STATUS_DELETE`
  """

  count: Optional[str]
  """Number of entitites that were targeted.

  **Event types**: :attr:`~discord.enums.AuditLogEvent.MESSAGE_DELETE` & :attr:`~discord.enums.AuditLogEvent.MESSAGE_BULK_DELETE` & :attr:`~discord.enums.AuditLogEvent.MEMBER_DISCONNECT` & :attr:`~discord.enums.AuditLogEvent.MEMBER_MOVE`
  """

  delete_member_days: Optional[str]
  """Number of days after which inactive members were kicked.

  **Event types**: :attr:`~discord.enums.AuditLogEvent.MEMBER_PRUNE`
  """

  id: Optional[Snowflake]
  """ID of the overwritten entity.

  **Event types**: :attr:`~discord.enums.AuditLogEvent.CHANNEL_OVERWRITE_CREATE` & :attr:`~discord.enums.AuditLogEvent.CHANNEL_OVERWRITE_UPDATE` & :attr:`~discord.enums.AuditLogEvent.CHANNEL_OVERWRITE_DELETE`
  """

  integration_type: Optional[str]
  """The type of integration which performed the action.

  **Event types**: :attr:`~discord.enums.AuditLogEvent.MEMBER_KICK` & :attr:`~discord.enums.AuditLogEvent.MEMBER_ROLE_UPDATE`
  """

  members_removed: Optional[str]
  """Number of members removed by the prune.

  **Event types**: :attr:`~discord.enums.AuditLogEvent.MEMBER_PRUNE`
  """

  message_id: Optional[Snowflake]
  """ID of the message that was targeted.

  **Event types**: :attr:`~discord.enums.AuditLogEvent.MESSAGE_PIN` & :attr:`~discord.enums.AuditLogEvent.MESSAGE_UNPIN`
  """

  role_name: Optional[str]
  """Name of the role if :attr:`~.type` is ``"0"`` (not present if type is ``"1"``).

  **Event types**: :attr:`~discord.enums.AuditLogEvent.CHANNEL_OVERWRITE_CREATE` & :attr:`~discord.enums.AuditLogEvent.CHANNEL_OVERWRITE_UPDATE` & :attr:`~discord.enums.AuditLogEvent.CHANNEL_OVERWRITE_DELETE`
  """

  status: Optional[str]
  """The new voice channel status.

  **Event types**: :attr:`~discord.enums.AuditLogEvent.VOICE_CHANNEL_STATUS_CREATE`
  """

  type: Optional[str]
  """Type of overwritten entity - role (``"0"``) or member (``"1"``).

  **Event types**: :attr:`~discord.enums.AuditLogEvent.CHANNEL_OVERWRITE_CREATE`` & :attr:`~discord.enums.AuditLogEvent.CHANNEL_OVERWRITE_UPDATE` & :attr:`~discord.enums.AuditLogEvent.CHANNEL_OVERWRITE_DELETE`
  """