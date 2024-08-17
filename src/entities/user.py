from dataclasses import dataclass

from entities.base_entity import BaseEntity

@dataclass
class User(BaseEntity):
    """
    Represents a user entity.
    """
    user_id: int
    user_code: str
    username: str
    password: str