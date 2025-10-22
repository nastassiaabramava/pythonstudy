from math import log, cos, sin, pi, e
x = float(input())
a = log(x ** (3 / 16), 32)
b = x ** cos((pi * x) / (2 * e))
c = sin(x / pi) ** 2
print(a + b - c)