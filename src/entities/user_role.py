from dataclasses import dataclass

from entities.base_entity import BaseEntity

@dataclass
class UserRole(BaseEntity):
    """
    Represents a user role entity.
    """
    user_id: str
    role_id: str