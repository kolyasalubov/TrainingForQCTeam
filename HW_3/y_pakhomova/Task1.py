#Homework

number = int(input("Enter number: "))
factorial = 1

if number < 0:
    print("Factorial doesn't exist for negative numbers!")

for x in range(1, number + 1):
    factorial = factorial * x

print(f"({number}!) = {factorial}")

