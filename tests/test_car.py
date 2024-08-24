import pytest
import logging
from entities.car import Car
from interface_adapters.repositories.car_repository import CarRepository
from use_cases.car_use_case import CarUseCase
from use_cases.user_use_case import UserUseCase


def test_get_car_list(car_repo, transaction_manager, test_logger):
    # Setup
    car_use_case = CarUseCase(car_repo, transaction_manager)

    # Test
    result = car_use_case.get_car_list()
    # test_logger.debug(result)
    # Verify
    assert result is not None
    assert len(result) > 0
    assert result[0].car_id is not None


def test_get_car_list_paged(car_repo, transaction_manager, test_logger):
    # Setup
    car_use_case = CarUseCase(car_repo, transaction_manager)

    # Test
    result = car_use_case.get_car_list_paged(1, 10)
    # test_logger.info(result)
    # Verify
    assert result is not None
    assert len(result) > 0
    assert len(result) <= 10


def test_update_car_info(user_repo,
                         booking_repo,
                         car_repo,
                         transaction_manager, test_logger):
    user_use_case = UserUseCase(
        user_repo, booking_repo, car_repo, transaction_manager)

    req = {
        'car_id': 1,
        'name': 'Test Car',
        'year': '2021',
        'passenger': 4,
        'transmission': 'Automatic',
        'luggage_large': 2,
        'luggage_small': 1,
        'engine': 'V6',
        'fuel': 'Gasoline',
        'status': 'inactive'
    }

    result = user_use_case.update_car_info(req)
    assert result is not None


def test_delete_car(user_repo,
                    booking_repo,
                    car_repo,
                    transaction_manager, test_logger):
    user_use_case = UserUseCase(
        user_repo, booking_repo, car_repo, transaction_manager)

    req = {
        'car_id': 1
    }

    result = user_use_case.delete_car_info(req)
    assert result is not None

    result = user_use_case.get_car_info(req)
    assert type(result) is Car
    assert result.status == 'deleted'


def test_create_carr(user_repo,
                     booking_repo,
                     car_repo,
                     transaction_manager, test_logger):
    user_use_case = UserUseCase(
        user_repo, booking_repo, car_repo, transaction_manager)

    req = {
        'car_code': 'test',
        'name': 'Test Car',
        'year': '2021',
        'passenger': 4,
        'transmission': 'Automatic',
        'luggage_large': 2,
        'luggage_small': 1,
        'engine': 'V6',
        'fuel': 'Gasoline',
        'status': 'inactive'
    }

    result = user_use_case.add_car_info(req)
    assert result is not None
