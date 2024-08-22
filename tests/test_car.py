# import pytest
# import logging
# from interface_adapters.repositories.car_repository import CarRepository
# from use_cases.car_use_case import CarUseCase


# def test_get_car_list(car_repo, transaction_manager, test_logger):
#     # Setup
#     car_use_case = CarUseCase(car_repo, transaction_manager)

#     # Test
#     result = car_use_case.get_car_list()
#     # test_logger.debug(result)
#     # Verify
#     assert result is not None
#     assert len(result) > 0
#     assert result[0].car_id is not None


# def test_get_car_list_paged(car_repo, transaction_manager, test_logger):
#     # Setup
#     car_use_case = CarUseCase(car_repo, transaction_manager)

#     # Test
#     result = car_use_case.get_car_list_paged(1, 10)
#     # test_logger.info(result)
#     # Verify
#     assert result is not None
#     assert len(result) > 0
#     assert len(result) <= 10
