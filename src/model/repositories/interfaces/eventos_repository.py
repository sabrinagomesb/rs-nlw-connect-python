from abc import ABC, abstractmethod
from src.model.entities.eventos import Eventos

class EventosRepositoryInterface(ABC):

    @abstractmethod
    def insert(self, event_name: str) -> int:
        pass

    @abstractmethod
    def get_event(self, event_name: str) -> Eventos:
        pass

