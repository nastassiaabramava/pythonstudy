from sys import stdin

students = [i.split() for i in stdin]

d_students = {}
for i in students:
    name = i[0]
    d_students[name] = [i[1]]
    d_students[name].append(i[2])

result = 0
for values in d_students.values():
    x = int(values[1]) - int(values[0])
    result += x / len(d_students)
print(round(result))
