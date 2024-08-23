import datetime
import constants.cli_constants as constants

from typing import List
from entities.car import Car
from interface_adapters.response import Response
from use_cases.customer_use_case import CustomerUseCase
from utils.date_utils import parse_date
from utils.logger import get_app_logger


class CustomerController:
    def __init__(self, customer_use_case: CustomerUseCase):
        self.customer_use_case = customer_use_case
        self.logger = get_app_logger()

    def sign_up(self, req: dict):
        """
        Sign up a customer
        :param req: Request
        :return: Response dict
        """
        if not req.get('username') or not req.get('password'):
            return Response(
                status_code=constants.STATUS_FAILURE,
                message=constants.MESSAGE_USERNAME_PASSWORD_REQUIRED
            ).to_dict()
        try:
            result = self.customer_use_case.sign_up(req)
        except RuntimeError as e:
            self.logger.error(f"RuntimeError occurred during sign up: {e}")
            return Response(
                status_code=constants.STATUS_FAILURE,
                message=constants.MESSAGE_SIGN_UP_FAILURE
            ).to_dict()

        if result:
            return Response(
                status_code=constants.STATUS_SUCCESS,
                message=constants.MESSAGE_SIGN_UP_SUCCESS
            ).to_dict()

        return Response(
            status_code=constants.STATUS_FAILURE,
            message=constants.MESSAGE_SIGN_UP_FAILURE
        ).to_dict()

    def sign_in(self, req: dict):
        """
        Sign in a customer
        :param req: Request
        :return: Response dict
        """

        if not req.get('username') or not req.get('password'):
            return Response(
                status_code=constants.STATUS_FAILURE,
                message=constants.MESSAGE_USERNAME_PASSWORD_REQUIRED
            ).to_dict()

        try:
            customer = self.customer_use_case.sign_in(req)
            if customer:
                return Response(
                    status_code=constants.STATUS_SUCCESS,
                    message=constants.MESSAGE_SIGN_IN_SUCCESS,
                    data=customer
                ).to_dict()
        except ValueError as e:
            return Response(
                status_code=constants.STATUS_FAILURE,
                message=str(e)
            ).to_dict()
        return Response(
            status_code=constants.STATUS_FAILURE,
            message=constants.MESSAGE_SIGN_IN_FAILURE
        ).to_dict()

    def get_car_list_paged(self, page: int, page_size: int) -> List[Car]:
        return self.customer_use_case.get_car_list_paged(page, page_size)

    def make_a_booking(self, req: dict):
        """
        Make a booking
        :param req: Request
        :return: response dict
        """
        start_date = req.get('start_date')
        end_date = req.get('end_date')

        # Input Validation
        if not start_date or not end_date:
            return Response(
                status_code=constants.STATUS_FAILURE,
                message=constants.MESSAGE_START_END_DATE_REQUIRED
            ).to_dict()

        # Validate date format
        try:
            # format date
            start_date_parsed = parse_date(start_date).strftime('%Y-%m-%d')
            end_date_parsed = parse_date(end_date).strftime('%Y-%m-%d')
            # set formatted date
            req['start_date'] = start_date_parsed
            req['end_date'] = end_date_parsed
        except ValueError:
            return Response(
                status_code=constants.STATUS_FAILURE,
                message=constants.MESSAGE_INVALID_DATE_FORMAT
            ).to_dict()

        # validate if start_date is before end_date
        if start_date >= end_date:
            return Response(
                status_code=constants.STATUS_FAILURE,
                message=constants.MESSAGE_START_DATE_BEFORE_END_DATE
            ).to_dict()
        # validate if start_date is in the past
        if parse_date(start_date) < datetime.datetime.now():
            return Response(
                status_code=constants.STATUS_FAILURE,
                message=constants.MESSAGE_START_DATE_IN_FUTURE
            ).to_dict()
        # Validation check passed

        # Create a booking
        result = self.customer_use_case.make_a_booking(req)

        if result:
            return Response(
                status_code=constants.STATUS_SUCCESS,
                message=constants.MESSAGE_BOOKING_SUCCESS
            ).to_dict()
        return Response(
            status_code=constants.STATUS_FAILURE,
            message=constants.MESSAGE_BOOKING_FAILURE
        ).to_dict()

    def get_booking_list(self, req: dict):
        """
        Get booking list
        :param req: Request
        :return: Response dict
        """
        return self.customer_use_case.get_customer_booking_list(req)
