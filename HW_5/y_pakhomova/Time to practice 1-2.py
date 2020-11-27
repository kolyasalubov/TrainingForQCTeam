#Time to practice 1

input_string = input("Enter a list elements separated by space: ")
numbers = input_string.split()

min = int(numbers[0])
max = int(numbers[0])

for x in numbers:
    if int(x) > max:
        max = int(x)
    elif int(x) < min:
        min = int(x)

print(f"Max number: {max} Min number: {min}")

#Time to practice 2

for x in range(1, 11):
    if x%2 == 0:
        print(f"{x} is even number")
    elif x%2 != 0 and x%3 == 0:
        print(f"{x} is odd number divisible by 3")
    else:
        print(f"{x} is not divisible by 2 or 3")

