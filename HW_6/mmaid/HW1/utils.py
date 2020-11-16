from math import pi as PI
from math import pow


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
    return print(PI*pow(r, 2))

def us_sel(sel):
    """Main logic of programm, arg -> str"""
    if sel == "1":
        sq_tri()
    elif sel == "2":
        sq_res()
    else:
        sq_cir()
