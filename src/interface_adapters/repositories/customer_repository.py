from typing import Optional
from entities.customer import Customer
from interface_adapters.repositories.repository_interface import RepositoryInterface


class CustomerRepository(RepositoryInterface) :
    def __init__(self, connection):
        self.connection = connection

    def create(self, customer: Customer) -> int:
        cursor = self.connection.cursor()
        cursor.execute(
            '''
            INSERT INTO customer (cst_id, cst_code, username, password)
            VALUES (?, ?, ?, ?)
            ''',
            (customer.cst_id, self.generate_customer_code(), customer.username, customer.password))
        return cursor.lastrowid
    
    def generate_customer_code(self) -> str:
        """
        Generate customer code
        :return: Customer code
        """
        cursor = self.connection.cursor()
        cursor.execute(
            '''
            SELECT cst_code FROM customer ORDER BY cst_id DESC LIMIT 1
            ''')
        row = cursor.fetchone()
        if row:
            code = row[0]
            # code = code.split('-')
            code = int(code[1]) + 1
            return code
    
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
        return Customer(*row) if row else None
    
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
       #TODO: Implement this method
       pass
    
    def delete(self, id: int) -> bool:
       #TODO: Implement this method
       pass