def get_operator(operator):
    if operator == '+':
        return lambda a, b: a + b
    elif operator == '-':
        return lambda a, b: a - b
    elif operator == '*':
        return lambda a, b: a * b
    elif operator == '//':
        return lambda a, b: a // b
    elif operator == '**':
        return lambda a, b: a ** b