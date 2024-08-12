import uuid

from entities.user import User
from interface_adapters.repositories.user_repository import UserRepository
from frameworks_drivers.db_setup.database_setup import TransactionManager

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
    def sign_in(self, username, password):
        with self.transaction_mngr.transaction_scope():
            user = User(None, 
                        self.generate_new_user_code(), 
                        username, 
                        password)
            return self.user_repo.save(user)

    def createUser(self, user:User = None, **kwargs):
        print('createUser called')

        if user is None:
            username = kwargs.get('username')
            password = kwargs.get('password')
            if not username or not password:
                raise ValueError("username과 password는 필수입니다.")
            
            # user_id = str(uuid.uuid4())
            new_user_code = self.generate_new_user_code()
            user = User(None, new_user_code, username, password)
        
        return self.user_repo.save(user)

    def generate_new_user_code(self):
        print('generate_new_user_code called')
        last_user_code = self.user_repo.get_last_user_code()
        if last_user_code is None:
            return '000001'
        new_user_code = str(int(last_user_code) + 1)
        return new_user_code.zfill(6)
    
    def signIn(self, username, password) -> User:
        return self.user_repo.sign_in(username, password)