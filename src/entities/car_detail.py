from entities.base_entity import BaseEntity


class CarDetail(BaseEntity):
    """
    Represents a car detail entity.
    """

    def __init__(self,
                 car_dtl_id: int, car_id: int, mileage: str, color: str, vin: str, status: str,
                 created_at=None, created_by=None, updated_at=None, updated_by=None):
        self.car_dtl_id = car_dtl_id
        self.car_id = car_id
        self.mileage = mileage
        self.color = color
        self.vin = vin
        self.status = status

        super().__init__(created_at, created_by, updated_at, updated_by)
