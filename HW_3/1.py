# import math
# n = int(input("Enter any number: "))
# fact = math.factorial(n)
# print("The factorial of", n, "is", fact) 

# Variant without import 
n = int(input("Enter any number: "))

fact = 1
while n > 1:
    fact *= n
    n -= 1

print("factorial is ", fact)
