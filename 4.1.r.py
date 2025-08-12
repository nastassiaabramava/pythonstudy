def merge(set1, set2):
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