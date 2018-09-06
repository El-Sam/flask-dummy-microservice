from unittest import TestCase

from application.resource.resources import Person


class TestPerson(TestCase):

    def test_init(self):
        person = Person('abc', 'test', None)

        self.assertEqual('abc', person.id)
        self.assertEqual('test', person.name)
        self.assertIsNone(person.birth_date)

        self.assertEqual({
            'id': 'abc',
            'name': 'test',
            'birth_date': None
        }, person.to_json()
        )
