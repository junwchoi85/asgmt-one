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

    def get_booking_list(self, req: dict) -> list[Booking]:
        booking_status = req['status']

        cursor = self.connection.cursor()
        if booking_status is None:
            cursor.execute(
                '''
                SELECT * FROM booking WHERE status IS NOT NULL
                '''
            )
        else:
            cursor.execute(
                '''
                SELECT * FROM booking WHERE status = ?
                ''',
                (booking_status,)
            )
        rows = cursor.fetchall()
        booking_list = []
        for row in rows:
            booking = Booking(
                booking_id=row[0],
                cst_id=row[1],
                car_dtl_id=row[2],
                start_date=row[3],
                end_date=row[4],
                total_fee=row[5],
                status=row[6]
            )
            booking_list.append(booking)
        return booking_list

    def update_booking_status(self, req: dict) -> bool:
        cursor = self.connection.cursor()
        cursor.execute(
            '''
            UPDATE booking
            SET status = ?
            WHERE booking_id = ?
            ''',
            (req['status'], req['booking_id'])
        )
        return True
