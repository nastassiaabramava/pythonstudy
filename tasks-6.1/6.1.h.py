import numpy as np


def snake(m, n, direction='H'):
    if direction == 'V':
        # order='F' сперва заполняются столбцы
        matrix = np.arange(1, m * n + 1, dtype=np.int16).reshape(n, m, order='F')
        matrix[::, 1::2] = matrix[::-1, 1::2]
    else:
        matrix = np.arange(1, m * n + 1, dtype=np.int16).reshape(n, m)
        matrix[1::2, ::] = matrix[1::2, ::-1]
    return matrix