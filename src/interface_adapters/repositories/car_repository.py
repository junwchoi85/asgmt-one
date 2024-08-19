from typing import Optional
from entities.car import Car
from frameworks_drivers.db.transaction_manager import TransactionManager
from interface_adapters.repositories.repository_interface import RepositoryInterface


class CarRepository(RepositoryInterface):
    def __init__(self, transaction_mngr: TransactionManager):
        self.connection = transaction_mngr.transaction_scope()

    def create(self, car: Car) -> int:
        pass

    def read(self, id: int) -> Optional[dict]:
        pass

    def update(self, car: Car) -> bool:
        pass

    def delete(self, id: int) -> bool:
        pass

    def get_car_list(self) -> list:
        cursor = self.connection.cursor()
        cursor.execute(
            '''
            SELECT * FROM car
            ''')
        return cursor.fetchall()

    def get_car_list_paged(self, page: int, page_size: int) -> list[Car]:
        offset = (page - 1) * page_size
        cursor = self.connection.cursor()
        cursor.execute(
            '''
            SELECT * FROM car
            LIMIT ? OFFSET ?
            ''', (page_size, offset))
        rows = cursor.fetchall()
        car_list = []
        for row in rows:
            car = Car(
                car_id=row[0],
                car_code=row[1],
                name=row[2],
                year=row[3],
                passenger=row[4],
                transmission=row[5],
                luggage_large=row[6],
                luggage_small=row[7],
                engine=row[8],
                fuel=row[9]
            )
            car_list.append(car)
        return car_list
