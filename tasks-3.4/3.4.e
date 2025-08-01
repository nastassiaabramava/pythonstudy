spisok = []

for i in range(3):
    s = input().replace(',', '').split()
    spisok.extend(s)
for index, value in enumerate(sorted(spisok), 1):
    print(f'{index}. {value}')
