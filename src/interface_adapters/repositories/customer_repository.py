from typing import Optional
from entities.customer import Customer
from frameworks_drivers.db.transaction_manager import TransactionManager
from interface_adapters.repositories.repository_interface import RepositoryInterface


class CustomerRepository(RepositoryInterface):
    def __init__(self, transaction_mngr: TransactionManager):
        self.connection = transaction_mngr.transaction_scope()

    def create(self, cursor, customer: Customer) -> int:
        cursor.execute(
            '''
            INSERT INTO customer (cst_code, username, password)
            VALUES (?, ?, ?)
            ''',
            (customer.cst_code, customer.username, customer.password))
        return cursor.lastrowid

    def read(self, id: int) -> Optional[dict]:
        cursor = self.connection.cursor()
        cursor.execute(
            '''
            SELECT * FROM customer WHERE cst_id = ?
            ''',
            (id,))
        row = cursor.fetchone()
        return dict(row) if row else None

    def update(self, customer: Customer) -> bool:
        # TODO: Implement this method
        pass

    def delete(self, id: int) -> bool:
        # TODO: Implement this method
        pass

    def fetch_latest_customer_code(self, cursor) -> str:
        """
        Generate customer code
        :return: Customer code
        """
        cursor.execute(
            '''
            SELECT cst_code FROM customer ORDER BY cst_id DESC LIMIT 1
            ''')
        row = cursor.fetchone()

        if row:
            return row[0]
        else:
            return 'cst-001'

    def find_by_username(self, username: str) -> Customer:
        """
        Get a customer by username
        :param username: Username
        :return: Customer object
        """
        cursor = self.connection.cursor()
        cursor.execute(
            '''
            SELECT * FROM customer WHERE username = ?
            ''',
            (username,))
        row = cursor.fetchone()
        if row:
            cst_id, cst_code, username, password, created_at, created_by, updated_at, updated_by = row
            return Customer(cst_id=cst_id, cst_code=cst_code, username=username, password=password)
        return None
