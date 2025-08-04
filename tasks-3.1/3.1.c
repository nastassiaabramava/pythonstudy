L = int(input())
n = int(input())

for i in range(n):
    text = str(input())
    if len(text) > L:
        print(f'{text[0: L - 3]}...')
    else:
        print(text)
