from entities.base_entity import BaseEntity


class Customer(BaseEntity):
    """
    Represents a customer entity.
    """

    def __init__(self, cst_id: int, cst_code: str, username: str, password: str):
        self.cst_id = cst_id
        self.cst_code = cst_code
        self.username = username
        self.password = password
