from dataclasses import dataclass

from entities.base_entity import BaseEntity

@dataclass
class CarRentalTerms(BaseEntity):
    """
    Represents a car rental terms entity.
    """
    term_id: int
    car_id: int
    rental_period: str
    price_per_day: float
    insurance_included: bool