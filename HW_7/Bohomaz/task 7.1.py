def square_rectangle():
    height = float(input("Enter height:"))
    width =  float(input("Enter width:"))
    return input(height*width)

def square_circle():
    PI =3.14
    radius = float(input("Enter radius"))
    return input(PI*radius**2)


def square_triangle():
    height = float(input("Enter height:"))
    base = float(input("Enter base:"))
    return input(height*base)

def square():
    choise_user = float(input("Enter the number: \
   1 - square_rectangl, 2 - square_circle, 3 - square_triangle "))
    if choise_user == 1:
        square_rectangle()
    elif choise_user == 2:
        square_circle()
    elif choise_user ==3:
        square_triangle()
    else:
        return "Please tipe: 1 or 2 or 3"

print (square())
 