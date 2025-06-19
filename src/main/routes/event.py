from flask import Blueprint, jsonify

# agregador de rotas
event_route_bp = Blueprint('event_route', __name__)

@event_route_bp.route('/event', methods=['POST'])
def create_event():

    return jsonify({"message": "Evento criado com sucesso"}), 201
