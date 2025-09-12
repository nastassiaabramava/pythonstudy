def gcd(*numbers):
    a = numbers[0]
    if len(numbers) == 1:
        return numbers[0]
    else:
        for b in numbers:
            while b != 0:
                a, b = b, a % b
            b = a
        return b