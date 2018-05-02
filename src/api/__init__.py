import flask
import logging
from flask_injector import FlaskInjector
from injector import Injector
from .controller import blueprint
from model.models import db
import os
from application import ServiceModule, FactoryModule
from application.resource.encoders import FlaskCustomJSONEncoder
from application.exceptions.exceptions import ClientException
from infrastructure import PersonRepositoryModule


def init_app(config, debug=False, testing=False):
    app = flask.Flask(__name__)

    app.config.from_object(config)

    app.json_encoder = FlaskCustomJSONEncoder

    app.debug = debug
    app.testing = testing

    db_host = os.environ['POSTGRES_HOST']
    db_name = os.environ['POSTGRES_DB']
    db_user = os.environ['POSTGRES_USER']
    db_pass = os.environ['POSTGRES_PASSWORD']
    db_port = os.environ['POSTGRES_PORT']

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port,
                                                                                 db_name)

    db.init_app(app)

    if not app.testing:
        logging.basicConfig(level=logging.INFO)

    app.register_blueprint(blueprint=blueprint, url_prefix='/')

    # Sentry - only for production

    # Todo uncomment this if you have a sentry DSN
    # if not app.debug and not app.testing and 'SENTRY_DSN' in app.config:
    #     from raven.contrib.flask import Sentry
    #     Sentry(app)

    @app.errorhandler(500)
    def server_error(e):
        return """
        An internal error occurred: <pre>{}</pre>
        """.format(e), 500

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

    return app
