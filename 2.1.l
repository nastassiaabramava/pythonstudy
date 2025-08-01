n = int(input())
m = int(input())
a1 = n // 100
b1 = (n // 10) % 10
c1 = n % 10

a2 = m // 100
b2 = (m // 10) % 10
c2 = m % 10

sum_3 = (c1 + c2) % 10
sum_2 = (b1 + b2) % 10
sum_1 = (a1 + a2) % 10

print(sum_1, sum_2, sum_3, sep='')
