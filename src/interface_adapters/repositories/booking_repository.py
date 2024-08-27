from typing import Optional
from entities.booking import Booking
from entities.booking_detail import BookingDetail
from frameworks_drivers.db.transaction_manager import TransactionManager
from interface_adapters.repositories.repository_interface import RepositoryInterface
# from utils.logger import get_app_logger


class BookingRepository(RepositoryInterface):
    def __init__(self, transaction_mngr: TransactionManager):
        # self.connection = transaction_mngr.transaction_scope()
        self.transaction_mngr = transaction_mngr

    def create(self, cursor, booking: Booking) -> int:
        pass

    def read(self, cursor, id: int) -> Optional[dict]:
        pass

    def update(self, cursor, booking: Booking) -> bool:
        pass

    def delete(self, cursor, id: int) -> bool:
        pass

    def book_car(self, cursor,  req: dict) -> int:
        query = '''
            INSERT INTO booking (cst_id, car_dtl_id, start_date, end_date, total_fee, status)
            VALUES (?, ?, ?, ?, ?, ?)
            '''
        params = (req['cst_id'], req['car_dtl_id'], req['start_date'],
                  req['end_date'], req['total_fee'], req['status'])
        self.transaction_mngr.execute(cursor, query, params)
        return cursor.lastrowid

    def get_booking_list(self, cursor, req: dict) -> list[Booking]:
        # build query
        query, query_params = self._build_selection_query(req)
        self.transaction_mngr.log_query(query, query_params)

        cursor.execute(query, query_params)

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

    def update_booking_status(self, cursor, req: dict) -> bool:
        query = '''
            UPDATE booking
            SET status = ?
            WHERE booking_id = ?
            '''
        params = (req['status'], req['booking_id'])
        return self.transaction_mngr.execute(cursor, query, params)

    def _build_selection_query(self, req: dict) -> tuple:
        query = 'SELECT * FROM booking'
        conditions = []
        query_params = []

        if req.get('booking_id'):
            conditions.append('booking_id = ?')
            query_params.append(req['booking_id'])
        if req.get('cst_id'):
            conditions.append('cst_id = ?')
            query_params.append(req['cst_id'])
        if req.get('car_dtl_id'):
            conditions.append('car_dtl_id = ?')
            query_params.append(req['car_dtl_id'])
        if req.get('start_date'):
            conditions.append('start_date = ?')
            query_params.append(req['start_date'])
        if req.get('end_date'):
            conditions.append('end_date = ?')
            query_params.append(req['end_date'])
        if req.get('total_fee'):
            conditions.append('total_fee = ?')
            query_params.append(req['total_fee'])
        if req.get('status'):
            conditions.append('status = ?')
            query_params.append(req['status'])

        if conditions:
            query += ' WHERE ' + ' AND '.join(conditions)

        return query, query_params

    def get_booking_detail_list(self, cursor, req: dict):
        query = '''
            SELECT  c.car_code,
                    c.name,
                    c.year,
                    c.passenger,
                    c.transmission,
                    c.luggage_large,
                    c.luggage_small,
                    c.engine,
                    c.fuel,
                    b.start_date,
                    b.end_date,
                    b.total_fee,
                    b.status
            FROM car c
            JOIN car_detail cd ON c.car_id = cd.car_id
            JOIN booking b ON cd.car_dtl_id = b.car_dtl_id
            WHERE b.cst_id = ?
            '''
        params = (req['cst_id'],)
        self.transaction_mngr.execute(cursor, query, params)

        rows = cursor.fetchall()
        booking_detail_list = []
        for row in rows:
            booking_detail = BookingDetail(
                car_code=row[0],
                name=row[1],
                year=row[2],
                passenger=row[3],
                transmission=row[4],
                luggage_large=row[5],
                luggage_small=row[6],
                engine=row[7],
                fuel=row[8],
                start_date=row[9],
                end_date=row[10],
                total_fee=row[11],
                status=row[12]
            )
            booking_detail_list.append(booking_detail)
        return booking_detail_list
