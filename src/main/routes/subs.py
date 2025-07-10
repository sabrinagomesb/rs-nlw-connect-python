from flask import Blueprint, jsonify, request

subs_route_bp = Blueprint('subs_route', __name__)

from src.http_types.http_request import HttpRequest
from src.validators.inscritos_creator_validator import inscritos_creator_validator
from src.controllers.inscritos.inscritos_creator import InscritosCreator
from src.model.repositories.inscritos_repository import InscritosRepository

@subs_route_bp.route('/subscriber', methods=['POST'])
def create_subscriber():
    inscritos_creator_validator(request)
    http_request = HttpRequest(body=request.json)

    inscritos_repository = InscritosRepository()
    inscritos_creator = InscritosCreator(inscritos_repository)

    http_response = inscritos_creator.create(http_request)

    return jsonify(http_response.body), http_response.status_code
