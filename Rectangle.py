# Luke Reissmueller
# CECS 229 - Programming Assignment 1
# 9/18/2020

# Rectangle Class
class Rectangle:
    def __init__(self, width = 1, height = 1):  # Rectangle Constructor
        self._width = width
        self._height = height

    def getHeight(self):  # Returns height of rectangle
        return self._height

    def getWidth(self):  # Returns width of rectangle
        return self._width

    def getArea(rect):  # Returns product of height and width of rectangle
        return rect.getHeight() * rect.getWidth()

    def getPerimeter(rect):  # Returns sum of sides of rectangle
        return rect.getHeight() * 2 + rect.getWidth() * 2
