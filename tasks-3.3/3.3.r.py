{key: [value for value in range(1, key + 1) if key % value == 0] for key in sorted(numbers)}
