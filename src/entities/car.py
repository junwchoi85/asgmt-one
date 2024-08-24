from enum import Enum
from entities.base_entity import BaseEntity
from entities.car_rental_terms import CarRentalTerms


class Status(Enum):
    ACTIVE = 'active',
    INACTIVE = 'inactive',
    DELETED = 'deleted',


class Car(BaseEntity):
    """
    Represents a car entity.
    """

    def __init__(self,
                 car_id: int, car_code: str, name: str, year: str,
                 passenger: int, transmission: str, luggage_large: int,
                 luggage_small: int, engine: str, fuel: str,
                 status: Status = Status.ACTIVE,
                 created_at=None, created_by=None, updated_at=None, updated_by=None,
                 car_rental_terms: CarRentalTerms = None):
        self.car_id = car_id
        self.car_code = car_code
        self.name = name
        self.year = year
        self.passenger = passenger
        self.transmission = transmission
        self.luggage_large = luggage_large
        self.luggage_small = luggage_small
        self.engine = engine
        self.fuel = fuel
        self.status = status
        # Car rental terms
        self.car_rental_terms = car_rental_terms

        super().__init__(created_at, created_by, updated_at, updated_by)
