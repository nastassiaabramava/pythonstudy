import re
from sys import stdin

search = input().lower().strip()
found = False
for filename in stdin:
    filename = filename.strip()
    try:
        with open(filename, encoding='utf-8') as file_in:
            text = file_in.read().lower()
            final_text = re.sub(r'\s+', ' ', text).strip()
            if search in final_text:
                print(filename)
                found = True
    except FileNotFoundError:
        continue
if not found:
    print('404. Not Found')
