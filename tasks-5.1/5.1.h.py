class Checkers:

    def __init__(self):
        # словарь рядов и столбцов
        self.cells = {'P': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'], 'Q': [1, 2, 3, 4, 5, 6, 7, 8]}
        # словарь позиций шашек
        self.board = {}
        # списки для удобства
        column = self.cells['P']
        row = self.cells['Q']

        for r in row:
            for c in column:
                # берем индексы столбцов, начиная с 1
                ci = column.index(c) + 1
                # равенство для четных\нечетных
                equal = (r % 2) == (ci % 2)
                # если шашка на рядах для "черных" и в равенстве, то стейт - блэк
                if r in (8, 7, 6) and equal:
                    state = 'B'
                # если шашка на рядах для "белых" и в равенстве, то стейт - уайт
                elif r in (1, 2, 3) and equal:
                    state = 'W'
                # все остальные - пустые
                else:
                    state = 'X'
                # добавляем координаты в словарь
                self.board[c + str(r)] = Cell(state)

    def move(self, f, t):
        # определяем текущее положение шашки с помощью метода статус
        new_state = self.board[f].status()
        # очищаем клетку иначе будет typeError
        self.board[f].state = 'X'
        # присваиваем новое значение
        self.board[t].state = new_state

    def get_cell(self, p):
        return self.board[p]


class Cell:
    def __init__(self, state):
        self.state = state

    def status(self):
        return self.state