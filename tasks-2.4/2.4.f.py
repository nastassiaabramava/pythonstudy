n = int(input())
a = int(input()) 
 
for i in range(n - 1): 
    b = int(input()) 
    while a != 0 and b != 0: 
        if a > b: 
            a = a % b 
        elif b > a: 
            b = b % a
        elif a == b:
            break 
    if a == b:
        a = b
    else:
        a = a + b  
print(a)
