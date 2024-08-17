
from use_cases.customer_use_case import CustomerUseCase


class CustomerController:
    def __init__(self, customer_register_use_case: CustomerUseCase):
        self.customer_register_use_case = customer_register_use_case

    def sign_up(self, username, password):
        if not username or not password:
            raise ValueError('Username and password are required')

        customer_data = {
            'username': username,
            'password': password
        }
        result = self.customer_register_use_case.register_customer(customer_data)
        return result