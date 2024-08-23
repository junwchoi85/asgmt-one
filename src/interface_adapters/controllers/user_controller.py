from typing import List
from entities.booking import Booking
from entities.car import Car
from use_cases.user_use_case import UserUseCase


class UserController:
    def __init__(self, user_use_case: UserUseCase):
        self.user_use_case = user_use_case

    def sign_in(self, req: dict):
        if not req.get('username') or not req.get('password'):
            raise ValueError('Username and password are required')

        user = self.user_use_case.sign_in(req)
        if user:
            return {"status": "success", "user": user}
        else:
            return {"status": "failure", "message": "Invalid credentials"}

    def get_booking_list(self, req: dict) -> list[Booking]:
        booking_list = self.user_use_case.get_booking_list(req)
        return {"status": "success", "booking_list": booking_list}

    def confirm_booking(self, req: dict):
        result = self.user_use_case.confirm_booking(req)
        if result:
            return {"status": "success"}
        else:
            return {"status": "failure", "message": "Booking not found"}

    def reject_booking(self, req: dict):
        result = self.user_use_case.reject_booking(req)
        if result:
            return {"status": "success"}
        else:
            return {"status": "failure", "message": "Booking not found"}

    def get_car_list_paged(self, page: int, page_size: int) -> List[Car]:
        return self.user_use_case.get_car_list_paged(page, page_size)
