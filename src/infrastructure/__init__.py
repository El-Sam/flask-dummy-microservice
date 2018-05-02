from injector import Module
from .persistence.repositories import PersonRepository


class PersonRepositoryModule(Module):
    def configure(self, binder):
        binder.bind(PersonRepository)
