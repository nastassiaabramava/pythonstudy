import re


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
    # если множество ключей не равно, что просят
    if set(kwargs) != {'last_name', 'first_name', 'username'}:
        raise KeyError
    # если каждое значение - не строка
    for i in kwargs:
        if not isinstance(kwargs[i], str):
            raise TypeError
    # всех в валидатор
    last = name_validation(kwargs['last_name'])
    first = name_validation(kwargs['first_name'])
    user = username_validation(kwargs['username'])

    return {'last_name': last, 'first_name': first, 'username': user}