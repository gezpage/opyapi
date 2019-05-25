from __future__ import annotations
from . import Annotation
from enum import Enum


class OperationMethod(Enum):
    GET = "get"
    POST = "post"
    PUT = "put"
    PATCH = "patch"
    DELETE = "delete"
    OPTIONS = "options"
    HEAD = "head"

    def __str__(self):
        return self.value


class Operation(Annotation):
    """
    .. _Open Api Operation: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md#operationObject
    """
    def __init__(
        self,
        route: str,
        method=None,
        summary: str = "",
        description: str = "",
        responses=None,
        request=None,
        tags: list = None,
    ):
        print("init")
