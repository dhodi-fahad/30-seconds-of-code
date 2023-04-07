class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


v1 = Vector(1, 2)
v2 = Vector(3, 4)

v3 = v1 + v2

print(v3.x)
print(v3.y)


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __str__(self):
        return f"Rectangle of Length: {self.length} and Width: {self.width}"

    def __eq__(self, other):
        return True if self.area() == other.area() else False

    def __lt__(self, other):
        return True if self.area() < other.area() else False


r1 = Rectangle(10, 5)
r2 = Rectangle(5, 10)
print(r1 == r2)
print(r1 < r2)

rect1 = Rectangle(4, 5)
rect2 = Rectangle(2, 10)

print(rect1 == rect2)  # False
print(rect1 < rect2)  # True
