line = input().split()
numbers = []

for i in line:
    if i in '+-*':
        # как только появляется оператор - удаляем предыдущие две цифры из списка
        a = numbers.pop()
        b = numbers.pop()
        # и проводим с ними операцию в зависимости от оператора
        if i == '+':
            numbers.append(a + b)
        elif i == '-':
            numbers.append(b - a)
        elif i == '*':
            numbers.append(a * b)
    else:
        numbers.append(int(i))
print(numbers[0])