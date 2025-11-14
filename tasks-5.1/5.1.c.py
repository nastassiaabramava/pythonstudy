class RedButton:
    def __init__(self, counter: int = 0):   # создаем счетчик
        self.counter = counter

    def click(self):    # считаем клики
        self.counter += 1
        print('Тревога!')

    def count(self):    # возвращаем кол-во кликов
        return self.counter