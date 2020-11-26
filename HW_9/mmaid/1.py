def age_type(a):
    try:
        a = float(a)
        if a >= 0:
            return print("Even" if a%2 == 0 else "odd")
        else:
            return print("Error, age should be more than 0")
    except:
        return print("Error, input is incorrect.")


age = input("Enter your age: ")
age_type(age)
