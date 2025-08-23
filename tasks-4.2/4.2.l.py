first = []
second = []


def enter_results(*args):
    parameters = list(args)
    first_group = parameters[::2]
    second_group = parameters[1::2]
    first.extend(first_group)
    second.extend(second_group)


def get_sum():
    suma1 = round(sum(first), 2) if first else 0.0
    suma2 = round(sum(second), 2) if second else 0.0
    return suma1, suma2


def get_average():
    avr1 = sum(first) / len(first) if first else 0.0
    avr2 = sum(second) / len(second) if second else 0.0
    return avr1, avr2