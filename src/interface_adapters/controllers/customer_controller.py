from typing import List
from entities.car import Car
from interface_adapters.response import Response
from use_cases.customer_use_case import CustomerUseCase
import datetime

from utils.date_utils import parse_date


class CustomerController:
    def __init__(self, customer_use_case: CustomerUseCase):
        self.customer_use_case = customer_use_case

    def sign_up(self, req: dict):
        if not req.get('username') or not req.get('password'):
            raise ValueError('Username and password are required')

        result = self.customer_use_case.sign_up(
            req)
        return result

    def sign_in(self, req: dict):
        """
        Sign in a customer
        :param req: Request
        :return: 
        """

        if not req.get('username') or not req.get('password'):
            return Response(
                status_code="failure",
                message="Username and password are required"
            ).to_dict()

        try:
            customer = self.customer_use_case.sign_in(req)
            if customer:
                return Response(
                    status_code="success",
                    message="Sign in successful",
                    data=customer
                ).to_dict()
        except ValueError as e:
            return Response(
                status_code="failure",
                message=str(e)
            ).to_dict()

    def get_car_list_paged(self, page: int, page_size: int) -> List[Car]:
        return self.customer_use_case.get_car_list_paged(page, page_size)

    def make_a_booking(self, req: dict):
        start_date = req.get('start_date')
        end_date = req.get('end_date')

        # Input Validation
        if not start_date or not end_date:
            return Response(
                status_code="failure",
                message="Start date and end date are required"
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
                status_code="failure",
                message="Invalid date format. Date must be in the format YYYY-MM-DD"
            ).to_dict()

        # validate if start_date is before end_date
        if start_date >= end_date:
            return Response(
                status_code="failure",
                message="Start date must be before end date"
            ).to_dict()
        # validate if start_date is in the past
        if datetime.datetime.strptime(start_date, '%Y-%m-%d') < datetime.datetime.now():
            return Response(
                status_code="failure",
                message="Start date must be in the future"
            ).to_dict()
        # Validation check passed

        # Create a booking
        result = self.customer_use_case.make_a_booking(req)

        if result:
            return Response(
                status_code="success",
                message="Booking successful"
            ).to_dict()
        return Response(
            status_code="failure",
            message="Booking failed"
        ).to_dict()
