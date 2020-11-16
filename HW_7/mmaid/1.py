class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 2)

    def squ(self):
        a, b = self.sides
        return a*b

t = Rectangle()
t.inputSides()
print(f"Squareof the rectangle = {t.squ()}")


