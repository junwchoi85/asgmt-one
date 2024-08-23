from datetime import datetime

from entities.base_entity import BaseEntity
from entities.car import Car
from entities.car_detail import CarDetail
from entities.customer import Customer


class Booking(BaseEntity):
    def __init__(self,
                 booking_id: int,
                 cst_id: int,
                 car_dtl_id: int,
                 start_date: datetime,
                 end_date: datetime,
                 total_fee: float,
                 status: str):

        self.booking_id = booking_id
        self.cst_id = cst_id
        self.car_dtl_id = car_dtl_id
        self.start_date = start_date
        self.end_date = end_date
        self.total_fee = total_fee
        self.status = status
