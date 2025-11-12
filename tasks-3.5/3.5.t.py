with open('numbers.num', 'rb') as f:
    data = f.read()

total = 0

# идём по 2 байта: [hi][lo]
for i in range(0, len(data), 2):
    hi = data[i]
    lo = data[i + 1]
    value = hi * 256 + lo

    # сумма в 2-байтном диапазоне
    total = (total + value) % 65536

print(total)