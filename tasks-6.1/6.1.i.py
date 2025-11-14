import numpy as np


def rotate(matrix, angle):
    if angle == 90:
        matrix = matrix.transpose()[::, ::-1]
    if angle == 180:
        matrix = matrix[::-1, ::-1]
    if angle == 270:
        matrix = matrix.transpose()[::-1, ::]
    else:
        return matrix
    return matrix