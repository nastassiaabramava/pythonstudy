p = int(input())
v = int(input())
t = int(input())
if t < v < p:
    print('1. Петя', '2. Вася', '3. Толя', sep='\n')
elif v < p < t:
    print('1. Толя', '2. Петя', '3. Вася', sep='\n')
elif p < t < v:
    print('1. Вася', '2. Толя', '3. Петя', sep='\n')
elif v < t < p:
    print('1. Петя', '2. Толя', '3. Вася', sep='\n')
elif p < v < t:
    print('1. Толя', '2. Вася', '3. Петя', sep='\n')
else:
    print('1. Вася', '2. Петя', '3. Толя', sep='\n')
