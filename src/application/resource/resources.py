from typing import Optional
from abc import ABC, abstractmethod


class Resource(ABC):
    @abstractmethod
    def to_json(self) -> dict:
        raise NotImplemented('Please implement this method')


class Person(Resource):

    id = None
    name = None
    birth_date = None

    def __init__(self, id: str, name: str, birth_date: Optional):
        self.id = id
        self.name = name
        self.birth_date = birth_date

    def to_json(self) -> dict:
        return dict(id=self.id, name=self.name, birth_date=self.birth_date)
