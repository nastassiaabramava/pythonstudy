import pandas as pd


def need_to_work_better(journal):
    columns = ['maths', 'physics', 'computer science']
    return journal.loc[(journal[columns] == 2).any(axis=1)]