import sys
import math

for row in sys.stdin:
    res = math.gcd(*map(int, row.split()))
    print(res)