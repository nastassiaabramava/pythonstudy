def same_type(func):
    def wrapper(*args, **kwargs):
        # мэп берет тип каждого аргумента, кладет его во множество
        # множ-во съедает все одинаковые
        # поэтому, если > 1, то значит там разные типы есть
        if len(set(map(type, args))) > 1:
            print('Обнаружены различные типы данных')
            return None
        return func(*args, **kwargs)
    return wrapper