import uuid

from interface_adapters.repositories.user_repository import UserRepository
from entities.user import User

class UserUseCase:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def createUser(self, user: User):
        return self.user_repo.save(user)

    def createUser(self, username, password):
        user_id = str(uuid.uuid4())
        user = User(user_id, username, password)
        return self.user_repo.save(user)