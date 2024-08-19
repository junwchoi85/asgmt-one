
import pytest

from interface_adapters.repositories.booking_repository import BookingRepository
from interface_adapters.repositories.car_repository import CarRepository
from interface_adapters.repositories.customer_repository import CustomerRepository
from use_cases.customer_use_case import CustomerUseCase
import datetime


def test_book_car(customer_repo, car_repo, booking_repo, transaction_manager, test_logger):
    # Setup
    customer_use_case = CustomerUseCase(customer_repo,
                                        car_repo,
                                        booking_repo,
                                        transaction_manager)
    # Create a customer
    req_create_customer = {
        'username': 'cut_sign_up',
        'password': 'password'
    }
    rslt_create_customer = customer_use_case.sign_up(req_create_customer)
    # get the customer
    customer = customer_use_case.find_user_by_username(
        req_create_customer['username'])
    # test_logger.debug(customer.cst_id)
    # Select a Car
    cars = customer_use_case.get_car_list()
    # select the first car
    car_selected = cars[0]

    # Get today's date
    today = datetime.date.today()
    one_month_from_today = today + datetime.timedelta(days=30)
    # Format today's date as 'YYYY-MM-DD'
    today_formatted = today.strftime('%Y-%m-%d')
    one_month_from_today_formatted = one_month_from_today.strftime('%Y-%m-%d')
    # Book the car
    req_book_car = {
        'cst_id': customer.cst_id,
        'car_id': car_selected.car_id,
        'car_dtl_id': 1,
        'start_date': today_formatted,
        'end_date': one_month_from_today_formatted,
        'total_fee': 100,
        'status': 'BOOKED'
    }
    # Test
    rewult = customer_use_case.book_car(req_book_car)
    # Verify
    assert rewult is not None
