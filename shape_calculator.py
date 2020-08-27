# Scientific Computing with Python Projects - Polygon Area Calculator
# https://www.linkedin.com/in/vasilis-timoudas
# https://github.com/vasilistimoudas

class Rectangle:

    # Initialize width and height
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Returns an instance of a Rectangle as a string
    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    # Sets width
    def set_width(self, width):
        self.width = width

    # Sets height
    def set_height(self, height):
        self.height = height

    # Returns area
    def get_area(self):
        return  self.width * self.height

    # Returns perimeter
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    # Returns diagonal
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    # Returns a string that represents the shape using lines of "*" and
    # if the width or height is larger than 50 returns "Too big for picture."
    def get_picture(self):
        picture = "Too big for picture."
        if self.width < 50 and self.height < 50:
            draw_width = "*" * self.width
            picture = (draw_width + "\n") * self.height
        return picture

    # Returns the number of times the passed in shape could fit inside the shape
    def get_amount_inside(self, rectangle):
        if self.width < rectangle.width or self.height < rectangle.height:
            return 0
        width_mul = int(self.width / rectangle.width)
        height_mul = int(self.height / rectangle.height)
        return width_mul * height_mul

# Subclass of Rectangle
class Square(Rectangle):

    # # Initialize sides
    def __init__(self, side):
        super().__init__(side, side)

    # Returns an instance of a Square as a string
    def __repr__(self):
        return f"Square(side={self.width})"

    # Sets sides
    def set_side(self, side):
        self.width = side
        self.height = side

    # Sets sides
    def set_width(self, side):
        self.set_side(side)

    # Sets sides
    def set_height(self, side):
        self.set_side(side)