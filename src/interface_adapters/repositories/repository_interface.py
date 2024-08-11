from abc import ABC, abstractmethod

class RepositoryInterface(ABC):
    @abstractmethod
    def read(self, id: int):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def create(self, entity):
        pass

    @abstractmethod
    def update(self, entity):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass