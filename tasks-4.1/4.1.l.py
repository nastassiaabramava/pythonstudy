from itertools import product


def find_mountains(data):
    n = len(data)   # количество списков
    m = len(data[0])   # количество цифр в списке
    result = []
    # индексы кроме первого и последнего (не участвуют)
    # создаем новую ячейку i, j
    for i, j in product(range(1, n - 1), range(1, m - 1)):
        # создаем комбинации координат k, t вокруг ячейки i, j, включая ее саму
        # если координаты k, t равны или меньше i, j, то условие true
        # тогда добавляем в список (+1 потому что краевые скипаем)
        if all((k == i and t == j) or data[i][j] > data[k][t] for k, t in
               product(range(i - 1, i + 2), range(j - 1, j + 2))):
            result.append((i + 1, j + 1))
    return tuple(result)