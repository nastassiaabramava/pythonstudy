import json

count = 0
positive = 0
spisok = []

in_filename = input()
out_filename = input()

with open(in_filename, encoding='utf-8') as file_in:
    for line in file_in:
        for value in line.split():
            num = int(value)
            spisok.append(num)
            count += 1
            if num > 0:
                positive += 1

num_min = min(spisok)
num_max = max(spisok)
suma = sum(spisok)
aver = suma / count

records = {
    "count": count,
    "positive_count": positive,
    "min": num_min,
    "max": num_max,
    "sum": suma,
    "average": round(aver, 2)
}

with open(out_filename, "w", encoding="utf-8") as file_out:
    json.dump(records, file_out, ensure_ascii=False, indent=4)
