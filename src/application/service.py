from .factory import Factory
from injector import inject
from infrastructure.persistence.repositories import PersonRepository


class Service(object):
    @inject
    def __init__(self, factory: Factory, person_repository: PersonRepository):
        self.__factory = factory
        self.__person_repository = person_repository

    def fetch_all_persons_service(self):
        persons = self.__factory.get_all_persons()

        return {'persons': persons}, 200

    def create_person_service(self, body):
        person = self.__factory.create_person_model(body)
        self.__person_repository.save(person)
        person = self.__factory.create_person_resource_from_model(person)

        return person, 201

    def get_person_service(self, id: str):
        person = self.__factory.get_person_model(id)

        return self.__factory.create_person_resource_from_model(person), 200
