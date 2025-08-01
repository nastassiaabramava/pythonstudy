spisok = []
n = int(input())

for i in range(n):
    s = input().replace(',', '').split()
    spisok.extend(s)
for index, value in enumerate(sorted(spisok), 1):
    print(f'{index}. {value}')
