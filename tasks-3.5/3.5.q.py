with open('secret.txt', encoding='utf-8') as file_in:
    code = file_in.read()

result = []
for symbol in code:
    number = ord(symbol)
    if number > 127:
        code = chr(number % 256)
        result.append(code)
    else:
        result.append(chr(number))
print(''.join(result))
