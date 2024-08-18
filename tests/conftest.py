import pytest

from frameworks_drivers.db.database_setup import setup_database
from frameworks_drivers.db.transaction_manager import TransactionManager


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
    with transaction_manager as connection:
        yield connection
