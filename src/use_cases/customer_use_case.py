
from entities.customer import Customer
from frameworks_drivers.db.transaction_manager import TransactionManager
from interface_adapters.repositories.customer_repository import CustomerRepository


class CustomerUseCase:
    def __init__(self, customer_repository: CustomerRepository, transaction_mngr: TransactionManager):
        self.customer_repository = customer_repository
        self.transaction_mngr = transaction_mngr

    def register_customer(self, customer_data: dict) -> int:
        with self.transaction_mngr.transaction_scope():
            customer = Customer(
                cst_id = None,
                cst_code = None,
                username=customer_data['username'],
                password=customer_data['password']
            )
            return self.customer_repository.create(customer)