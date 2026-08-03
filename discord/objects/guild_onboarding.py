from .._dataclass import dataclass
from ..enums import OnboardingMode
from ..snowflake import Snowflake
from .onboarding_prompt import OnboardingPrompt


@dataclass
class GuildOnboarding:
  """Represents the onboarding flow for a guild."""

  default_channel_ids: list[Snowflake]
  """Channel IDs that members get opted into automatically."""

  enabled: bool
  """Whether onboarding is enabled in the guild."""

  guild_id: Snowflake
  """ID of the guild this onboarding is part of."""

  mode: OnboardingMode
  """Current mode of onboarding."""

  prompts: list[OnboardingPrompt]
  """Prompts shown during onboarding and in customize community."""