from typing import List
import uuid

from entities.booking import Booking
from entities.car import Car
from entities.user import User
from interface_adapters.repositories.booking_repository import BookingRepository
from interface_adapters.repositories.car_repository import CarRepository
from interface_adapters.repositories.user_repository import UserRepository
from frameworks_drivers.db.database_setup import TransactionManager
from utils.encryption_util import encrypt_password


class UserUseCase:
    def __init__(self,
                 user_repo: UserRepository, booking_repo: BookingRepository, car_repo: CarRepository,
                 transaction_mngr: TransactionManager):

        self.user_repo = user_repo
        self.booking_repo = booking_repo
        self.car_repo = car_repo
        self.transaction_mngr = transaction_mngr

    """
    Python doesn't support method overloading, 
    so we can't have two methods with the same name but different parameters.
    
    def createUser(self, user: User):
        return self.user_repo.save(user)

    def createUser(self, username, password):
        user_id = str(uuid.uuid4())
        
        new_user_code = self.generate_new_user_code()
        user = User(user_id, new_user_code, username, password)
        return self.user_repo.save(user)
    Instead, we can use the arguments
    """

    def sign_in(self, req: dict) -> User:
        username = req.get('username')
        password_encrypted = encrypt_password(req.get('password'))
        with self.transaction_mngr.transaction_scope() as cursor:
            user = self.user_repo.find_by_username(cursor, username)
            if not user:
                raise ValueError('User not found')

            if user.password != password_encrypted:
                raise ValueError('Incorrect password')

            return user

    def sign_up(self, req: dict) -> int:
        username = req.get('username')
        password_encrypted = encrypt_password(req.get('password'))

        with self.transaction_mngr.transaction_scope() as cursor:
            user = self.user_repo.find_by_username(cursor, username)
            if user:
                raise ValueError('User already exists')

            new_user_code = self.generate_user_code(cursor)
            user = User(None, new_user_code, username, password_encrypted)
            return self.user_repo.create(cursor, user)

    def generate_user_code(self, cursor) -> str:
        """
        Generate user code
        """
        code = self.user_repo.fetch_latest_user_code(cursor)
        if code:
            code = code.split('-')
            code[1] = str(int(code[1]) + 1).zfill(4)
            return '-'.join(code)

    def get_booking_list(self, req: dict) -> list[Booking]:
        """
        Get a list of bookings
        :return: List of bookings
        """

        with self.transaction_mngr.transaction_scope() as cursor:
            return self.booking_repo.get_booking_list(cursor, req)

    def confirm_booking(self, req: dict):
        """
        Confirm a booking
        :param req: Request
        :return: None
        """
        with self.transaction_mngr.transaction_scope() as cursor:
            self.booking_repo.update_booking_status(cursor, req)

    def reject_booking(self, req: dict):
        """
        Reject a booking
        :param req: Request
        :return: None
        """
        with self.transaction_mngr.transaction_scope() as cursor:
            self.booking_repo.update_booking_status(cursor, req)

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

    def update_car_info(self, req: dict):
        """
        Update car information
        :param req: Request
        :return: None
        """
        with self.transaction_mngr.transaction_scope() as cursor:
            return self.car_repo.update(cursor, req)

    def delete_car_info(self, req: dict):
        """
        Delete car information
        :param req: Request
        :return: None
        """
        with self.transaction_mngr.transaction_scope() as cursor:
            req['status'] = 'deleted'
            return self.car_repo.delete(cursor, req)

    def get_car_info(self, req: dict):
        """
        Get car information
        :param req: Request
        :return: Car
        """
        with self.transaction_mngr.transaction_scope() as cursor:
            return self.car_repo.read(cursor, req['car_id'])

    def add_car_info(self, req: dict):
        """
        Add car information
        :param req: Request
        :return: None
        """
        with self.transaction_mngr.transaction_scope() as cursor:
            if 'car_code' not in req:
                car_code = self.car_repo.create_car_code(cursor)
                req['car_code'] = car_code

            return self.car_repo.create(cursor, req)
