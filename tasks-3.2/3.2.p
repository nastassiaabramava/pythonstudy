area = set()

while (s := input()) != '':
    spisok = s.split()
    for i in range(len(spisok)):
        if spisok[i] == 'зайка':
            if i > 0:
                area.add(spisok[i - 1])
            if i < len(spisok) - 1:
                area.add(spisok[i + 1])
       
for i in area:
    print(i)
