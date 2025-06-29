from src.model.configs.connection import DBConnectionHandler
from src.model.entities.inscritos import Inscritos
from src.model.repositories.interfaces.inscritos_repository import InscritosRepositoryInterface

class InscritosRepository(InscritosRepositoryInterface):
    def insert(self, dados_inscrito: dict) -> None:
        with DBConnectionHandler() as db_handler:
            try:
                novo_inscrito = Inscritos(
                    nome=dados_inscrito.get("nome"),
                    email=dados_inscrito.get("email"),
                    link=dados_inscrito.get("link"),
                    evento_id=dados_inscrito.get("evento_id")
                )

                db_handler.session.add(novo_inscrito)
                db_handler.session.commit()
            except Exception as e:
                db_handler.session.rollback()
                raise e

    def get_subscriber(self, email: str, evento_id: int) -> Inscritos:
        with DBConnectionHandler() as db_handler:
            data = (
                db_handler.session
                .query(Inscritos)
                .filter(
                    Inscritos.email == email,
                    Inscritos.evento_id == evento_id)
                .one_or_none()
            )
            return data
