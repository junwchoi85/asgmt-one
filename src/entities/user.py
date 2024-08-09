from uuid import UUID, uuid4

class User:
    def __init__(self, user_id: UUID, user_code: str, username: str, password: str):
        self.user_id = user_id
        self.user_code = user_code
        self.username = username
        self.password = password
    