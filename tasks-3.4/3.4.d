from itertools import accumulate

s = input().split()
d = [i + ' ' for i in s]

for value in accumulate(d):
    print(value)
