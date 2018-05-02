from flask import Blueprint, jsonify, request, Response
from injector import inject
from application.service import Service

blueprint = Blueprint('main', __name__)


@blueprint.route('persons', methods=['GET'])
@inject
def get_persons(service: Service) -> Response:
    result = service.fetch_all_persons_service()
    response = jsonify(result[0])
    response.status_code = result[1]
    return response


@blueprint.route('persons', methods=['POST'])
@inject
def create_person(service: Service) -> Response:
    body = request.get_json(force=True)
    result = service.create_person_service(body)
    response = jsonify(result[0])
    response.status_code = result[1]
    return response


@blueprint.route('persons/<string:id>', methods=['GET'])
@inject
def get_person(service: Service, id: str) -> Response:
    result = service.get_person_service(id)
    response = jsonify(result[0])
    response.status_code = result[1]
    return response
