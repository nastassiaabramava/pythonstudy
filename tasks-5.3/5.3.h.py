import re


class MyAwesomeError(Exception):
    pass


class BadCharacterError(MyAwesomeError):
    pass


class StartWithDigitError(MyAwesomeError):
    pass


def username_validation(username):
    if not isinstance(username, str):
        raise TypeError

    if not re.fullmatch(r'[A-Za-z0-9_]+', username):
        raise BadCharacterError()
    if username[0].isdigit():
        raise StartWithDigitError()
    return username