import pytest
import logging
from interface_adapters.repositories.car_repository import CarRepository
from use_cases.car_use_case import CarUseCase


@pytest.fixture
def car_repo(transaction_manager):
    return CarRepository(transaction_manager)


def test_get_car_list(car_repo, transaction_manager):
    # Setup
    car_use_case = CarUseCase(car_repo, transaction_manager)

    # Test
    result = car_use_case.get_car_list()
    # Verify
    assert result is not None
    assert len(result) > 0


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
