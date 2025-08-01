name = str(input())
p = int(input())
w = int(input())
m = int(input())
fp = p * w
x = m - w * p
print('Чек')
print(f'{name} - {w}кг - {p}руб/кг')
print(f'Итого: {fp}руб')
print(f'Внесено: {m}руб')
print(f'Сдача: {x}руб')
