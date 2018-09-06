import os
from api import init_app
from config import config


app = init_app(config=config.get(os.getenv('FLASK_ENV'), 'dev'))

if __name__ == "__main__":
    if os.getenv('FLASK_ENV') == 'prod':
        raise Exception('You\'re trying to run this Flask app in a production environment with \n' +
                        'Flask\'s builtin application server which is not suitable for production.')

    app.run(host='0.0.0.0', port=8080)
