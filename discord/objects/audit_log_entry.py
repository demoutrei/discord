from .._dataclass import dataclass
from ..enums import AuditLogEvent
from ..snowflake import Snowflake
from ..utils import Nullable, Optional
from .audit_log_change import AuditLogChange
from .optional_audit_entry_info import OptionalAuditEntryInfo


@dataclass
class AuditLogEntry:
  """Each audit log entry represents a single administrative action (or event), indicated by :attr:`~.action_type`. Most entries contain one to many changes in the :attr:`~.changes` array that affected an entity in Discord--whether that's a user, channel, guild, emoji, or something else.

  Apps can specify why an administrative action is being taken by passing an ``X-Audit-Log-Reason`` request header, which will be stored as the audit log entry's :attr:`~.reason` field. The ``X-Audit-Log-Reason`` header supports 1-512 URL-encoded UTF-8 characters. Reasons are visible to users in the client and to apps when fetching audit log entries with the API.
  
  .. hint::
      For :attr:`~discord.enums.AuditLogEvent.APPLICATION_COMMAND_PERMISSION_UPDATE` events, the :attr:`~.target_id` is the command ID or the app ID since the :attr:`~.changes` array represents the entire :attr:`~discord.objects.GuildApplicationCommandPermissions.permissions` property.
  """

  action_type: AuditLogEvent
  """Type of action that occurred."""

  changes: Optional[list[AuditLogChange]]
  """Changes made to the target_id."""

  id: Snowflake
  """ID of the entry."""

  options: Optional[OptionalAuditEntryInfo]
  """Additional info for certain eventy types."""

  reason: Optional[str]
  """Reason for the changes (1-512 characters)."""

  target_id: Nullable[str]
  """ID of the affected entity (webhook, user, role, etc.)."""

  user_id: Nullable[Snowflake]
  """User or app that made the changes."""