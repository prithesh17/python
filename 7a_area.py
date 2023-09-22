import math

class Shape:
    def __init__(self):
        self.area = 0
        self.name = ""

    def show_area(self):
        print("The area of the", self.name, "is", self.area, "units")

class Circle(Shape):
    def __init__(self, radius):
        self.name = "Circle"
        self.radius = radius

    def calculate_area(self):
        self.area = math.pi * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.name = "Rectangle"
        self.length = length
        self.width = width

    def calculate_area(self):
        self.area = self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.name = "Triangle"
        self.base = base
        self.height = height

    def calculate_area(self):
        self.area = (self.base * self.height) / 2

radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)
circle.calculate_area()
circle.show_area()

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
rectangle = Rectangle(length, width)
rectangle.calculate_area()
rectangle.show_area()

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
triangle = Triangle(base, height)
triangle.calculate_area()
triangle.show_area()
