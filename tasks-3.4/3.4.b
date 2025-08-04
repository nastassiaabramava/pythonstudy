s = input().replace(",", "").split()
s1 = input().replace(",", "").split()

for a, b in zip(s, s1):
    print(f'{a} - {b}')
