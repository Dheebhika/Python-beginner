class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius


r = int(input("Enter the radius: "))
object = Circle(r)
print(object.area())
print(object.perimeter())
