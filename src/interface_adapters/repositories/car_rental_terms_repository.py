from typing import Optional
from entities.car_rental_terms import CarRentalTerms
from frameworks_drivers.db.transaction_manager import TransactionManager
from interface_adapters.repositories.repository_interface import RepositoryInterface


class CarRentalTermsRepository(RepositoryInterface):
    def __init__(self, transaction_mngr: TransactionManager):
        # self.connection = transaction_mngr.transaction_scope()
        self.transaction_mngr = transaction_mngr

    def create(self, car: CarRentalTerms) -> int:
        pass

    def read(self, id: int) -> Optional[dict]:
        pass

    def update(self, car: CarRentalTerms) -> bool:
        pass

    def delete(self, id: int) -> bool:
        pass

    # car rental terms section
    # TODO : Consider moving this to a separate repository
    def get_rental_terms(self, cursor, req: dict) -> CarRentalTerms:

        query, query_params = self._build_query(req)
        self.transaction_mngr.execute(query, query_params)

        row = cursor.fetchone()
        car_rental_terms = CarRentalTerms(
            car_rtr_id=row[0],
            car_id=row[1],
            min_rental_days=row[2],
            max_rental_days=row[3],
            price_per_day=row[4],
        )
        return car_rental_terms

    # private method to build query
    def _build_query(self, req: dict) -> tuple:
        query = 'SELECT * FROM car_rental_terms'
        conditions = []
        query_params = []

        # Build the query
        if req.get('car_id'):
            conditions.append('car_id = ?')
            query_params.append(req['car_id'])
        if req.get('min_rental_days'):
            conditions.append('min_rental_days = ?')
            query_params.append(req['min_rental_days'])
        if req.get('max_rental_days'):
            conditions.append('max_rental_days = ?')
            query_params.append(req['max_rental_days'])
        if req.get('price_per_day'):
            conditions.append('price_per_day = ?')
            query_params.append(req['price_per_day'])

        if conditions:
            query += ' WHERE ' + ' AND '.join(conditions)
        # Build query ends

        return query, query_params
