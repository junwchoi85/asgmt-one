from dataclasses import dataclass
from entities.base_entity import BaseEntity

@dataclass
class CarDetail(BaseEntity) :
    """
    Represents a car detail entity.
    """
    car_detail_id: int
    car_id: int
    color: str
    price: float
    available: bool