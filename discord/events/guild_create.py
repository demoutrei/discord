from ..objects import Channel, Guild, GuildMember, GuildScheduledEvent, SoundboardSound, StageInstance, UnavailableGuild, VoiceState
from ..utils import ISO8601Timestamp
from .presence_update import PresenceUpdateEvent


class GuildCreateEvent(Guild, UnavailableGuild):
  channels: list[Channel]
  """Channels in the guild."""
  
  guild_scheduled_events: list[GuildScheduledEvent]
  """Scheduled events in the guild."""
  
  joined_at: ISO8601Timestamp
  """When this guild was joined at."""

  large: bool
  """``True`` if this is considered a large guild."""

  member_count: int
  """Total number of members in this guild."""

  members: list[GuildMember]
  """Users in the guild."""

  presences: list[PresenceUpdateEvent]
  """Presences of the members in the guild, will only include non-offline members if the size is greater than ``large threshold``."""

  soundboard_sounds: list[SoundboardSound]
  """Soundboard sounds in the guild."""

  stage_instances: list[StageInstance]
  """Stage instances in the guild."""

  threads: list[Channel]
  """All active threads in the guild that current user has permission to view."""

  unavailable: Optional[bool]
  """``True`` if this guild is unavailable due to an outage."""

  voice_states: list[VoiceState]
  """States of members currently in voice channels; lacks the :attr:`~discord.objects.VoiceState.guild_id` key."""