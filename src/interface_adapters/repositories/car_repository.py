from typing import Optional
from entities.car import Car
from entities.car_detail import CarDetail
from entities.car_rental_terms import CarRentalTerms
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

    def find_by_car_code(self, car_code: str) -> Optional[Car]:
        cursor = self.connection.cursor()
        cursor.execute(
            '''
            SELECT * FROM car
            WHERE car_code = ?
            ''', (car_code,))
        row = cursor.fetchone()
        if row is None:
            return None
        return Car(
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

    def get_car_list(self) -> list[Car]:
        cursor = self.connection.cursor()
        cursor.execute(
            '''
            SELECT 
                car.car_id,
                car.car_code,
                car.name,
                car.year,
                car.passenger,
                car.transmission,
                car.luggage_large,
                car.luggage_small,
                car.engine,
                car.fuel,
                crt.price_per_day
            FROM 
                car car,
                car_rental_terms crt
            where car.CAR_id = crt.car_id
            ''')
        rows = cursor.fetchall()
        # print(rows)
        car_list = []
        for row in rows:
            car_rental_terms = CarRentalTerms(
                price_per_day=row[10]
            )

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
                fuel=row[9],
                car_rental_terms=car_rental_terms
            )
            car_list.append(car)
        return car_list

    def get_car_list_paged(self, page: int, page_size: int) -> list[Car]:
        offset = (page - 1) * page_size
        cursor = self.connection.cursor()
        cursor.execute(
            '''
            SELECT 
                car.car_id,
                car.car_code,
                car.name,
                car.year,
                car.passenger,
                car.transmission,
                car.luggage_large,
                car.luggage_small,
                car.engine,
                car.fuel,
                crt.price_per_day
            FROM 
                car car,
                car_rental_terms crt
            where car.CAR_id = crt.car_id
            LIMIT ? OFFSET ?
            ''', (page_size, offset))
        rows = cursor.fetchall()
        car_list = []
        for row in rows:
            car_rental_terms = CarRentalTerms(
                price_per_day=row[10]
            )

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
                fuel=row[9],
                car_rental_terms=car_rental_terms
            )
            car_list.append(car)
        return car_list

    # car detail section
    # TODO : Consider moving this to a separate repository
    def select_car_detail(self, req: dict) -> CarDetail:
        car_id = req['car_id']

        cursor = self.connection.cursor()
        cursor.execute(
            '''
            SELECT * FROM car_detail
            WHERE car_id = ?
            AND status = 'Available'
            ORDER BY RANDOM()
            LIMIT 1
            ''', (car_id,))
        row = cursor.fetchone()
        car_detail = CarDetail(
            car_dtl_id=row[0],
            car_id=row[1],
            mileage=row[2],
            color=row[3],
            vin=row[4],
            status=row[5]
        )
        return car_detail
