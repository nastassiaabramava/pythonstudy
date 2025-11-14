import math

deka = list(map(float, input().split()))
pola = list(map(float, input().split()))
deka_x = deka[0]
deka_y = deka[1]
p = pola[0]
f = pola[1]
# переводим точки в декартово расстояние по формуле
pola_x = p * math.cos(f)
pola_y = p * math.sin(f)

distance = math.dist((deka_x, deka_y), (pola_x, pola_y))
print(distance)