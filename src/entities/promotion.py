from datetime import datetime

from entities.base_entity import BaseEntity


class Promotion(BaseEntity):

    def __init__(self,
                 prm_id: int,
                 desc: str,
                 discount_rate: float,
                 dt_start: datetime,
                 dt_end: datetime,
                 created_at=None, created_by=None, updated_at=None, updated_by=None):

        self.prm_id = prm_id
        self.desc = desc
        self.discount_rate = discount_rate
        self.dt_start = dt_start
        self.dt_end = dt_end

        super().__init__(created_at, created_by, updated_at, updated_by)
