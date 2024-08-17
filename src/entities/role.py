from dataclasses import dataclass, field

from entities.base_entity import BaseEntity

@dataclass
class Role(BaseEntity):
    """
    Represents a role entity.
    """
    role_id: int
    role_code: str
    desc: str = None