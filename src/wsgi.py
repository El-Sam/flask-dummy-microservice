from api import init_app
from config import config

# used for production, and served by WSGI server
app = init_app(config=config.get('FLASK_ENV', 'prod'))
