from datetime import datetime

from entities.base_entity import BaseEntity

class Booking(BaseEntity):
    def __init__(self,
                 booking_id: int, 
                 user_id: int, 
                 car_id: int, 
                 start_date: datetime, 
                 end_date: datetime, 
                 total_price: float, 
                 status: str):
        
        self.booking_id = booking_id
        self.user_id = user_id
        self.car_id = car_id
        self.start_date = start_date
        self.end_date = end_date
        self.total_price = total_price
        self.status = status