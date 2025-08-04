objects = dict()

while (s := input()) != "":
    k = s.split()
    for i in k:
        if i not in objects:
            objects[i] = 1
        else:
            objects[i] = objects[i] + 1
for j in objects:
    print(j, objects[j])
