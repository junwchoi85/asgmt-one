import sqlite3

from interface_adapters.cli import greeting_cli
from frameworks_drivers.db.transaction_manager import TransactionManager
from interface_adapters.controllers.car_controller import CarController
from interface_adapters.controllers.customer_controller import CustomerController
from interface_adapters.repositories.booking_repository import BookingRepository
from interface_adapters.repositories.car_repository import CarRepository
from interface_adapters.repositories.customer_repository import CustomerRepository
from interface_adapters.repositories.user_repository import UserRepository
from use_cases.car_use_case import CarUseCase
from use_cases.user_use_case import UserUseCase
from use_cases.customer_use_case import CustomerUseCase
from interface_adapters.controllers.user_controller import UserController

DB_FILE = 'mse800.db'


def create_user_controller(transaction_manager: TransactionManager):
    # User
    user_repo = UserRepository(transaction_manager)
    user_use_case = UserUseCase(user_repo, transaction_manager)
    user_controller = UserController(user_use_case)

    return user_controller


def create_customer_controller(transaction_manager: TransactionManager):
    customer_repo = CustomerRepository(transaction_manager)
    car_repo = CarRepository(transaction_manager)
    booking_repo = BookingRepository(transaction_manager)
    customer_use_case = CustomerUseCase(
        customer_repo, car_repo, booking_repo, transaction_manager)
    customer_controller = CustomerController(customer_use_case)

    return customer_controller


def create_vihecle_controller(transaction_manager: TransactionManager):
    car_repository = CarRepository(transaction_manager)
    car_use_case = CarUseCase(car_repository, transaction_manager)
    car_controller = CarController(car_use_case)

    return car_controller


def rental_controller(transaction_manager: TransactionManager):
    pass


def main():
    # Create database connectionㄱ
    transaction_manager = TransactionManager(DB_FILE)

    # Create controllers
    user_controller = create_user_controller(transaction_manager)
    customer_controller = create_customer_controller(transaction_manager)
    vihecle_controller = create_vihecle_controller(transaction_manager)
    rental_controller(transaction_manager)

    # The central hub for starting the application.
    greeting_cli.greet(obj={'user_controller': user_controller,
                            'customer_controller': customer_controller,
                            'vihecle_controller': vihecle_controller})


if __name__ == '__main__':
    main()
