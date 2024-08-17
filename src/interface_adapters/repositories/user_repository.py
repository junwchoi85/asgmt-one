from typing import Optional
from entities.user import User
from interface_adapters.repositories.repository_interface import RepositoryInterface

class UserRepository(RepositoryInterface):
    def __init__(self, connection):
        self.connection = connection

    def create(self, user: User) -> int:
        pass
    
    def read(self, id: int) -> Optional[dict]:
        cursor = self.connection.cursor()
        cursor.execute(
            '''
            SELECT * FROM user WHERE cst_id = ?
            ''',
            (id,))
        row = cursor.fetchone()
        return dict(row) if row else None
    
    def update(self, entity) -> bool:
        pass

    def delete(self, id: int) -> bool:
        pass

    def find_by_username(self, username: str) -> User:
        cursor = self.connection.cursor()
        cursor.execute(
            '''
            SELECT * FROM user WHERE username = ?
            ''',
            (username,))
        row = cursor.fetchone()
        if row:
            user_id, user_code, username, password, created_at, created_by, updated_at, updated_by  = row
            return User(user_id=user_id, user_code=user_code , username=username, password=password)
        return None