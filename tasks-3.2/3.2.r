n = int(input())
spisok_par = {}

for i in range(n):
    s = input().split()
    spisok_par[i] = s    # создаем список всех перечисленных пар

for i in spisok_par:
    new_spisok = []
    for j in spisok_par[i]:
        fd = (int(j) // 10)
        new_spisok.append(fd)    # создаем список первых цифр всех чисел
           
    spisok_par[i] = new_spisok    # присваиваем новое значение по ключам из первых цифр    

counts = {}
for i in spisok_par:
    key = tuple(spisok_par[i])  # превращаем список в кортеж, чтобы использовать как ключ
    counts[key] = counts.get(key, 0) + 1

print(max(counts.values()))
