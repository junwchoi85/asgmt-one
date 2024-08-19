
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

    new_username = 'test_booking'
    new_password = 'password'

    # Create a customer
    req_create_customer = {
        'username': new_username,
        'password': new_password
    }
    rslt_create_customer = customer_use_case.sign_up(req_create_customer)
    # get the customer
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
        'username': new_username,
        'car_code': car_selected.car_code,
        'start_date': '2021-01-01',
        'end_date': '2021-01-31',
    }
    # Test
    rewult = customer_use_case.make_a_booking(req_book_car)
    # Verify
    assert rewult is not None
