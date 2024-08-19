from typing import Optional
from entities.booking import Booking
from frameworks_drivers.db.transaction_manager import TransactionManager
from interface_adapters.repositories.repository_interface import RepositoryInterface


class BookingRepository(RepositoryInterface):
    def __init__(self, transaction_mngr: TransactionManager):
        self.connection = transaction_mngr.transaction_scope()

    def create(self, booking: Booking) -> int:
        pass

    def read(self, id: int) -> Optional[dict]:
        pass

    def update(self, booking: Booking) -> bool:
        pass

    def delete(self, id: int) -> bool:
        pass

    def book_car(self, req: dict) -> int:
        cursor = self.connection.cursor()
        cursor.execute(
            '''
            INSERT INTO booking (cst_id, car_dtl_id, start_date, end_date, total_fee, status)
            VALUES (?, ?, ?, ?, ?, ?)
            ''',
            (req['cst_id'], req['car_dtl_id'], req['start_date'], req['end_date'], req['total_fee'], req['status']))
        return cursor.lastrowid
