from src.model.configs.connection import DBConnectionHandler
from src.model.entities.eventos import Eventos
from src.model.repositories.interfaces.eventos_repository import EventosRepositoryInterface

class EventosRepository(EventosRepositoryInterface):
    def insert(self, event_name: str) -> int:
        with DBConnectionHandler() as db_handler:
            try:
                new_event = Eventos(nome=event_name)
                db_handler.session.add(new_event)
                db_handler.session.commit()
                return new_event.id
            except Exception as e:
                db_handler.session.rollback()
                raise e

    def get_event(self, event_name: str) -> Eventos:
        with DBConnectionHandler() as db_handler:
            data = (
                db_handler.session
                .query(Eventos)
                .filter(Eventos.nome == event_name)
                .one_or_none()
            )
            return data
