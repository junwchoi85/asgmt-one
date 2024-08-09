from uuid import UUID, uuid4
from dataclasses import dataclass, field

@dataclass
class Role:
    role_id: UUID = field(default_factory=uuid4)
    role_code: str = ''
    desc: str = ''