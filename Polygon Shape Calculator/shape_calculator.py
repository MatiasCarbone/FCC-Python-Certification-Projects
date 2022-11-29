import math


class Rectangle:
    width = 0
    height = 0

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def __str__(self):
        return "Rectangle(width=%d, height=%d)" % (self.width, self.height)

    def set_width(self, x):
        self.width = x

    def set_height(self, x):
        self.height = x

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width**2 + self.height**2) ** 0.5
        return diagonal

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        text = ""

        for i in range(self.height):
            text = text + "*" * self.width + "\n"

        return text

    def get_amount_inside(self, x):
        obj = x
        timesWidth = self.width / obj.width
        timesHeigth = self.height / obj.height

        if timesWidth < 1 or timesHeigth < 1:
            return 0
        else:
            timesInside = math.floor(timesWidth) * math.floor(timesHeigth)
            return timesInside

        print("TW %d | TH %d" % (timesWidth, timesHeigth))
        return


class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return "Square(side=%d)" % (self.width)

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, x):
        self.width = x
        self.height = x

    def set_height(self, x):
        self.height = x
        self.width = x