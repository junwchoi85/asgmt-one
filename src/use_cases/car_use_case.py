from typing import List
from entities.car import Car
from frameworks_drivers.db.transaction_manager import TransactionManager
from interface_adapters.repositories.car_repository import CarRepository


class CarUseCase:
    def __init__(self, car_repo: CarRepository, transaction_mngr: TransactionManager):
        self.car_repo = car_repo
        self.transaction_mngr = transaction_mngr

    def get_car_list(self) -> List[Car]:
        with self.transaction_mngr.transaction_scope():
            return self.car_repo.get_car_list()

    def get_car_list_paged(self, page: int, page_size: int) -> List[Car]:
        with self.transaction_mngr.transaction_scope():
            return self.car_repo.get_car_list_paged(page, page_size)

    def get_car_rental_terms_by_car_id(self, req) -> List[Car]:
        with self.transaction_mngr.transaction_scope():
            car_id = req['car_id']
            return self.car_repo.get_car_rental_terms(car_id)
