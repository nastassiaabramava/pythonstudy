n = int(input())
best_base = 2    # стартовое основание
max_sum = 0

# проверяем все основания от 2 до 10
for base in range(2, 11):
    num = n
    total = 0

    # считаем сумму в данном основании
    while num > 0:
        total += num % base
        num //= base

    # если сумма больше максимума — это новый максимум
    # соответственно, это основание - самое выгодное
    if total > max_sum:
        max_sum = total
        best_base = base

print(best_base)