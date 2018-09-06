from flask.json import JSONEncoder
from .resources import Resource


class FlaskCustomJSONEncoder(JSONEncoder):
    def default(self, obj) -> dict:
        if isinstance(obj, Resource):
            return obj.to_json()
        return super().default(obj)
