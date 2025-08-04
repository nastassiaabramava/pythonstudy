a = int(input())
b = int(input())
c = int(input())
fda = a // 10
lda = a % 10
fdb = b // 10
ldb = b % 10
fdc = c // 10
ldc = c % 10

if fda == fdb == fdc:
    print(fda)
elif lda == ldb == ldc:
    print(lda)
