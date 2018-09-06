from unittest import TestCase, mock
from application.service import Service, PersonRepository
from application.factory import Factory, Person, PersonModel


class TestService(TestCase):

    def setUp(self):
        self.factory = mock.Mock(spec_set=Factory)
        self.repo = mock.Mock(spec_set=PersonRepository)
        self.service = Service(self.factory, self.repo)

    def test_fetch_all_persons_service(self):
        attrs = {
            'get_all_persons.return_value': [
                mock.Mock(spec_set=Person),
                mock.Mock(spec_set=Person),
                mock.Mock(spec_set=Person),
            ]
        }

        self.factory.configure_mock(**attrs)

        result = self.service.fetch_all_persons_service()

        self.assertEqual(3, len(result[0]['persons']))
        self.assertEqual(200, result[1])

    def test_create_person_service(self):
        factory_attrs = {
            'create_person_model.return_value': mock.Mock(spec_set=PersonModel),
            'create_person_resource_from_model.return_value': mock.Mock(spec_set=Person)
        }
        repo_attrs = {
            'save.return_value': None,
        }

        self.factory.configure_mock(**factory_attrs)
        self.repo.configure_mock(**repo_attrs)

        result = self.service.create_person_service({})

        self.assertIsInstance(cls=Person, obj=result[0])
        self.assertEqual(201, result[1])

    def test_get_person_service(self):

        factory_attrs = {
            'get_person_model.return_value': mock.Mock(spec_set=PersonModel),
            'create_person_resource_from_model.return_value': mock.Mock(spec_set=Person)
        }

        self.factory.configure_mock(**factory_attrs)

        result = self.service.get_person_service({})

        self.assertIsInstance(cls=Person, obj=result[0])
        self.assertEqual(200, result[1])
