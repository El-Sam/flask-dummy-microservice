from unittest import TestCase, mock
from unittest.mock import patch

from application.factory import Factory, PersonModel, Person, MissingPropertyException, NotFoundException
from uuid import uuid4


class TestFactory(TestCase):

    def setUp(self):
        self.factory = Factory()

    def test_get_all_persons_with_no_persons_in_db_returns_empty_list(self):
        with mock.patch('application.factory.PersonModel.query', autospec=True) as query_mock:
            query_mock \
                .return_value.all \
                .return_value = None

            persons = self.factory.get_all_persons()

            self.assertFalse(persons)

    def test_get_all_persons_with_2_persons_in_db_returns_two_persons(self):
        with patch('flask_sqlalchemy._QueryProperty.__get__', autospec=True) as query_mock:
            id1 = uuid4()
            id2 = uuid4()

            attrs1 = {
                'id': id1,
                'name': 'john',
                'birth_date': None
            }
            attrs2 = {
                'id': id2,
                'name': 'joe',
                'birth_date': '01/01/1975'
            }

            person1 = mock.Mock(spec_set=PersonModel)
            person1.configure_mock(**attrs1)

            person2 = mock.Mock(spec_set=PersonModel)
            person2.configure_mock(**attrs2)

            query_mock \
                .return_value.all \
                .return_value = [person1, person2]

            persons = self.factory.get_all_persons()

            self.assertEqual(2, len(persons))

            self.assertEqual(id1, persons[0].id)
            self.assertEqual(id2, persons[1].id)

            self.assertEqual('john', persons[0].name)
            self.assertEqual('joe', persons[1].name)

            self.assertIsNone(persons[0].birth_date)
            self.assertEqual('01/01/1975', persons[1].birth_date)

    def test_create_person_model_with_no_birth_date(self):
        with patch('flask_sqlalchemy._QueryProperty.__get__', autospec=True):
            with patch('application.factory.PersonModel', autospec=True) as mock_model:

                model = mock_model.return_value

                body = {
                    'name': 'jane'
                }
                person = self.factory.create_person_model(body)

                self.assertIs(model, person)

    def test_create_person_model_with_no_name_expect_exception(self):
        with patch('flask_sqlalchemy._QueryProperty.__get__', autospec=True):
            with patch('application.factory.PersonModel', autospec=True):
                body = {
                    'birth_date': '22/01/1975'
                }

                with self.assertRaises(MissingPropertyException):
                    self.factory.create_person_model(body)

    def test_create_person_resource_from_model(self):
        with patch('flask_sqlalchemy._QueryProperty.__get__', autospec=True):
            person_id = uuid4()

            attrs1 = {
                'id': person_id,
                'name': 'john',
                'birth_date': None
            }

            person = mock.Mock(spec_set=PersonModel)
            person.configure_mock(**attrs1)

            resource = self.factory.create_person_resource_from_model(person)

            self.assertIsInstance(cls=Person, obj=resource)

            self.assertEqual('john', person.name)
            self.assertEqual(person_id, person.id)
            self.assertIsNone(person.birth_date)

    def test_get_person_model_found(self):
        with patch('flask_sqlalchemy._QueryProperty.__get__', autospec=True) as query_mock:
            person_id = uuid4()

            attrs1 = {
                'id': person_id,
                'name': 'john',
                'birth_date': None
            }

            person = mock.Mock(spec_set=PersonModel)
            person.configure_mock(**attrs1)

            query_mock\
                .return_value.get\
                .return_value = person

            model = self.factory.get_person_model(str(person_id))

            self.assertIs(model, person)

    def test_get_person_model_not_found_expect_exception(self):
        with patch('flask_sqlalchemy._QueryProperty.__get__', autospec=True) as query_mock:

            person_id = uuid4()

            query_mock\
                .return_value.get\
                .return_value = None

            with self.assertRaises(NotFoundException):
                self.factory.get_person_model(str(person_id))
