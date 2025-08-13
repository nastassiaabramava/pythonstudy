def table(values):
    scheme = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    result = ''

    for num, symbol in scheme:
        while values >= num:    # для чисел > 2k
            if values >= num:
                result += symbol    # если загаданное число больше, то добавляем данный символ
                values -= num    # отнимаем num, т.к. мы его использовали
    return result


def roman(number1, number2):
    num1 = table(number1)
    num2 = table(number2)
    num3 = table(number1 + number2)
    answer = f'{num1} + {num2} = {num3}'
    return answer