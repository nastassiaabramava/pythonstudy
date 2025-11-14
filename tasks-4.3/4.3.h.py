def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a    # берем текущее значение а и обновляем его
        a, b = b, a + b