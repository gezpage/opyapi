from __future__ import annotations
import re
from ..exceptions import ValidationError
from .validator import Validator

# https://www.w3.org/TR/html5/forms.html#valid-e-mail-address
_EMAIL_REGEX = re.compile(
    r"^[a-z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?(?:\.[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?)*",
    re.I
)


class Email(Validator):
    def validate(self, value):

        if not _EMAIL_REGEX.match(value):
            raise ValidationError(f"Passed value {value} is not valid email address.")
        return value
