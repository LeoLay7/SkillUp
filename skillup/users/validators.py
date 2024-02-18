import re
import django.core.exceptions


def school_class_validator(value):
    pattern = "'^[1-9]|1[0-1][А-Я]"

    if not re.match(pattern, value):
        raise django.core.exceptions.ValidationError(
            message="Введенное значение не является классом"
        )
