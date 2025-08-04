n = input()
spisok = n.split()
a = []

  
for k in spisok:
    num_int = int(k)
    numbers = {"digits": 0, "units": 0, "zeros": 0}
    while num_int != 0:
        dnum = num_int % 2
        num_int = num_int // 2
        numbers["digits"] += 1
        if dnum == 1:
            numbers["units"] += 1
        if dnum == 0:
            numbers["zeros"] += 1
    a.append(numbers)    
print(a)
