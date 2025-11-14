def result_accumulator(func):
    result = []

    def wrapper(*args, **kwargs):
        nonlocal result  # nonlocal видит на 1 уровень выше
        value = func(*args)  # вызвали функцию из примера
        result.append(value)  # результат добавили в список
        if kwargs.get('method') == 'drop':
            ans = result  # т.к. список будем очищать, то сделали его копию
            result = []  # список очистили
            return ans  # копию вернули

    return wrapper