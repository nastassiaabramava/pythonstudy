n = int(input())

with open("public.txt", encoding='utf-8') as file_in:
    text = file_in.read()
result = []
for symbol in text:
    if 'A' <= symbol <= 'Z':
        code = chr((ord(symbol) - ord('A') + n) % 26 + ord('A'))
        result.append(code)
    elif 'a' <= symbol <= 'z':
        code = chr((ord(symbol) - ord('a') + n) % 26 + ord('a'))
        result.append(code)
    else:
        result.append(symbol)
with open('private.txt', 'w', encoding='utf-8') as file_out:
    file_out.write(''.join(result))
