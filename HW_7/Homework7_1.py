class Polygon:
    def __init__(self, sides):
        self.x = sides
        self.sides = [0 for i in range(sides)]

    def inputside(self):
        self.sides = [float(input("Enter sides "+str(i+1)+" : ")) for i in range(self.x)]

    def dispside(self):
        for i in range(self.x):
            print("Side", i + 1, "is", self.sides[i])


class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 2)

    def squ(self):
        a, b = self.sides
        return a*b


t = Rectangle()
t.inputside()
print(f"Square of the rectangle = {t.squ()}")
