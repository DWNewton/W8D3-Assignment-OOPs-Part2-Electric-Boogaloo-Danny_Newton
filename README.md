# W8D3 - Assignment: OOPs - Part2
OOP Assignment to demo inheritance and polymorphism
## Shape Class Hierarchy
The Shape class hierarchy is an exploration into the world of colorful and geometric wonders. Each shape is not only colorful but also comes with its unique set of characteristics and a penchant for calculation.
# Base Class: Shape
## Attributes:
- color (string): The color of the shape.
## Methods:
- __init__(self, color): Initializes the shape with the given color.
- calculate_area(self): Abstract method to calculate the area of the shape.
- calculate_perimeter(self): Abstract method to calculate the perimeter of the shape.
- get_color(self): Retrieves the color of the shape.
- set_color(self, color): Sets the color of the shape.
# Derived Classes:
## Circle
### Attributes:
- radius (float): The radius of the circle.
### Methods:
- __init__(self, color, radius): Initializes the circle with the given color and radius.
- calculate_area(self): Calculates the area of the circle (πr²).
- calculate_perimeter(self): Calculates the perimeter (circumference) of the circle (2πr).
## Rectangle
### Attributes:
- length (float): The length of the rectangle.
- width (float): The width of the rectangle.
### Methods:
- __init__(self, color, length, width): Initializes the rectangle with the given color, length, and width.
- calculate_area(self): Calculates the area of the rectangle (length * width).
- calculate_perimeter(self): Calculates the perimeter of the rectangle (2 * (length + width)).
## Triangle
### Attributes:
- side1 (float): The length of the first side of the triangle.
- side2 (float): The length of the second side of the triangle.
- side3 (float): The length of the third side of the triangle.
### Methods:
- __init__(self, color, side1, side2, side3): Initializes the triangle with the given color and side lengths.
- calculate_area(self): Calculates the area of the triangle using Heron's formula.
- calculate_perimeter(self): Calculates the perimeter of the triangle (side1 + side2 + side3).

# Instructions
## Run the Program:
- Save the TotallySafeShapes.py file from GitHub.
- Open a terminal or command prompt.
- Navigate to the directory where the file is saved.
- Run the program using the command: __python TotallySafeShapes.py__

# Interacting with the Shape Objects:
- The program creates instances of different shapes (circle, rectangle, triangle) with specific dimensions and colors.
- It uses polymorphism to store the shape objects in a list.
- It iterates over the list of shapes and invokes the calculate_area() and calculate_perimeter() methods for each shape. The area, perimeter, and color of each shape are displayed.

## Dive into the wonderful world of shapes, where geometry meets a splash of color. Enjoy your stay and may your shapes ever be vibrant!
###### (Sorry, had to lighten up the assignment a little...)