from src.model.repositories.interfaces.eventos_repository import EventosRepositoryInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class EventosCreator:
    def __init__(self, eventos_repository: EventosRepositoryInterface):
        self.__eventos_repository = eventos_repository

    def create(self, http_request: HttpRequest) -> HttpResponse:
        eventos_info = http_request.body["data"]
        evento_name = eventos_info["name"]

        self.__check_event_exists(evento_name)
        evento_id = self.__insert_event(evento_name)

        return self.__format_response(evento_name, evento_id)

    def __check_event_exists(self, evento_nome: str) -> None:
        response = self.__eventos_repository.get_event(evento_nome)
        if response: raise Exception(f"Evento {evento_nome} já existe")

    def __insert_event(self, evento_nome: str) -> int:
        return self.__eventos_repository.insert(evento_nome)

    def __format_response(self, evento_nome: str, evento_id: int) -> HttpResponse:
        return HttpResponse(
            body={
                "data": {
                    "type": "eventos",
                    "count": 1,
                    "attributes": {
                        "id": evento_id,
                        "event_name": evento_nome
                    }
                }
            },
            status_code=201
        )
