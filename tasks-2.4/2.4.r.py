n = int(input())
num = 1
flag = False

for i in range(1, n + 1):
    # создаем строку, чтобы узнать количество символов в последней
    line = ''
    for j in range(1, i + 1):
        line += str(num)
        # если не последний символ в строке и вообще не последний, то добавляем пробел
        if j < i and num < n:
            line += ' '
        num += 1
        if num > n:
            flag = True
            break
    # ширина последней сроки, по которой будем центрировать
    width = len(line)
    if flag:
        break

num = 1
flag = False
# повторяем все тоже самое и печатаем уже с известной шириной для центрирования
for i in range(1, n + 1):
    line = ''
    for j in range(1, i + 1):
        line += str(num)
        if j < i and num < n:
            line += ' '
        num += 1
        if num > n:
            flag = True
            break
    print(f'{line:^{width}}')
    if flag:
        break
