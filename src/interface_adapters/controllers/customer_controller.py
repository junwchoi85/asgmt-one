
from typing import List
from entities.car import Car
from interface_adapters.response import Response
from use_cases.customer_use_case import CustomerUseCase
import datetime


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
                status="failure",
                message="Username and password are required"
            )

        try:
            customer = self.customer_use_case.sign_in(req)
            if customer:
                return {"status": "success", "message": "Sign in successful", "customer": customer}
        except ValueError as e:
            return {"status": "failure", "message": str(e)}

    def get_car_list_paged(self, page: int, page_size: int) -> List[Car]:
        return self.customer_use_case.get_car_list_paged(page, page_size)

    def make_a_booking(self, req: dict):
        start_date = req.get('start_date')
        end_date = req.get('end_date')

        # Input Validation
        if not start_date or not end_date:
            return {"status": "failure", "message": "Start date and end date are required"}
        # Validate date format
        try:
            datetime.datetime.strptime(start_date, '%Y-%m-%d')
            datetime.datetime.strptime(end_date, '%Y-%m-%d')
        except ValueError:
            return {"status": "failure", "message": "Invalid date format. Date should be in yyyy-mm-dd format"}
        # validate if start_date is before end_date
        if start_date >= end_date:
            return {"status": "failure", "message": "Start date must be before end date"}
        # validate if start_date is in the past
        if datetime.datetime.strptime(start_date, '%Y-%m-%d') < datetime.datetime.now():
            return {"status": "failure", "message": "Start date must be in the future"}
        # Validation check passed

        # Create a booking
        result = self.customer_use_case.make_a_booking(req)

        if result:
            return {"status": "success", "message": "Booking successful"}
        return {"status": "failure", "message": "Booking failed"}
