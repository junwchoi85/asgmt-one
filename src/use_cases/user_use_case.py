import uuid

from entities.user import User
from interface_adapters.repositories.user_repository import UserRepository
from frameworks_drivers.db.database_setup import TransactionManager


class UserUseCase:
    def __init__(self, user_repo: UserRepository, transaction_mngr: TransactionManager):
        self.user_repo = user_repo
        self.transaction_mngr = transaction_mngr

    """
    Python doesn't support method overloading, 
    so we can't have two methods with the same name but different parameters.
    
    def createUser(self, user: User):
        return self.user_repo.save(user)

    def createUser(self, username, password):
        user_id = str(uuid.uuid4())
        
        new_user_code = self.generate_new_user_code()
        user = User(user_id, new_user_code, username, password)
        return self.user_repo.save(user)
    Instead, we can use the arguments
    """

    def sign_in(self, req: dict) -> User:
        username = req.get('username')
        password = req.get('password')

        with self.transaction_mngr.transaction_scope():
            user = self.user_repo.find_by_username(username)
            if not user:
                raise ValueError('User not found')

            if user.password != password:
                raise ValueError('Incorrect password')

            return user

    def sign_up(self, req: dict) -> int:
        username = req.get('username')
        password = req.get('password')

        with self.transaction_mngr.transaction_scope():
            user = self.user_repo.find_by_username(username)
            if user:
                raise ValueError('User already exists')

            new_user_code = self.generate_user_code()
            user = User(None, new_user_code, username, password)
            return self.user_repo.create(user)

    def generate_user_code(self) -> str:
        """
        Generate user code
        """
        code = self.user_repo.fetch_latest_user_code()
        if code:
            code = code.split('-')
            code[1] = str(int(code[1]) + 1).zfill(4)
            return '-'.join(code)
