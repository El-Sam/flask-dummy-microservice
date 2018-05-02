from typing import Optional


class Person(object):
    id = None
    name = None
    birth_date = None

    def __init__(self, id: str, name: str, birth_date: Optional):
        self.id = id
        self.name = name
        self.birth_date = birth_date
