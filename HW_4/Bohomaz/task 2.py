r = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(r)):
    if r[i] % 2 == 0:
        print("even numbers that are divisible by 2", r[i])
for i in range(len(r)):
    if r[i] % 3 == 0 and r[i] % 2 == 1:
        print("odd numbers, which are divisible by 3", r[i])
for i in range(len(r)):
    if r[i] % 3 == 1 and r[i] % 2 == 1:
        print("numbers that are not divisible by 2 and 3", r[i])
        