n = input()
count = 0
while n != 'Приехали!':
    if 'зайка' in n:
        count += 1
    n = input()
print(count)
