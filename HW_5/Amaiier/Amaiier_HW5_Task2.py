print ("1-rectangle, 2-triangle, 3-circle")
figure = input ('Choose a figure:')

if figure == '1':
    print ("The sides of the rectangle:")
    a = float (input("a = "))
    b = float (input("b = "))
    print ("Square rectangle:", a*b)

elif figure == '2':
    print ("The side and high of the triangle:")
    a = float (input("a = "))
    h = float (input("h = "))
    print ("Square of the triangle:", (a/2)*h)

elif figure == '3':
    r = float (input("Radius of the circle: "))
    pi=3.14
    #from math import pi
    print ("Square of the circle:", (pi*r**2))

else:
    print ("Wrong choice")
