
import pytest
from interface_adapters.repositories.customer_repository import CustomerRepository
from use_cases.customer_use_case import CustomerUseCase


def test_sign_up(customer_repo, car_repo, booking_repo, transaction_manager):
    # Setup
    customer_use_case = CustomerUseCase(
        customer_repo, car_repo, booking_repo, transaction_manager)

    req = {
        'username': 'cut_sign_up',
        'password': 'password'
    }

    # Test
    result = customer_use_case.sign_up(req)
    # Verify
    assert result is not None


def test_sign_in(customer_repo, car_repo, booking_repo, transaction_manager):
    # Setup
    pass
    customer_use_case = CustomerUseCase(
        customer_repo, car_repo, booking_repo, transaction_manager)

    req = {
        'username': 'cut_sign_in',
        'password': 'password'
    }

    # Save the customer
    new_customer = customer_use_case.sign_up(req)
    # Test
    result = customer_use_case.sign_in(req)
    # Verify
    assert result is not None
    assert result.username == req['username']


def test_get_car_rental_terms(customer_repo, car_repo, booking_repo, transaction_manager):
    # Setup
    car_use_case = CustomerUseCase(
        customer_repo, car_repo, booking_repo, transaction_manager)

    req = {
        'car_id': 1
    }
    # Test
    result = car_use_case.get_rental_terms(req)
    # test_logger.info(result)
    # Verify
    assert result is not None
