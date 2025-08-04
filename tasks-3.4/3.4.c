from itertools import count
n = input().split()

for value in count(float(n[0]), float(n[2])):
    if value <= float(n[1]):
        print(format(value, '.2f'))
    else:
        break
