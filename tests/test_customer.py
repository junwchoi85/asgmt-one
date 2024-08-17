import pytest

from interface_adapters.repositories.customer_repository import CustomerRepository

@pytest.fixture
def customer_repo(db_cursor):
    return CustomerRepository(db_cursor)

def test_create_customer(customer_repo):
    