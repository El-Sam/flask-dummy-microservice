from unittest import TestCase
from src.model.models import Person
from app import app


class TestPerson(TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False

    def testConstructPersonWithNoBirthDate(self):
        person = Person(name='john')

        self.assertEqual('john', person.name)
        self.assertIsNone(person.id)
        self.assertIsNone(person.birth_date)

    def testConstructPersonWithBirthDate(self):
        person = Person(name='john', birth_date='01/01/1975')

        self.assertEqual('john', person.name)
        self.assertEqual('01/01/1975', person.birth_date)
        self.assertIsNone(person.id)
