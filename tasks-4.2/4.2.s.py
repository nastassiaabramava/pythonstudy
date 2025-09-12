from itertools import cycle


def secret_replace(text, **kwargs):
    result = {}    # словарь для итератора-цикла
    for key, value in (kwargs.items()):
        if isinstance(value, (tuple, list)):    # сделали итератор-цикл из значений
            result[key] = cycle(value)    # и добавили в словарь итераторов
        else:
            result[key] = cycle((value,))    # одиночное значение
    out = []
    for letter in text:
        out.append(next(result[letter]) if letter in result else letter)
    # в out добавляем букву из циела, если она есть в словаре, иное - букву из ориг.текста
    return ''.join(out)