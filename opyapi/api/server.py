from __future__ import annotations
from . import Annotation
from ..application import Application


class Server(Annotation):
    def __init__(self, id: str, host: str, port: int = 80, description: str = "", variables: list = None):
        self.id = id
        self.variables = variables
        self.description = description
        self.host = host
        self.port = port
        self.url = host + ":" + str(port)

    """
        Base class for all other classes that are used as decorators,
        responsible for binding open api api into user-land classes.
        """

    def __call__(self, target):
        super().__call__(target)
        Application.add_server(target)
