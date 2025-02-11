from __future__ import annotations
import re
from ..exceptions import ValidationError
from .validator import Validator

_HOSTNAME_REGEX = re.compile(
    r"^[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?(?:\.[a-z0-9](?:[-0-9a-z]{0,61}[0-9a-z])?)*$",
    re.I
)


class Hostname(Validator):
    def validate(self, value):

        if not _HOSTNAME_REGEX.match(value):
            raise ValidationError(f"Passed value {value} is not valid hostname.")
        return value
