def choice(*args, **kwargs):
    (key, f), = kwargs.items()    # распаковка в ключ-значение, запятая в конце означает "ожидаю ровно 1 элемент"
    if key == 'min':
        g = min
    else:
        g = max
    return g(map(f, args))