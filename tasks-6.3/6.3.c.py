from requests import get


address = input()
response = get(f'http://{address}/')
# если элемент в джейсоне - число, то он в списке
numbers = [x for x in response.json() if isinstance(x, int)]

print(sum(numbers))