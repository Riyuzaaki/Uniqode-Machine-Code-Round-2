from enum import Enum

class PlanTiers(Enum):
    TIER1 = "tier1"
    TIER2 = "tier2"
    TIER3 = "tier3"

class PostCategory(Enum):
    PERSONAL_PRODUCTIVITY = "personal_productivity"
    PRODUCT_MANAGEMENT = "product_management"
    B2B = "b2b"
    AGENT_WRAPPERS = "agent_wrappers"
