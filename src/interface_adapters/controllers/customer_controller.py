
from use_cases.customer_use_case import CustomerUseCase


class CustomerController:
    def __init__(self, customer_register_use_case: CustomerUseCase):
        self.customer_register_use_case = customer_register_use_case

    def sign_up(self, req: dict):
        if not req.get('username') or not req.get('password'):
            raise ValueError('Username and password are required')

        result = self.customer_register_use_case.sign_up(
            req)
        return result

    def sign_in(self, req: dict):
        if not req.get('username') or not req.get('password'):
            raise ValueError('Username and password are required')

        result = self.customer_register_use_case.sign_in(req)
        return result
