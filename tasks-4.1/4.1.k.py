def find_mountains(heights):
    data = heights
    mountains = []
    # индекс тройки; тройка цифр и индексы этих цифр;
    # 2 - начинаем с цифры с индексом 2, т.к. она будет центральной в первой тройке
    # не начинаем с индекса 1, потому что в условии нельзя брать крайние цифры
    for index, (left, middle, right) in enumerate(zip(data, data[1:], data[2:]), 2):
        if left < middle > right:
            mountains.append(index)
    return tuple(mountains)