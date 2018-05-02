from unittest import TestCase, mock
from flask import Response
from app import app
from application.resource.resources import Person
from api.controller import create_person, get_persons, get_person, Service
from uuid import uuid4
from json import loads


class TestController(TestCase):

    def setUp(self):
        app.config['DEBUG'] = False
        app.config['TESTING'] = True
        app.test_request_context().push()

    def test_get_persons(self):
        id = uuid4()

        person_mock = mock.Mock(spec_set=Person)
        person_mock.configure_mock(**{
            'id': id,
            'name': 'jane',
            'birth_date': None
        })

        service = mock.Mock(spec_set=Service)
        service.configure_mock(**{
            'fetch_all_persons_service.return_value': ({'persons': [person_mock]}, 200)
        })

        response = get_persons(service)

        self.assertIsInstance(cls=Response, obj=response)
        self.assertEqual(200, response.status_code)
        self.assertEqual({'persons': [{'id': str(id), 'name': 'jane', 'birth_date': None}]}, loads(response.data))

    def test_get_person(self):
        id = uuid4()

        person_mock = mock.Mock(spec_set=Person)
        person_mock.configure_mock(**{
            'id': id,
            'name': 'jane',
            'birth_date': None
        })

        service = mock.Mock(spec_set=Service)
        service.configure_mock(**{
            'get_person_service.return_value': (person_mock, 200)
        })

        response = get_person(service, id)

        self.assertIsInstance(cls=Response, obj=response)
        self.assertEqual(200, response.status_code)
        self.assertEqual({'id': str(id), 'name': 'jane', 'birth_date': None}, loads(response.data))

    def test_create_person(self):
        id = uuid4()

        person_mock = mock.Mock(spec_set=Person)
        person_mock.configure_mock(**{
            'id': id,
            'name': 'jane',
            'birth_date': None
        })

        service = mock.Mock(spec_set=Service)
        service.configure_mock(**{
            'create_person_service.return_value': (person_mock, 201)
        })

        with mock.patch('api.controller.request') as request_mock:
            request_mock.return_value = request = mock.Mock()
            request.get_json.return_value = {}

            response = create_person(service)

            self.assertIsInstance(cls=Response, obj=response)
            self.assertEqual(201, response.status_code)
            self.assertEqual({'id': str(id), 'name': 'jane', 'birth_date': None}, loads(response.data))
