import re


class MyAwesomeError(Exception):
    pass


class CyrillicError(MyAwesomeError):
    pass


class CapitalError(MyAwesomeError):
    pass


def name_validation(name):
    if not isinstance(name, str):
        raise TypeError
    # из списка всех кириллич.символов делаем строку
    cyrill = ''.join(re.findall(r'\b[А-Яа-яЁё]+\b', name))
    if len(cyrill) != len(name):
        raise CyrillicError
    capitalized_name = name.capitalize()
    if name != capitalized_name:
        raise CapitalError
    return name