from typing import Optional
from entities.user import User
from frameworks_drivers.db.transaction_manager import TransactionManager
from interface_adapters.repositories.repository_interface import RepositoryInterface


class UserRepository(RepositoryInterface):
    def __init__(self, transaction_mngr: TransactionManager):
        self.connection = transaction_mngr.transaction_scope()

    def create(self, cursor, user: User) -> int:
        """
        Create a new user.
        """
        cursor.execute(
            '''
            INSERT INTO user (user_code, username, password) VALUES (?, ?, ?)
            ''',
            (user.user_code, user.username, user.password))
        return cursor.lastrowid

    def read(self, cursor, id: int) -> Optional[dict]:
        cursor.execute(
            '''
            SELECT * FROM user WHERE cst_id = ?
            ''',
            (id,))
        row = cursor.fetchone()
        return dict(row) if row else None

    def update(self, cursor, entity) -> bool:
        pass

    def delete(self, cursor, id: int) -> bool:
        pass

    def find_by_username(self, cursor, username: str) -> User:
        cursor.execute(
            '''
            SELECT * FROM user WHERE username = ?
            ''',
            (username,))
        row = cursor.fetchone()
        if row:
            user_id, user_code, username, password, created_at, created_by, updated_at, updated_by = row
            return User(user_id=user_id, user_code=user_code, username=username, password=password)
        return None

    def fetch_latest_user_code(self, cursor) -> str:
        cursor.execute(
            '''
            SELECT user_code FROM user ORDER BY user_id DESC LIMIT 1
            ''')
        row = cursor.fetchone()

        if row:
            return row[0] if row else None
        # if row:
        #     code = row[0]
        #     code = code.split('-')
        #     code = int(code[1]) + 1
        #     return code
