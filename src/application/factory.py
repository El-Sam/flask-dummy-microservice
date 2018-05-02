from typing import List

from application.resource.resources import Person
from application.exceptions.exceptions import NotFoundException, MissingPropertyException
from model.models import Person as PersonModel


class Factory(object):

    def get_all_persons(self) -> List[Person]:
        persons = [Person(id=person_model.id, name=person_model.name, birth_date=person_model.birth_date)
                   for person_model in PersonModel.query.all()]
        return persons

    def create_person_model(self, body):
        try:
            person = PersonModel(body['name'], body.get('birth_date', None))
            return person
        except KeyError as e:
            raise MissingPropertyException(property_name=str(e))

    def create_person_resource_from_model(self, person_model: PersonModel):
        person_resource = Person(id=person_model.id, name=person_model.name, birth_date=person_model.birth_date)
        return person_resource

    def get_person_model(self, id: str):
        person = PersonModel.query.get(id)

        if person is None:
            raise NotFoundException()

        return person
