import math


def s_triangle ():
    a = float(input('Enter a:  '))
    b = float(input('Enter b:  '))
    c = float(input('Enter c:  '))
    p = (a + b + c) / 2
    s = math.sqrt(((p - a)*(p - b)*(p - c)) * p)
    print(f'Result is {s}')
    return s


def s_rectangle():
    a = float(input('Enter a:  '))
    b = float(input('Enter b:  '))
    s = a * b
    print(f'Result is {s}')
    return s


def s_circle():
    r = float(input('Enter radius:  '))
    s = math.pi * (r ** 2)
    print(f'Result is {s}')
    return s


def trs():
    choice = int(input('Select one: \n1. S for triangle \n2. S for rectangle \n3. S for circle \nEnter your choice:  '))
    if choice == 1:
        return s_triangle()
    elif choice == 2:
        return s_rectangle()
    else:
        return s_circle()
trs()
