from use_cases.user_use_case import UserUseCase

class UserController:
    def __init__(self, user_use_case: UserUseCase):
        self.user_use_case = user_use_case
    
    def sign_up(self, username, password):
        return self.user_use_case.sign_up(username, password)
    
    def sign_in(self, username, password):
        return self.user_use_case.sign_in(username, password)