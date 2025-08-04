with open('numbers.num', encoding='utf-8') as file_in:
    numbers = file_in.read()
number_list = [num for line in numbers for num in line.split()]
sum_number = 0
for num in number_list:
    number = int(num, 16)
    sum_number += number
print(sum_number % 65536)