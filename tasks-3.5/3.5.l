numbers = input()
even = input()
odd = input()
eq = input()

with open(numbers, encoding="utf-8") as file_in, \
        open(even, "w", encoding="utf-8") as even_out, \
        open(odd, "w", encoding="utf-8") as odd_out, \
        open(eq, "w", encoding="utf-8") as eq_out:
    for line in file_in:
        even_spisok = []
        odd_spisok = []
        eq_spisok = []
        for value in line.strip().split():
            num = str(value)
            even_count = sum(1 for digit in num if int(digit) % 2 == 0)
            odd_count = sum(1 for digit in num if int(digit) % 2 != 0)

            if even_count > odd_count:
                even_spisok.append(num)
            elif odd_count > even_count:
                odd_spisok.append(num)
            else:
                eq_spisok.append(num)
        even_out.write(" ".join(even_spisok) + "\n")
        odd_out.write(" ".join(odd_spisok) + "\n")
        eq_out.write(" ".join(eq_spisok) + "\n")
