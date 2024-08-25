from typing import List
from constants import cli_constants as constants
from entities.booking import Booking
from entities.car import Car
from interface_adapters.response import Response
from use_cases.user_use_case import UserUseCase
import constants.cli_constants as constants


class UserController:
    def __init__(self, user_use_case: UserUseCase):
        self.user_use_case = user_use_case

    def sign_in(self, req: dict):
        if not req.get('username') or not req.get('password'):
            raise ValueError('Username and password are required')

        try:
            user = self.user_use_case.sign_in(req)
        except ValueError as e:
            return Response(
                status_code=constants.STATUS_FAILURE,
                message=constants.MSSSAGE_USER_SIGN_IN_FAILURE
            ).to_dict()
        if user:
            return Response(
                status_code=constants.STATUS_SUCCESS,
                message=constants.MESSAGE_USER_SIGN_IN_SUCCESS,
                data=user
            ).to_dict()
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

    def update_car_info(self, req: dict):

        result = self.user_use_case.update_car_info(req)

        if result:
            return Response(
                status_code=constants.STATUS_SUCCESS,
                message=constants.MESSAGE_CAR_UPDATE_SUCCESS
            ).to_dict()
        else:
            return Response(
                status_code=constants.STATUS_FAILURE,
                message=constants.MESSAGE_CAR_NOT_FOUND
            ).to_dict()

    def delete_car_info(self, req: dict):

        result = self.user_use_case.delete_car_info(req)

        if result:
            return Response(
                status_code=constants.STATUS_SUCCESS,
                message=constants.MESSAGE_CAR_DELETE_SUCCESS
            ).to_dict()
        else:
            return Response(
                status_code=constants.STATUS_FAILURE,
                message=constants.MESSAGE_CAR_NOT_FOUND
            ).to_dict()

    def add_car_info(self, req: dict):

        result = self.user_use_case.add_car_info(req)

        if result:
            return Response(
                status_code=constants.STATUS_SUCCESS,
                message=constants.MESSAGE_CAR_ADD_SUCCESS
            ).to_dict()
        else:
            return Response(
                status_code=constants.STATUS_FAILURE,
                message=constants.MESSAGE_CAR_ADD_FAILURE
            ).to_dict()
