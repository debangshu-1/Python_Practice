import math

# Base Class
class Shape:
    def area(self):
        # A generic shape doesn't have an area, so it acts as a placeholder
        raise NotImplementedError("Subclasses must implement the area() method.")

# Subclass 1
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self): # Overriding the parent method
        return math.pi * (self.radius ** 2)

# Subclass 2
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self): # Overriding the parent method
        return self.length * self.width

# Subclass 3
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self): # Overriding the parent method
        return 0.5 * self.base * self.height

# Example Usage:
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

print(f"Circle Area: {circle.area():.2f}")
print(f"Rectangle Area: {rectangle.area()}")
print(f"Triangle Area: {triangle.area()}")