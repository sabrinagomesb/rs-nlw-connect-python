from flask import Blueprint, jsonify, request

from src.controllers.eventos.eventos_creator import EventosCreator
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

from src.validators.events_creator_validator import events_creator_validator
from src.model.repositories.eventos_repository import EventosRepository
# agregador de rotas
event_route_bp = Blueprint('event_route', __name__)

@event_route_bp.route('/event', methods=['POST'])

def create_event():
    events_creator_validator(request)
    http_request = HttpRequest(body=request.json)

    eventos_repository = EventosRepository()
    eventos_creator = EventosCreator(eventos_repository)

    http_response = eventos_creator.create(http_request)

    return jsonify(http_response.body), http_response.status_code

