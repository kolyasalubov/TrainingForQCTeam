from math import sqrt

def solve_quadric_equation(a, b, c):
    try:
        x1 = complex((-b + sqrt(b** + 4*a*c))/(2*a))
        x2 = complex((-b - sqrt(b** + 4*a*c))/(2*a))
        return f"The solution are x1={x1} and x2={x2}"
    except ZeroDivisionError:
        return  "Zero Division Error"
    except TypeError:
        return "Could not convert string to float"

