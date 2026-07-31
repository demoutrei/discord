from .._dataclass import dataclass
from ..snowflake import Snowflake
from .application_command_permissions import ApplicationCommandPermissions


@dataclass
class GuildApplicationCommandPermissions:
  """Returned when fetching the permissions for an app's command(s) in a guild.

  When the :attr:`~.id` field is the application ID instead of a command ID, the permissions apply to all commands that do not contain explicit overwrites.
  """
  
  application_id: Snowflake
  """ID of the application the command belongs to"""

  guild_id: Snowflake
  """ID of the guild"""
  
  id: Snowflake
  """ID of the command or the application ID"""

  permissions: list[ApplicationCommandPermissions]
  """Permissions for the command in the guild, max of 100"""