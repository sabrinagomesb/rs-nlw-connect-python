from src.model.repositories.interfaces.inscritos_repository import InscritosRepositoryInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class InscritosCreator:
    def __init__(self, inscritos_repository: InscritosRepositoryInterface):
        self.__inscritos_repository = inscritos_repository

    def create(self, http_request: HttpRequest) -> HttpResponse:
        inscrito_info = http_request.body["data"]
        inscrito_email = inscrito_info["email"]
        inscrito_evento_id = inscrito_info["evento_id"]

        self.__check_subscriber_exists(inscrito_email, inscrito_evento_id)
        self.__insert_subscriber(inscrito_info)
        return self.__format_response(inscrito_info)

    def __check_subscriber_exists(self, inscrito_email: str, inscrito_evento_id: int) -> None:
        response = self.__inscritos_repository.get_subscriber(inscrito_email, inscrito_evento_id)
        if response: raise Exception(f"Inscrito com email {inscrito_email} já existe para o evento {inscrito_evento_id}")

    def __insert_subscriber(self, inscrito_info: dict) -> None:
        self.__inscritos_repository.insert(inscrito_info)

    def __format_response(self, inscrito_info: dict) -> HttpResponse:
        return HttpResponse(
            body={
                "data": {
                    "type": "inscritos",
                    "count": 1,
                    "attributes": inscrito_info
                }
            },
            status_code=201
        )
