def sq_tri():
    h = int(input("Input H = "))
    base = int(input("Input base = "))
    return print(h*base/2)
def sq_res():
    w = int(input("Input w = "))
    h = int(input("Input h = "))
    return print(w*h)
def sq_cir():
    r = int(input("Input r = "))
    PI = 3.14
    return print(PI*r**2)

sel = input("Select: 1 - triangle, 2 - rectangle, 3 - circle ")
if sel == "1":
    sq_tri()
elif sel == "2":
    sq_res()
else:
    sq_cir()