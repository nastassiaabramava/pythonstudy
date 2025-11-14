import numpy as np


def multiplication_matrix(n):
    numbers = np.arange(1, n + 1)
    matrix = np.outer(numbers, numbers)
    return matrix