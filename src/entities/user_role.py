from dataclasses import dataclass, field

@dataclass
class UserRole:
    user_id: str = ''
    role_id: str = ''