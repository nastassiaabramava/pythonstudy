import json
from sys import stdin

with open('scoring.json', encoding='utf-8') as file_in:
    scoring = json.load(file_in)
input_iter = iter(stdin)    # итератор по строкам ввода
total_score = 0

for group in scoring:
    points = group['points']    # сколько очков за группу 
    tests = group['tests']    # сами тесты в группе
    group_score = 0    # количество правильных ответов
    for test in tests:
        expected = test['pattern'].strip()    # правильный ответ теста
        actual = next(input_iter).strip()    # ввод из стдина
        if expected == actual:
            group_score += 1
    group_points = points * group_score // len(tests)
    total_score += group_points
print(total_score)
