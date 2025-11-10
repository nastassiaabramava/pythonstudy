import pandas as pd
import numpy as np


def values(func, start, end, step):
    xnums = np.arange(start, end + step, step)
    ynums = func(xnums)
    return pd.Series(ynums, index=xnums)


def min_extremum(data):
    return data.idxmin()


def max_extremum(data):
    return data.idxmax()