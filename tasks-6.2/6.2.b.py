import pandas as pd
import re


def length_stats(words):
    words = sorted(set(re.findall(r'[A-Za-zА-Яа-яЁё]+', words.lower())))
    series = pd.Series((map(len, words)), index=words, dtype='int64')
    even = series[series % 2 == 0]
    odd = series[series % 2 == 1]
    return odd, even