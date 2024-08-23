import datetime
from entities.base_entity import BaseEntity
from entities.booking import Booking


class BookingDetail(BaseEntity):
    def __init__(self,
                 car_code: str, name: str, year: str,
                 passenger: int, transmission: str, luggage_large: int,
                 luggage_small: int, engine: str, fuel: str,
                 start_date: datetime,
                 end_date: datetime,
                 total_fee: float,
                 status: str,
                 created_at=None, created_by=None, updated_at=None, updated_by=None):

        super().__init__(created_at, created_by, updated_at, updated_by)

        self.car_code = car_code
        self.name = name
        self.year = year
        self.passenger = passenger
        self.transmission = transmission
        self.luggage_large = luggage_large
        self.luggage_small = luggage_small
        self.engine = engine
        self.fuel = fuel
        self.start_date = start_date
        self.end_date = end_date
        self.total_fee = total_fee
        self.status = status
