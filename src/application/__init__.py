from injector import Module
from .factory import Factory
from .service import Service


class FactoryModule(Module):
    def configure(self, binder):
        binder.bind(Factory)


class ServiceModule(Module):
    def configure(self, binder):
        binder.bind(Service)
