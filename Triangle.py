class Triangle:
    def __init__(self, b, p, h):
        self.b = b
        self.p = p
        self.h = h

    def area(self):
        return (self.b * self.h)/2

    def perimeter(self):
        return self.b + self.p + self.h


t = Triangle(3,4,5)

print("Area: ", t.area())
print("Perimeter: ", t.perimeter())

        
