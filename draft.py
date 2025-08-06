def fragments(numbers):
    if not numbers:
        return []
    spisok1 = [numbers[0]]
    general_spisok = []

    for i in range(1, len(numbers)):
        if numbers[i] >= numbers[i - 1]:
            spisok1.append(numbers[i])
        else:
            general_spisok.append(spisok1)
            spisok1 = [numbers[i]]
    general_spisok.append(spisok1)
    return general_spisok

result = fragments([])
print(result)





