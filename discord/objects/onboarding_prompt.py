from .._dataclass import dataclass
from ..enums import OnboardingPromptType
from ..snowflake import Snowflake
from .onboarding_prompt_option import OnboardingPromptOption


@dataclass
class OnboardingPrompt:
  id: Snowflake
  """ID of the prompt."""

  in_onboarding: bool
  """Indicates whether the prompt is present in the onboarding flow. If ``False``, the prompt will only apepar in the **Channels & Roles** tab."""

  options: list[OnboardingPromptOption]
  """Options available within the prompt."""

  required: bool
  """Indicates whether the prompt is required before a user completes the onboarding flow."""

  single_select: bool
  """Indicates whether the users are limited to selecting one option for the prompt."""

  title: str
  """Title of the prompt."""

  type: OnboardingPromptType
  """Type of prompt."""