def merge(set1, set2):
    spisok1 = list(set1)
    spisok2 = list(set2)
    spisok1.extend(spisok2)
    return tuple(sorted(spisok1))