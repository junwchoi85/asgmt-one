from entities.base_entity import BaseEntity


class CarRentalTerms(BaseEntity):
    """
    Represents a car rental terms entity.
    """

    def __init__(self,
                 car_rtr_id: int,
                 car_id: int,
                 min_rent_period: int,
                 max_rent_period: int,
                 price_per_day: float,
                 created_at=None, created_by=None, updated_at=None, updated_by=None):
        self.car_rtr_id = car_rtr_id
        self.car_id = car_id
        self.min_rent_period = min_rent_period
        self.max_rent_period = max_rent_period
        self.price_per_day = price_per_day

        super().__init__(created_at, created_by, updated_at, updated_by)
