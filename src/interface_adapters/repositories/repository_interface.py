from abc import ABC, abstractmethod
from typing import Optional

class RepositoryInterface(ABC):

    @abstractmethod
    def create(self, entity) -> int:
        """
        Create a new entity
        :param entity: Entity to be created
        :return: The id of the created entity
        """
        pass

    @abstractmethod
    def read(self, id: int) -> Optional[dict]:
        """
        Read an entity by id
        :param id: Entity id
        :return: Entity
        """
        pass

    @abstractmethod
    def update(self, entity) -> bool:
        """
        Update an entity
        :param entity: Entity to be updated
        :return: True if the entity was updated, False otherwise
        """
        pass

    @abstractmethod
    def delete(self, id: int)-> bool:
        """
        Delete an entity
        :param id: Entity id
        :return: True if the entity was deleted, False otherwise
        """
        pass