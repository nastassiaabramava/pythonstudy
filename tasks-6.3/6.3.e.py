from requests import get
import sys

# первое значение из распаковки уходит в адрес, остальное в path
address, *path = map(str.strip, sys.stdin)
# сделали список списков из того, что получили
result = [get(f'http://{address}{path_}').json() for path_ in path]
total = sum(sum(numbers) for numbers in result)
print(total)