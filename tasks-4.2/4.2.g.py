def to_string(*data, sep=' ', end=''):
    return sep.join(str(value) for value in data) + end

def get_formatter(sep=' ', end=''):
    return lambda *data: to_string(*data, sep=sep, end=end)