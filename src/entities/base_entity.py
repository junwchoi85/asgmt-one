from datetime import datetime


class BaseEntity:
    """
    Represents a base entity.
    """

    def __init__(self,
                 created_at: datetime,
                 created_by: str,
                 updated_at: datetime,
                 updated_by: str):
        self.created_at = created_at
        self.created_by = created_by
        self.updated_at = updated_at
        self.updated_by = updated_by
