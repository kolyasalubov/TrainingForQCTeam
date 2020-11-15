a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Even numbers that are divisible by 2:")
for i in range(len(a)):
    if a[i] % 2 == 0:
        print(a[i])
print("Odd numbers, which are divisible by 3:")
for i in range(len(a)):
    if a[i] % 3 == 0 and a[i] % 2 == 1:
        print(a[i])
print("Numbers that are not divisible by 2 and 3:")
for i in range(len(a)):
    if a[i] % 3 == 1 and a[i] % 2 == 1:
        print(a[i])
