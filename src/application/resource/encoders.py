from flask.json import JSONEncoder
from .resources import Person


class FlaskCustomJSONEncoder(JSONEncoder):
    def default(self, obj) -> dict:
        if isinstance(obj, Person):
            return {
                'id': obj.id,
                'name': obj.name,
                'birth_date': obj.birth_date,
            }
        return super().default(obj)
