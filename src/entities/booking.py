from dataclasses import dataclass
from datetime import datetime

from entities.base_entity import BaseEntity

@dataclass
class Booking(BaseEntity):
    """
    Represents a booking entity.
    """
    booking_id: int
    user_id: int
    car_id: int
    start_date: datetime
    end_date: datetime
    total_price: float
    status: str