import pandas as pd


def best(journal):
    columns = ['maths', 'physics', 'computer science']
    return journal.loc[(journal[columns] > 3).all(axis=1)]