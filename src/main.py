import sqlite3

from interface_adapters.cli import greeting_cli
from frameworks_drivers.db.transaction_manager import TransactionManager
from interface_adapters.repositories.user_repository import UserRepository
from use_cases.user_use_case import UserUseCase
from interface_adapters.controllers.user_controller import UserController

DB_FILE = 'mse800.db'

def create_user_controller(transaction_manager: TransactionManager):
    connection = transaction_manager.transaction_scope()
    user_repository = UserRepository(connection)

    user_use_case = UserUseCase(user_repository, transaction_manager)

    user_controller = UserController(user_use_case)

    return user_controller

def create_vihecle_controller(transaction_manager: TransactionManager):
    pass

def rental_controller(transaction_manager: TransactionManager):
    pass

def main():
    # Create database connection
    connection = sqlite3.connect(DB_FILE)
    transaction_manager = TransactionManager(connection)

    # Create controllers
    user_controller = create_user_controller(transaction_manager)
    create_vihecle_controller(transaction_manager)
    rental_controller(transaction_manager)

    # The central hub for starting the application.
    greeting_cli.greet(obj={'user_controller': user_controller})

if __name__ == '__main__':
    main()