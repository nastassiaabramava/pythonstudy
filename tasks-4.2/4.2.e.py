def to_string(*data, sep=' ', end='\n'):
    return sep.join(str(value) for value in data) + end