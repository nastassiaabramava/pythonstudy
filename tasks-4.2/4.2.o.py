def get_repeater(func, count):
    def new_func(x, **kwargs):
        y = x
        for _ in range(count):
            y = func(y, **kwargs)
        return y
    return new_func
