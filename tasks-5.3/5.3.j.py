import re
import hashlib


class MyAwesomeError(Exception):
    pass


class BadCharacterError(MyAwesomeError):
    pass


class StartsWithDigitError(MyAwesomeError):
    pass


class CyrillicError(MyAwesomeError):
    pass


class CapitalError(MyAwesomeError):
    pass


class MinLengthError(MyAwesomeError):
    pass


class PossibleCharError(MyAwesomeError):
    pass


class NeedCharError(MyAwesomeError):
    pass


def name_validation(name):
    if not isinstance(name, str):
        raise TypeError
    cyrill = ''.join(re.findall(r'\b[А-Яа-яЁё]+\b', name))
    if len(cyrill) != len(name):
        raise CyrillicError
    capitalized_name = name.capitalize()
    if name != capitalized_name:
        raise CapitalError
    return name


def username_validation(username):
    if not isinstance(username, str):
        raise TypeError

    if not re.fullmatch(r'[A-Za-z0-9_]+', username):
        raise BadCharacterError()
    if username[0].isdigit():
        raise StartsWithDigitError()
    return username


def user_validation(**kwargs):
    if set(kwargs) != {'last_name', 'first_name', 'username'}:
        raise KeyError
    for i in kwargs:
        if not isinstance(kwargs[i], str):
            raise TypeError

    last = name_validation(kwargs['last_name'])
    first = name_validation(kwargs['first_name'])
    user = username_validation(kwargs['username'])

    return {'last_name': last, 'first_name': first, 'username': user}


def password_validation(password, min_length=8,
                        possible_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789',
                        at_least_one=str.isdigit):
    if not isinstance(password, str):
        raise TypeError
    if len(password) < min_length:
        raise MinLengthError
    if any(char not in possible_chars for char in password):
        raise PossibleCharError
    if not any(at_least_one(char) for char in password):
        raise NeedCharError
    # хэш пароля
    result = hashlib.sha256(password.encode('utf-8')).hexdigest()

    return result

print(password_validation("Hello12345"))

