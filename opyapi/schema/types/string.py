from __future__ import annotations

from .type import Type
from ..validators import DateTime


class String(Type):

    accept_types = str
    reject_types = bool
    type = "string"

    def __init__(
        self,
        format: str = None,
        min_length: int = None,
        max_length: int = None,
        pattern: str = None
    ):
        super().__init__()
        if format is not None:
            self.format = format

        if min_length is not None:
            self.min_length = min_length

        if max_length is not None:
            self.max_length = max_length

        if pattern is not None:
            self.pattern = pattern

        self._apply_format()

    def _apply_format(self):
        if self.format == "datetime":
            self.extra_validators.append(DateTime())

    def to_doc(self):
        doc = self._get_base_doc()

        if self.min_length is not None:
            doc["minLength"] = self.min_length

        if self.max_length is not None:
            doc["maxLength"] = self.max_length

        if self.pattern is not None:
            doc["pattern"] = self.pattern

        if self["format"] is not None:
            doc["format"] = self.format

        return doc
