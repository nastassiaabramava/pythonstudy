from datetime import datetime
DB = []    # общая бд, гед будут все юзеры


def insert(*info):    # добавляем юзеров в бд
    DB.extend(info)
# словарь операторов, где значения - лямбда-функции, чтобы юзать их в дальнейшем


opers = {
    '==': lambda a, b: a == b,
    '!=': lambda a, b: a != b,
    '>': lambda a, b: a > b,
    '<': lambda a, b: a < b,
    '>=': lambda a, b: a >= b,
    '<=': lambda a, b: a <= b,
}


# т.к. значение value приходит строкой, то делаем функцию для замены типа на нужный (кроме имени)
def types(parameter, value):
    if parameter == 'id':
        return int(value)
    if parameter == 'birth':
        return datetime.strptime(value, '%d.%m.%Y')
    else:
        return value


# если нет условий, то возвращаем всех
def select(parameters=None):
    if not parameters:
        # отсортированный по возростанию ид
        # через лямбду берем значение ид (цифру)
        return sorted(DB, key=lambda u: u['id'])

    # на входе будет параметр-оператор-значение
    parameter, oper, value = parameters.split()
    # к параметру и значению применили функцию types, чтобы привести value к нужному типу
    compare = types(parameter, value)
    # у каждого оператора - своя лмбда функция
    op_func = opers[oper]

    result = []
    for user in DB:
        if parameter == 'id':
            x = int(user['id'])    # если параметр id, то берем его значение
        elif parameter == 'birth':    # если параметр birth, то берем его значение
            x = datetime.strptime(user['birth'], '%d.%m.%Y')    # и приводим к нужному формату
        else:
            x = user['name']
        # применяем лямбду нужного оператора для значения параметра в нужном типе и value в нужном типе
        if op_func(x, compare):
            result.append(user)
    return sorted(result, key=lambda u: u['id'])