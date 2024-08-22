import os
import pytest

from frameworks_drivers.db.database_setup import setup_database
from frameworks_drivers.db.transaction_manager import TransactionManager
from interface_adapters.repositories.booking_repository import BookingRepository
from interface_adapters.repositories.car_repository import CarRepository
from interface_adapters.repositories.customer_repository import CustomerRepository
from interface_adapters.repositories.user_repository import UserRepository
from utils.logger import get_test_logger

# 로깅 설정


@pytest.fixture(scope='module')
def transaction_manager():
    """
    Fixture for creating a TransactionManager instance.

    This fixture creates a TransactionManager instance for the test module.
    The connection is closed after all tests in the module have run.

    Returns:
        TransactionManager: An instance of the TransactionManager.
    """
    db_path = 'test_database.db'  # 테스트용 데이터베이스 경로
    transaction_manager = TransactionManager(db_path)
    setup_database(transaction_manager)  # 데이터베이스 설정
    yield transaction_manager     # 테스트에 사용할 TransactionManager 인스턴스를 반환
    transaction_manager.close_connection()    # 테스트가 끝난 후 연결을 닫음
    if os.path.exists(db_path):
        os.remove(db_path)  # 테스트가 끝난 후 데이터베이스 파일 삭제


@pytest.fixture
def db_connection(transaction_manager):
    """
    Fixture for providing a database connection.

    This fixture provides a database connection for each test.
    The connection is managed by the TransactionManager.

    Args:
        transaction_manager (TransactionManager): The TransactionManager instance.

    Returns:
        connection: The database connection object.
    """
    with transaction_manager.transaction_scope() as connection:
        yield connection

# Repository fixtures


@pytest.fixture
def user_repo(transaction_manager):
    return UserRepository(transaction_manager)


@pytest.fixture
def customer_repo(transaction_manager):
    return CustomerRepository(transaction_manager)


@pytest.fixture
def car_repo(transaction_manager):
    return CarRepository(transaction_manager)


@pytest.fixture
def booking_repo(transaction_manager):
    return BookingRepository(transaction_manager)


# Logger fixture
@pytest.fixture(scope='session')
def test_logger():
    return get_test_logger('test_logger')
