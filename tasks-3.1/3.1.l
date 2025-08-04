n = int(input())

s = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']

for i in range(n):
    print(s[i])
    if len(s) < n:
        s = s * n
