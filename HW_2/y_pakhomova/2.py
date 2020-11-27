##Task 2
##1
number = 1479
sum = 0

for x in str(number):
    sum = sum + int(x)
print(f"Sum: {sum}")

##2
reversed = int(str(number)[::-1])
print(f"Reversed: {reversed}")

##3
list = list(map(int, str(number)))
print(f"Sorted: {sorted(list)}")


