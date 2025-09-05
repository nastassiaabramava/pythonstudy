def merge_sort(args=None):
    if args is None:    # если список пуст, то это и есть ответ
        return args
    if len(args) == 1:    # если в списке 1 цифра, то это и есть ответ
        return args

    mid = len(args) // 2    # делим входной список на 2 части
    left = merge_sort(args[:mid])    # левая часть от начала до середины
    right = merge_sort(args[mid:])    # правая часть от середины до конца
    result = []    # список для сортировки
    i = j = 0    # переменные для сравнения
    while i < len(left) and j < len(right):    # сравниваем и добавляем в список
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # добавляем все, что осталось, если половинки были разными по количеству цифр
    result.extend(left[i:])
    result.extend(right[j:])
    return result