from api import init_app
from config import config_prod

app = init_app(config=config_prod)

# used for production, and served by WSGI server
if __name__ == "__main__":
    app.run()
