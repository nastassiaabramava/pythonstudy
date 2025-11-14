class Programmer:
    positions = {'Junior': 10, 'Middle': 15, 'Senior': 20}

    # final time, чтобы складывать отработанное время
    def __init__(self, name, position, salary=0, final_time=0):
        self.name = name
        self.position = position
        self.salary = salary
        self.final_time = final_time

    def work(self, time=0):
        self.time = time
        # зп = текущая зп * отработанное время
        self.salary = self.salary + Programmer.positions[self.position] * self.time
        # прибавляем новое отработанное время к общему времени
        self.final_time += self.time

    def rise(self):
        if self.position == 'Junior':
            self.position = 'Middle'
        elif self.position == 'Middle':
            self.position = 'Senior'
        else:
            self.position = 'Senior'
            self.salary += self.time * 1    # сеньор получает +1 тг\час за повышение

    def info(self):
        return f'{self.name} {self.final_time}ч. {self.salary}тгр.'