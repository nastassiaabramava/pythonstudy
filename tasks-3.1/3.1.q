s = input()
s = s.lower()
a = list(s)
k = []

for letter in a:
    if letter != ' ':
        k.append(letter)
    else:
        continue
if k[0:] == k[::-1]:
    print('YES')
else:
    print('NO')
