def maxNumber(num1, num2):
    """returns the largest number of two numbers """
    if num1 >= num2: 
        return num1
    else: 
        return num2
num1 = input("tipe digit")
num2 = input("tipe digit")
print(maxNumber(num1, num2))         
