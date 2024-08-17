from dataclasses import dataclass
from datetime import datetime

from entities.base_entity import BaseEntity

@dataclass
class Customer(BaseEntity):
    """
    Represents a customer entity.
    """
    cst_id: int
    cst_code: str
    username: str
    password: str