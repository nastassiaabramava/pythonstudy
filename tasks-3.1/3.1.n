s = input()
p = int(input())
s = s.split()
spisok = []

for letter in s:
    x = int(letter) ** p
    print(x, end=' ')
