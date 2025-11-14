import pandas as pd
import re


def length_stats(words):
    words = sorted(set(re.findall(r'[A-Za-zА-Яа-яЁё]+', words.lower())))
    return pd.Series((map(len, words)), index=words, dtype='int64')