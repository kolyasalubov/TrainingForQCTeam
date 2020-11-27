import math


def age_type(a):
    try:
        a = int(a)
        math.pow(a, 0.5)
        if a > 0:
            print("Your age is Even" if a % 2 == 0 else "Your age is Odd")
        else:
            print("Error!! Really? Zero? ")
    except ValueError:
        print("Error!! Incorrect input.")


age = input("Your age, please: ")
age_type(age)