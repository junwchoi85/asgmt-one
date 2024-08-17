from dataclasses import dataclass
from entities.base_entity import BaseEntity

@dataclass
class CarDetail(BaseEntity) :
    """
    Represents a car detail entity.
    """
    car_dtl_id: int
    car_id: int
    mileage: str
    color: str
    vin: str
    status: str