from unittest import TestCase
from unittest.mock import patch

from src.model.models import Person


class TestPerson(TestCase):

    def testConstructPersonWithNoBirthDate(self):
        with patch('flask_sqlalchemy._QueryProperty.__get__', autospec=True):
            person = Person(name='john')

            self.assertEqual('john', person.name)
            self.assertIsNone(person.id)
            self.assertIsNone(person.birth_date)

    def testConstructPersonWithBirthDate(self):
        with patch('flask_sqlalchemy._QueryProperty.__get__', autospec=True):
            person = Person(name='john', birth_date='01/01/1975')

            self.assertEqual('john', person.name)
            self.assertEqual('01/01/1975', person.birth_date)
            self.assertIsNone(person.id)
