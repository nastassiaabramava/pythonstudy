from itertools import product

val = list(product([2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз'], ['пик', 'треф', 'бубен', 'червей']))
s = input()
for i in val:
    if i[1] != s:
        print(i[0], i[1])
    else:
        continue
