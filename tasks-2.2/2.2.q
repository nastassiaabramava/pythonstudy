a = float(input())
b = float(input())
c = float(input())
d = b ** 2 - 4 * a * c

if a == b == c == 0:
    print('Infinite solutions')
elif a == 0 and b != 0 and c != 0:
    x4 = - c / b
    print(f'{x4:.2f}')
elif d < 0 or a == b == 0 and c != 0:
    print('No solution')

elif d == 0:
    x = -b / (2 * a)
    print(f'{x:.2f}')

elif d > 0:
    x1 = (- b - d ** 0.5) / (2 * a)
    x2 = (- b + d ** 0.5) / (2 * a)
    if x1 < x2:
        print(f'{x1:.2f} {x2:.2f}')
    else:
        print(f'{x2:.2f} {x1:.2f}')
