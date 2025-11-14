import pandas as pd


def update(journal):
    columns = ['maths', 'physics', 'computer science']
    journal = journal.assign(average=lambda df: df[columns].mean(axis=1))
    return journal.sort_values(by=['average', 'name'], ascending=[False, True])