from abc import ABC, abstractmethod
from src.model.entities.inscritos import Inscritos

class InscritosRepositoryInterface(ABC):

    @abstractmethod
    def insert(self, dados_inscrito: dict) -> None:
        pass

    @abstractmethod
    def get_subscriber(self, email: str, evento_id: int) -> Inscritos:
        pass
