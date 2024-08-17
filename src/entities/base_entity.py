from dataclasses import dataclass
from datetime import datetime

@dataclass
class BaseEntity:
    """
    Represents a base entity.
    """
    created_at: datetime
    created_by: str
    updated_at: datetime
    updated_by: str

