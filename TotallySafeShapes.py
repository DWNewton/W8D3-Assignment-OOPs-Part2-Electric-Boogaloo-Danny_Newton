import math

class Shape:
    def __init__(self, color):
        # Initialize the shape with the given color (colors make everything better)
        self.color = color

    def calculate_area(self):
        raise NotImplementedError("This method is overridden by subclasses. Or maybe it got lost in space.")

    def calculate_perimeter(self):
        raise NotImplementedError("This method is overridden by subclasses. Or maybe it's just hiding.")

    def get_color(self):
        # Get the color of the shape (in case we forget what color it was)
        return self.color

    def set_color(self, color):
        # Sets the color of the shape (changing colors is a thing now)
        self.color = color


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def calculate_area(self):
        # Calculate the area of the circle (πr² - it's math, not magic)
        return math.pi * (self.radius ** 2)

    def calculate_perimeter(self):
        # Calculate the perimeter (circumference) of the circle (2πr - math is fun)
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def calculate_area(self):
        # Calculate the area of the rectangle (length * width - like arranging tiles)
        return self.length * self.width

    def calculate_perimeter(self):
        # Calculate the perimeter of the rectangle (2 * (length + width) - because who doesn't love brackets)
        return 2 * (self.length + self.width)


class Triangle(Shape):
    def __init__(self, color, side1, side2, side3):
        super().__init__(color)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        # Had to go to https://www.britannica.com/science/Herons-formula to figure this one out.
        # Calculate the area of the triangle using Heron's formula (it's a bit of a mouthful, but it's cool)
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def calculate_perimeter(self):
        # Calculate the perimeter of the triangle (side1 + side2 + side3 - just add them up)
        return self.side1 + self.side2 + self.side3


if __name__ == "__main__":
    # Create some colorful shapes with highly precise dimensions
    shapes = [
        Circle("Red", 42),
        Rectangle("Blue", 23, 19),
        Triangle("Green", 15, 20, 25)
    ]

    # Iterate over the list of shapes and show off their amazing attributes
    for shape in shapes:
        shape_type = type(shape).__name__.lower()
        print(f"A {shape.get_color()} {shape_type}:")
        print(f" - Area: {shape.calculate_area():.2f}")
        print(f" - Perimeter: {shape.calculate_perimeter():.2f}")
        print()  # Just a line break to keep things tidy