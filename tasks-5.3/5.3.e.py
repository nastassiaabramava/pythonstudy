def merge(set1, set2):
    try:
        iter(set1)
        iter(set2)
    except TypeError:
        raise StopIteration
    # сделали из кортежей множества по типу
    a = set(map(type, set1))
    b = set(map(type, set2))
    # объединили полученные множества, у неоднородных будет >1
    homo = a | b
    if len(homo) > 1:
        raise TypeError
    sort_1 = sorted(list(set1))
    sort_2 = sorted(list(set2))
    # сравнили отсортированные с тем, что изначально было
    if list(set1) != sort_1 or list(set2) != sort_2:
        raise ValueError
    i = 0
    j = 0
    result = []
    while i < len(set1) and j < len(set2):    # чтобы не было out of range
        if set1[i] < set2[j]:
            result.append(set1[i])
            i += 1
        else:
            result.append(set2[j])
            j += 1
    # добавляем оставшиеся элементы, т.к. добавили только меньшие
    result.extend(set1[i:])
    result.extend(set2[j:])
    return tuple(result)