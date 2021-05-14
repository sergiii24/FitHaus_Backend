from django.core.exceptions import ValidationError


def correct_pwd(value):
    if any(char.isupper() for char in value) and any(char.islower() for char in value) and any(
            char.isnumeric() for char in value) and any(not char.isalpha() for char in value):
        return value
    else:
        raise ValidationError("Password must have at least  1 uppercase letter, 1 lowercase letter, "
                              "1 number and 1 non alpha-numeric symbol")
