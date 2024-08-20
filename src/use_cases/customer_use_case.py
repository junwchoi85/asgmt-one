
from typing import List
from entities.car import Car
from entities.customer import Customer
from frameworks_drivers.db.transaction_manager import TransactionManager
from interface_adapters.repositories.booking_repository import BookingRepository
from interface_adapters.repositories.car_repository import CarRepository
from interface_adapters.repositories.customer_repository import CustomerRepository


class CustomerUseCase:
    def __init__(self,
                 customer_repository: CustomerRepository,
                 car_repository: CarRepository,
                 booking_repo: BookingRepository,
                 transaction_mngr: TransactionManager):

        self.customer_repo = customer_repository
        self.car_repo = car_repository
        self.transaction_mngr = transaction_mngr
        self.booking_repository = booking_repo

    def sign_up(self, customer_data: dict) -> int:
        with self.transaction_mngr.transaction_scope():
            customer = Customer(
                cst_id=None,
                cst_code=self.generate_customer_code(),
                username=customer_data['username'],
                password=customer_data['password']
            )
            return self.customer_repo.create(customer)

    def find_user_by_username(self, username: str) -> Customer:
        with self.transaction_mngr.transaction_scope():
            return self.customer_repo.find_by_username(username)

    def sign_in(self, customer_data: dict) -> Customer:
        username = customer_data['username']
        password = customer_data['password']
        with self.transaction_mngr.transaction_scope():
            customer = self.customer_repo.find_by_username(username)
            if not customer:
                raise ValueError('User not found')
            if customer.password != password:
                raise ValueError('Incorrect password')
            return customer

    def generate_customer_code(self) -> str:
        with self.transaction_mngr.transaction_scope():
            code = self.customer_repo.fetch_latest_customer_code()
            code = code.split('-')
            code[1] = str(int(code[1]) + 1).zfill(4)
            return '-'.join(code)

    # Car section. TODO: Consider moving this to a separate use case
    def get_car_list(self) -> List[Car]:
        """
        Get a list of cars
        :return: List of cars
        """
        with self.transaction_mngr.transaction_scope():
            return self.car_repo.get_car_list()

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
        with self.transaction_mngr.transaction_scope():
            return self.car_repo.get_car_list_paged(page, page_size)

    # Booking section. TODO: Consider moving this to a separate use case
    def make_a_booking(self, req: dict) -> int:
        """
        Book a car
        :param req: Booking information
        :return: Booking ID
        """
        username = req['username']
        car_code = req['car_code']
        total_fee = 100
        status = 'reserved'
        with self.transaction_mngr.transaction_scope():
            # select user
            customer = self.customer_repo.find_by_username(username)
            car = self.car_repo.find_by_car_code(car_code)
            select_car_detail_req = {
                'car_id': car.car_id
            }
            car_detail = self.car_repo.select_car_detail(select_car_detail_req)
            car_dtl_id = car_detail.car_dtl_id
            booking_req = {
                'cst_id': customer.cst_id,
                'car_dtl_id': car_dtl_id,
                'start_date': req['start_date'],
                'end_date': req['end_date'],
                'total_fee': total_fee,
                'status': status
            }

            return self.booking_repository.book_car(booking_req)
