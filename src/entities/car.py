from dataclasses import dataclass
from entities.base_entity import BaseEntity

@dataclass
class Car(BaseEntity):
    """
    Represents a car entity.
    """
    car_id: int
    car_code: str
    name: str
    year: str
    passenger: int
    transmission: str
    luggage_large: int
    luggage_small: int
    engine: str
    fuel: str