from use_cases.user_use_case import UserUseCase

class UserController:
    # Initialize the user controller with the user repository
    def __init__(self, user_repo):
        self.create_user_use_case = UserUseCase(user_repo)

    # Create a user
    def create_user(self, user):
        return UserUseCase(self.user_repo).createUser(user)