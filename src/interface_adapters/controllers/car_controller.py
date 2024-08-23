from typing import List
from entities.car import Car
from use_cases.car_use_case import CarUseCase


class CarController:
    def __init__(self, car_use_case: CarUseCase):
        self.car_use_case = car_use_case

    def get_car_list(self):
        return self.car_use_case.get_car_list()

    def get_car_list_paged(self, page: int, page_size: int) -> List[Car]:
        return self.car_use_case.get_car_list_paged(page=1, page_size=10)
