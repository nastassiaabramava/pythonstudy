n = int(input())
checker = set()
result = set()
sum = 0

for i in range(n):
    s = input()
    if s in checker:
        sum += 1
        result.add(s)
    else:
        checker.add(s)     
x = sum + len(result)        
print(x)
