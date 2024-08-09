from interface_adapters.repositories.user_repository import UserRepository
from entities.user import User

class CreateUser:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def execute(self, user: User):
        return self.user_repo.save(user)       