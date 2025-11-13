import re
from itertools import product

expr = input().strip()

# находим переменные (заглавные буквы), сортируем по алфавиту
vars_ = sorted(set(re.findall(r'[A-Z]', expr)))

# шапка, * для распаковки варс
print(*vars_, 'F')

# все комбинации значений переменных
for bits in product([0, 1], repeat=len(vars_)):
    # с этого момента я ничего не понимаю
    env = {v: bool(b) for v, b in zip(vars_, bits)}
    val = eval(expr, {}, env)
    print(*bits, int(bool(val)))