from src.model.configs.connection import DBConnectionHandler
from src.model.entities.eventos import Eventos

class EventosRepository:
    def insert(self, event_name: str) -> None:
        with DBConnectionHandler() as db_handler:
            try:
                new_event = Eventos(nome=event_name)
                db_handler.session.add(new_event)
                db_handler.session.commit()
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
