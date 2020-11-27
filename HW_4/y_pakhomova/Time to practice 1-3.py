# Task 1

for x in range(100):
    if x%2 == 0:
        print(x)

index = 0
while index < 100:
    if index%2 == 0:
        print(index)
    index = index + 1

# Task 2

for x in range(100):
    if x%2 == 0:
        continue
    print(x)

for x in range(100):
    if x%2 != 0:
        print(x)

# Task 3
list = [4, 6, 3, 8]
for x in list:
    if x%2 != 0:
        print("List contains odd numbers")
        break

