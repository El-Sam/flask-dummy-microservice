import flask
import logging
from flask_injector import FlaskInjector
from injector import Injector

from .controller import blueprint
from model.models import db
from application import ServiceModule, FactoryModule
from application.resource.encoders import FlaskCustomJSONEncoder
from application.exceptions.exceptions import ClientException
from infrastructure import PersonRepositoryModule


def init_app(config):
    app = flask.Flask(__name__)

    app.config.from_object(config)

    app.json_encoder = FlaskCustomJSONEncoder

    db.init_app(app)

    if not app.testing:
        logging.basicConfig(level=logging.INFO)

    app.register_blueprint(blueprint=blueprint, url_prefix='/')

    # Sentry - only for production

    # Todo uncomment this if you have a sentry DSN
    # if not app.debug and not app.testing and 'SENTRY_DSN' in app.config:
    #     from raven.contrib.flask import Sentry
    #     Sentry(app)

    @app.errorhandler(ClientException)
    def handle_client_errors(error):
        response = flask.jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    with app.app_context():
        db.create_all()

        my_injector = Injector([
            ServiceModule,
            FactoryModule,
            PersonRepositoryModule
        ])

        FlaskInjector(app=app, injector=my_injector)

    # No configuration after injection

    return app
