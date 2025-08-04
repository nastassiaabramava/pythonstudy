name = str(input())
shkaf = int(input())
group = shkaf // 100
krovat = (shkaf // 10) % 10
number = shkaf % 10

print(f'Группа №{group}.')
print(f'{number}. {name}.')
print(f'Шкафчик: {shkaf}.')
print(f'Кроватка: {krovat}.')
