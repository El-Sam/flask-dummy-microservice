from unittest import TestCase, mock
from flask import Response
from api import init_app
from config import config
from application.resource.resources import Person
from api.controller import create_person, get_persons, get_person, Service
from uuid import uuid4
from json import loads


class TestController(TestCase):

    def setUp(self):
        self.app = init_app(config.get('test'))
        self.app.test_request_context().push()
        self.service = mock.Mock(spec_set=Service)

    def test_get_persons(self):
        person_id = uuid4()

        person_mock = mock.Mock(spec_set=Person)
        person_mock.configure_mock(**{
            'id': person_id,
            'name': 'jane',
            'birth_date': None
        })

        self.service.configure_mock(**{
            'fetch_all_persons_service.return_value': ({'persons': [person_mock]}, 200)
        })

        response = get_persons(self.service)

        self.assertIsInstance(cls=Response, obj=response)
        self.assertEqual(200, response.status_code)
        self.assertEqual({
            'persons': [{'id': str(person_id), 'name': 'jane', 'birth_date': None}]},
            loads(response.data)
        )

    def test_get_person(self):
        person_id = uuid4()

        person_mock = mock.Mock(spec_set=Person)
        person_mock.configure_mock(**{
            'id': person_id,
            'name': 'jane',
            'birth_date': None
        })

        self.service.configure_mock(**{
            'get_person_service.return_value': (person_mock, 200)
        })

        response = get_person(self.service, person_id)

        self.assertIsInstance(cls=Response, obj=response)
        self.assertEqual(200, response.status_code)
        self.assertEqual({'id': str(person_id), 'name': 'jane', 'birth_date': None}, loads(response.data))

    def test_create_person(self):
        person_id = uuid4()

        person_mock = mock.Mock(spec_set=Person)
        person_mock.configure_mock(**{
            'id': person_id,
            'name': 'jane',
            'birth_date': None
        })

        self.service.configure_mock(**{
            'create_person_service.return_value': (person_mock, 201)
        })

        with mock.patch('api.controller.request') as request_mock:
            request_mock.return_value = request = mock.Mock()
            request.get_json.return_value = {}

            response = create_person(self.service)

            self.assertIsInstance(cls=Response, obj=response)
            self.assertEqual(201, response.status_code)
            self.assertEqual({'id': str(person_id), 'name': 'jane', 'birth_date': None}, loads(response.data))
