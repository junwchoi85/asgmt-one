import datetime
from typing import List
from entities.car import Car
from entities.customer import Customer
from frameworks_drivers.db.transaction_manager import TransactionManager
from interface_adapters.repositories.booking_repository import BookingRepository
from interface_adapters.repositories.car_repository import CarRepository
from interface_adapters.repositories.customer_repository import CustomerRepository
from utils.encryption_util import encrypt_password


class CustomerUseCase:
    def __init__(self,
                 customer_repository: CustomerRepository,
                 car_repository: CarRepository,
                 booking_repo: BookingRepository,
                 transaction_mngr: TransactionManager):

        self.customer_repo = customer_repository
        self.car_repo = car_repository
        self.transaction_mngr = transaction_mngr
        self.booking_repo = booking_repo

    def sign_up(self, req: dict) -> int:
        """
        Sign up a new user
        :param req: User information
        :return: User ID
        """
        with self.transaction_mngr.transaction_scope() as cursor:
            customer = Customer(
                cst_id=None,
                cst_code=self.generate_customer_code(cursor),
                username=req['username'],
                password=encrypt_password(req['password'])
            )
            return self.customer_repo.create(cursor, customer)

    def find_user_by_username(self, username: str) -> Customer:
        with self.transaction_mngr.transaction_scope() as cursor:
            return self.customer_repo.find_by_username(cursor, username)

    def sign_in(self, customer_data: dict) -> Customer:
        username = customer_data['username']
        encrypted_password = encrypt_password(customer_data['password'])
        with self.transaction_mngr.transaction_scope() as cursor:
            customer = self.customer_repo.find_by_username(cursor, username)
            if not customer:
                raise ValueError('User not found')
            if customer.password != encrypted_password:
                raise ValueError('Incorrect password')
            return customer

    def generate_customer_code(self, cursor) -> str:
        code = self.customer_repo.fetch_latest_customer_code(cursor)
        code = code.split('-')
        code[1] = str(int(code[1]) + 1).zfill(4)
        return '-'.join(code)

    # Car section. TODO: Consider moving this to a separate use case
    def get_car_list(self) -> List[Car]:
        """
        Get a list of cars
        :return: List of cars
        """
        with self.transaction_mngr.transaction_scope() as cursor:
            return self.car_repo.get_car_list(cursor)

    def get_car_list_paged(self, page: int, page_size: int) -> List[Car]:
        """
        Get a list of cars with pagination
        :param page: Page number
        :param page_size: Number of items per page
        :return: List of cars
        """
        if page < 1:
            page = 1
        if page_size < 1:
            page_size = 10
        with self.transaction_mngr.transaction_scope() as cursor:
            return self.car_repo.get_car_list_paged(cursor, page, page_size)

    # Booking section. TODO: Consider moving this to a separate use case
    def make_a_booking(self, req: dict) -> int:
        """
        Book a car
        :param req: Booking information
        :return: Booking ID
        """

        # Business Logic
        # get the rental terms of the car
        car_rental_terms = req['rental_terms']

        # calculate the total fee

        username = req['username']
        car_code = req['car_code']
        status = 'reserved'
        with self.transaction_mngr.transaction_scope() as cursor:
            customer = self.customer_repo.find_by_username(cursor, username)
            car = self.car_repo.find_by_car_code(cursor, car_code)

            if not car_rental_terms:
                req = {
                    'car_id': car.car_id
                }
                car_rental_terms = self.car_repo.get_rental_terms(cursor, req)

            select_car_detail_req = {
                'car_id': car.car_id
            }
            # get the car_detail of the car. Here, the car_detail will be selected randomly.
            car_detail = self.car_repo.select_car_detail(
                cursor, select_car_detail_req)

            # Calculate total fee
            total_fee = self._calculate_total_fee(
                car_rental_terms.price_per_day,
                req['start_date'],
                req['end_date']
            )

            car_dtl_id = car_detail.car_dtl_id
            booking_req = {
                'cst_id': customer.cst_id,
                'car_dtl_id': car_dtl_id,
                'start_date': req['start_date'],
                'end_date': req['end_date'],
                'total_fee': total_fee,
                'status': status
            }

            return self.booking_repo.book_car(cursor, booking_req)

    # private method to calculate total fee
    def _calculate_total_fee(self,
                             price_per_day: float,
                             start_date: str,
                             end_date: str) -> float:
        # calculate the total fee
        total_fee = price_per_day * (
            datetime.datetime.strptime(
                end_date, '%Y-%m-%d') - datetime.datetime.strptime(start_date, '%Y-%m-%d')
        ).days
        return round(total_fee, 2)

    def get_customer_booking_list(self, req: dict):
        with self.transaction_mngr.transaction_scope() as cursor:

            customer = self.find_user_by_username(req['username'])
            if customer:
                req = {
                    'cst_id': customer.cst_id
                }

            return self.booking_repo.get_booking_detail_list(cursor, req)
