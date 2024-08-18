from use_cases.user_use_case import UserUseCase


class UserController:
    def __init__(self, user_use_case: UserUseCase):
        self.user_use_case = user_use_case

    def sign_in(self, req: dict):
        if not req.get('username') or not req.get('password'):
            raise ValueError('Username and password are required')

        user = self.user_use_case.sign_in(req)
        if user:
            return {"status": "success", "user": user}
        else:
            return {"status": "failure", "message": "Invalid credentials"}
