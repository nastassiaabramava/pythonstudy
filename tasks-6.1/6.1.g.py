import numpy as np


def make_board(n):
    board = np.zeros((n, n), dtype=np.int8)
    board[::2, ::2] = 1    #1 в каждых четных столбцах и строках, начиная с 0
    board[1::2, 1::2] = 1    #1 в каждых нечетных столбцах и строках, начиная с 1
    return board