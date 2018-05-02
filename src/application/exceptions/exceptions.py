class ClientException(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        super().__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


class NotFoundException(ClientException):
    def __init__(self, code=404, payload=None):
        message = 'Not found.'
        super().__init__(message, code, payload)


class MissingPropertyException(ClientException):
    def __init__(self, property_name, code=400, payload=None):
        message = '{} is missing'.format(property_name)
        super().__init__(message, code, payload)
