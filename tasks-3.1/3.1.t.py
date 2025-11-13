line = input().split()
numbers = []
operators_bin = '+-*/'
operators_un = '~!#'
operators_ten = '@'

for i in line:
    if i in operators_bin:
        a = numbers.pop()
        b = numbers.pop()
        if i == '+':
            numbers.append(a + b)
        elif i == '-':
            numbers.append(b - a)
        elif i == '*':
            numbers.append(a * b)
        elif i == '/':
            numbers.append(b // a)
    elif i in operators_un:
        if i == '~':
            numbers.append(-numbers.pop())
        elif i == '!':  # факториал
            x = numbers.pop()
            res = 1
            for i in range(2, x + 1):  # 0! и 1! = 1
                res *= i
            numbers.append(res)
        elif i == '#':    # клонируем последнее число
            numbers.append(numbers[-1])
    elif i in operators_ten:    # меняем порядок значений
        if i == '@':
            c = numbers.pop()
            b = numbers.pop()
            a = numbers.pop()
            numbers.extend([b, c, a])
    else:
        numbers.append(int(i))
print(numbers[-1])
