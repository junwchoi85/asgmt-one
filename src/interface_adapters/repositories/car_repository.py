from typing import Optional
from entities.car import Car
from entities.car_detail import CarDetail
from entities.car_rental_terms import CarRentalTerms
from frameworks_drivers.db.transaction_manager import TransactionManager
from interface_adapters.repositories.repository_interface import RepositoryInterface
from utils.logger import get_app_logger


class CarRepository(RepositoryInterface):
    def __init__(self, transaction_mngr: TransactionManager):
        self.connection = transaction_mngr.transaction_scope()
        self.transaction_mngr = transaction_mngr
        # self.logger = get_app_logger()

    def create_car_code(self, cursor) -> str:
        # car_code = 'car-011'
        query = '''
            SELECT MAX(car_code) FROM car
            '''
        params = ()
        self.transaction_mngr.execute(cursor, query, params)
        row = cursor.fetchone()
        if row is None:
            return 'car-001'
        car_code = row[0]
        if car_code is None:
            return 'car-001'
        car_code = car_code.split('-')
        car_code = int(car_code[1]) + 1
        return f'car-{car_code:03}'

    def create(self, cursor, req: dict) -> int:
        """
        insert car info
        return car_id
        """
        query = '''
            INSERT INTO car (car_code, name, year, passenger, transmission, luggage_large, luggage_small, engine, fuel)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            '''
        params = (
            req['car_code'],
            req['name'],
            req['year'],
            req['passenger'],
            req['transmission'],
            req['luggage_large'],
            req['luggage_small'],
            req['engine'],
            req['fuel']
        )
        self.transaction_mngr.execute(cursor, query, params)
        return cursor.lastrowid

    def read(self, cursor, id: int) -> Optional[Car]:
        """
        select car by id
        return car info
        """
        query = '''
            SELECT * FROM car
            WHERE car_id = ?
            '''
        params = (id,)
        self.transaction_mngr.execute(cursor, query, params)
        row = cursor.fetchone()
        if row:
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
                fuel=row[9],
                status=row[10]
            )
        return None

    def update(self, cursor, req: dict) -> bool:
        query, query_params = self._build_car_update_query(req)
        return cursor.execute(query, query_params)

    def delete(self, cursor, req: dict) -> bool:
        query, query_params = self._build_car_update_query(req)
        return cursor.execute(query, query_params)

    def _build_car_update_query(self, req: dict) -> tuple:
        query = 'UPDATE car SET '
        update_fields = []
        query_params = []

        # Build the query
        if 'name' in req and req['name']:
            update_fields.append('name = ?')
            query_params.append(req['name'])
        if 'year' in req and req['year']:
            update_fields.append('year = ?')
            query_params.append(req['year'])
        if 'passenger' in req and req['passenger']:
            update_fields.append('passenger = ?')
            query_params.append(req['passenger'])
        if 'transmission' in req and req['transmission']:
            update_fields.append('transmission = ?')
            query_params.append(req['transmission'])
        if 'luggage_large' in req and req['luggage_large']:
            update_fields.append('luggage_large = ?')
            query_params.append(req['luggage_large'])
        if 'luggage_small' in req and req['luggage_small']:
            update_fields.append('luggage_small = ?')
            query_params.append(req['luggage_small'])
        if 'engine' in req and req['engine']:
            update_fields.append('engine = ?')
            query_params.append(req['engine'])
        if 'fuel' in req and req['fuel']:
            update_fields.append('fuel = ?')
            query_params.append(req['fuel'])
        if 'status' in req and req['status']:
            update_fields.append('status = ?')
            query_params.append(req['status'])

        if update_fields:
            query += ', '.join(update_fields)
        query += ' WHERE car_id = ?'
        query_params.append(req['car_id'])
        # Build query ends
        # self.logger.debug(query)
        # self.logger.debug(query_params)
        # self.logger.debug('Update car info query built successfully')
        return query, query_params

    def find_by_car_code(self, cursor, car_code: str) -> Optional[Car]:
        query = '''
            SELECT * FROM car
            WHERE car_code = ?
            '''
        params = (car_code,)
        self.transaction_mngr.execute(cursor, query, params)
        row = cursor.fetchone()
        if row:
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
                fuel=row[9],
                status=row[10]
            )
        return None

    def get_car_list(self, cursor) -> list[Car]:
        query = '''
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
                car.status,
                crt.price_per_day
            FROM 
                car car,
                car_rental_terms crt
            where car.CAR_id = crt.car_id
            '''
        params = ()
        self.transaction_mngr.execute(cursor, query, params)

        rows = cursor.fetchall()
        # print(rows)
        car_list = []
        for row in rows:
            car_rental_terms = CarRentalTerms(
                price_per_day=row[11]
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
                status=row[10],
                car_rental_terms=car_rental_terms
            )
            car_list.append(car)
        return car_list

    def get_car_list_paged(self, cursor, page: int, page_size: int) -> list[Car]:
        offset = (page - 1) * page_size
        query = '''
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
                car.status,
                crt.price_per_day
            FROM 
                car car,
                car_rental_terms crt
            where car.CAR_id = crt.car_id
            and car.status = 'ACTIVE'
            LIMIT ? OFFSET ?
        '''
        params = (page_size, offset)
        self.transaction_mngr.execute(cursor, query, params)
        rows = cursor.fetchall()

        car_list = []
        for row in rows:
            car_rental_terms = CarRentalTerms(
                price_per_day=row[11]
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
                status=row[10],
                car_rental_terms=car_rental_terms
            )
            car_list.append(car)
        return car_list

    # car detail section
    # TODO : Consider moving this to a separate repository
    def select_car_detail(self, cursor, req: dict) -> CarDetail:
        car_id = req['car_id']

        query = '''
            SELECT * FROM car_detail
            WHERE car_id = ?
            AND status = 'Available'
            ORDER BY RANDOM()
            LIMIT 1
            '''
        params = (car_id,)
        self.transaction_mngr.execute(cursor, query, params)
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

    # car rental terms section
    # TODO : Consider moving this to a separate repository
    def get_rental_terms(self, cursor, req: dict) -> CarRentalTerms:

        query, query_params = self._build_car_rental_term_query(req)

        cursor.execute(query, query_params)
        row = cursor.fetchone()
        car_rental_terms = CarRentalTerms(
            car_rtr_id=row[0],
            car_id=row[1],
            min_rent_period=row[2],
            max_rent_period=row[3],
            price_per_day=row[4],
        )
        return car_rental_terms

    # private method to build query
    def _build_car_rental_term_query(self, req: dict) -> tuple:
        query = 'SELECT * FROM car_rental_terms'
        conditions = []
        query_params = []

        # Build the query
        if req['car_id']:
            conditions.append('car_id = ?')
            query_params.append(req['car_id'])
        if req['min_rent_period']:
            conditions.append('min_rent_period = ?')
            query_params.append(req['min_rent_period'])
        if req['max_rent_period']:
            conditions.append('max_rent_period = ?')
            query_params.append(req['max_rent_period'])
        if req['price_per_day']:
            conditions.append('price_per_day = ?')
            query_params.append(req['price_per_day'])

        if conditions:
            query += ' WHERE ' + ' AND '.join(conditions)
        # Build query ends

        return query, query_params
