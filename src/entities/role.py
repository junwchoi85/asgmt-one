from entities.base_entity import BaseEntity


class Role(BaseEntity):
    """
    Represents a role entity.
    """

    def __init__(self,
                 role_id: int, role_code: str, desc: str,
                 created_at=None, created_by=None, updated_at=None, updated_by=None):
        self.role_id = role_id
        self.role_code = role_code
        self.desc = desc

        super().__init__(created_at, created_by, updated_at, updated_by)
