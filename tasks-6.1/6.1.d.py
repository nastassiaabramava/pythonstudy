import math

spisok = list(map(float, input().split()))
mnozh = math.prod(spisok)
nums = len(spisok)

x = (math.pow(mnozh, (1 / nums)))
print(x)