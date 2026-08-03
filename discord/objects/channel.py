from .._dataclass import dataclass
from ..enums import ChannelType, DefaultSortOrderType, ForumLayoutType, VideoQualityMode
from ..flags import ChannelFlags, PermissionFlags
from ..snowflake import Snowflake
from ..utils import ISO8601Timestamp, Nullable, Optional
from .default_reaction import DefaultReaction
from .forum_tag import ForumTag
from .permission_overwrite import PermissionOverwrite
from .thread_member import ThreadMember
from .thread_metadata import ThreadMetadata
from .user import User


@dataclass
class Channel:
  """Represents a guild or DM channel within Discord."""

  application_id: Optional[Snowflake]
  """Application ID of the group DM creator if it is bot-created"""

  applied_tags: Optional[list[Snowflake]]
  """The IDs of the set of tags that have been applied to a thread in a :attr:`~discord.enums.ChannelType.GUILD_FORUM` or a :attr:`~discord.enums.ChannelType.GUILD_MEDIA` channel"""

  app_permissions: Optional[PermissionFlags]
  """Computed permissions for the bot user in the channel, including overwrites, only included when part of the ``resolved`` data received on an interaction. This does not include implicit permissions, which may need to be checked separately"""

  available_tags: Optional[list[ForumTag]]
  """The set of tags that can be used in a :attr:`~discord.enums.ChannelType.GUILD_FORUM` or a :attr:`~discord.enums.ChannelType.GUILD_MEDIA` channel"""

  bitrate: Optional[int]
  """The bitrate (in bits per second) of the voice channel"""

  default_auto_archive_duration: Optional[int]
  """Default duration, copied onto newly created threads, in minutes, threads will stop showing in the channel list after the specified period of inactivity, can be set to: 60, 1440, 4320, 10080"""

  default_forum_layout: Optional[ForumLayoutType]
  """The default forum layout view used to display posts in :attr:`~discord.enums.ChannelType.GUILD_FORUM` channels. Defaults to :attr:`~discord.enums.ForumLayoutType.NOT_SET`, which indicates a layout view has not been set by a channel admin"""

  default_reaction_emoji: Optional[Nullable[DefaultReaction]]
  """The emoji to show in the add reaction button on a thread in a :attr:`~discord.enums.ChannelType.GUILD_FORUM` or a :attr:`~discord.enums.ChannelType.GUILD_MEDIA` channel"""

  default_sort_order: Optional[Nullable[DefaultSortOrderType]]
  """The default sort order type used to order posts in :attr:`~discord.enums.ChannelType.GUILD_FORUM` and :attr:`~discord.enums.ChannelType.GUILD_MEDIA` channels. Defaults to ``None``, which indicates a preferred sort order hasn't been set by a channel admin"""

  default_thread_rate_limit_per_user: Optional[int]
  """The initial :attr:`~.rate_limit_per_user` to set on newly created threads in a channel. This field is copied to the thread at creation time and does not live update"""

  flags: Optional[ChannelFlags]
  """Channel flags combined as a bitfield"""

  guild_id: Optional[Snowflake]
  """The ID of the guild (may be missing for some channel objects received over gateway guild dispatches)"""

  icon: Optional[Nullable[str]]
  """Icon hash of the group DM"""

  id: Snowflake
  """The ID of this channel"""

  last_message_id: Optional[Nullable[Snowflake]]
  """The ID of the last message sent in this channel (or thread for :attr:`discord.enums.ChannelType.GUILD_FORUM` or :attr:`~discord.enums.ChannelType.GUILD_MEDIA` channels) (may not point to an existing or valid message or thread)"""

  last_pin_timestamp: Optional[Nullable[ISO8601Timestamp]]
  """When the last pinned message was pinned. This may be ``None`` in events such as ``GUILD_CREATE`` when a message is not pinned"""

  managed: Optional[bool]
  """For group DM channels: whether the channel is managed by an application via the ``gdm.join`` OAuth2 scope"""

  member: Optional[ThreadMember]
  """Thread member object for the current user, if they have joined the thread, only included on certain API endpoints"""

  member_count: Optional[int]
  """An approximate count of users in a thread, stops counting at 50"""

  message_count: Optional[int]
  """Number of messages (not including the initial message or deleted messages) in a thread.

  .. note::
      For threads created before July 1, 2022, the message count is inaccurate when it's greater than 50.
  """

  name: Optional[Nullable[str]]
  """The name of the channel (1-100 characters)"""

  nsfw: Optional[bool]
  """Whether the channel is age-restricted"""

  owner_id: Optional[Snowflake]
  """ID of the creator of the group DM or thread"""

  parent_id: Optional[Nullable[Snowflake]]
  """For guild channels: ID of the parent category for a channel (each parent category can contain up to 50 channels), for threads: ID of the text channel this thread was created"""

  permissions: Optional[PermissionFlags]
  """Computed permissions for the invoking user in the channel, including overwrites, only included when part of the ``resolved`` data received on an interaction. This does not include implicit permissions, which may need to be checked separately"""

  permission_overwrites: Optional[list[PermissionOverwrite]]
  """Explicit permission overwrites for members and roles"""

  position: Optional[int]
  """Sorting position of the channel (channels with the same position are sorted by id)"""

  rate_limit_per_user: Optional[int]
  """Amount of seconds a user has to wait before sending another message (0-21600); bots, as well as users with the permission :attr:`~discord.flags.PermissionFlag.BYPASS_SLOWMODE`, are unaffected

  .. tip::
      :attr:`~.rate_limit_per_user` also applies to thread creation. Users can send one message and create one thread during each :attr:`~.rate_limit_per_user` interval.
  """

  recipients: Optional[list[User]]
  """The recipients of the DM"""

  rtc_region: Optional[Nullable[str]]
  """Voice region ID for the voice channel, automatic when set to null"""

  thread_metadata: Optional[ThreadMetadata]
  """Thread-specific fields not needed by other channels"""

  topic: Optional[Nullable[str]]
  """The channel topic (0-4096 characters for :attr:`~discord.enums.ChannelType.GUILD_FORUM` and :attr:`~discord.enums.ChannelType.GUILD_MEDIA` channels, 0-1024 characters for all others)"""

  total_messages_sent: Optional[int]
  """Number of messages ever sent in a thread, it's similar to :attr:`~.message_count` on message creation, but will not decrement the number when a message is deleted"""

  type: ChannelType
  """The type of channel"""

  user_limit: Optional[int]
  """The user limit of the voice channel"""

  video_quality_mode: Optional[VideoQualityMode]
  """The camera video quality mode of the voice channel, ``1`` when not present"""