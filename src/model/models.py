from sqlalchemy_utils import UUIDType
from flask_sqlalchemy import SQLAlchemy
import uuid

from typing import Optional

db = SQLAlchemy()


class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True
    id = db.Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)


class Person(BaseModel):
    __tablename__ = 'persons'

    name = db.Column(db.Unicode, unique=True)
    birth_date = db.Column(db.Date)

    def __init__(self, name: str, birth_date: Optional = None):
        self.name = name
        self.birth_date = birth_date
