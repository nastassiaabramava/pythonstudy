s = input()
s1 = s.split()
spisok = []
slov = {}


for i in s1:
    s2 = i.rstrip(';')
    numb = int(s2)
    spisok.append(numb)    # может и не надо
    slov[numb] = []
for key in slov:
    prost = []
    for num in spisok:
        a, b = int(key), int(num)
        while b != 0:
            a, b = b, a % b
        if a == 1:
            prost.append(num)
        
    slov[key] = prost
dict1 = dict(sorted(slov.items()))

for key, value in dict1.items():
    if value:
        m = sorted(set(value))
        print(f"{key} - {', '.join(str(x) for x in m)}")
