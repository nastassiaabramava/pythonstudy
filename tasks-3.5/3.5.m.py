import json
from sys import stdin
filename = input()

with open(filename, encoding='utf-8') as file_in:
    records = json.load(file_in)
for line in stdin:
    if '==' in line:
        key, value = line.strip().split('==')
        records[key.strip()] = value.strip()
with open(filename, 'w', encoding='utf-8') as file_out:
    json.dump(records, file_out, ensure_ascii=False, indent=4)
