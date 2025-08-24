def get_repeater(func, count):    # аргументы: некая функция (лямбда) и число (кол-во раз)
    def new_func(x):    # создаем новую функцию, в котрой описываем func
        for i in range(count):    # для каждого числа в диапазоне х-count
            x = func(x)    # применяем функцию к х
        return x    # new_func возвращает нам число
    return new_func    # get_repeater возвращает функцию new_func