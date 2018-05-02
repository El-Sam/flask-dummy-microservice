from unittest import TestCase
from app import app
from src.infrastructure.persistence.repositories import PersonRepository, Person


class TestPersonRepository(TestCase):

    def setUp(self):
        app.app_context().push()

        self.repository = PersonRepository()

    def testSave(self):
        person = Person(name='Joe', birth_date='01/01/1975')

        self.repository.save(person)
        self.assertIsNotNone(person.id)

        self.repository.remove(person)

    def testRemove(self):
        person = Person(name='Joe', birth_date='01/01/1975')

        self.repository.save(person)

        id = person.id

        self.assertIsNotNone(id)
        self.repository.remove(person)

        person = Person.query.get(id)

        self.assertIsNone(person)
