s1 = set(input())
s2 = set(input())
s3 = s1 & s2

for letter in s3:
    print(letter, end='')
