# Luke Reissmueller
# CECS 229 - Programming Assignment 1
# 9/18/2020

# Rectangle Tester

from Rectangle import Rectangle  # import Rectangle class from Rectangle file

def testRect(rect):  # Rectangle tester method, prints width, height, area, perimeter
    print("Width:" , rect.getWidth() , "| Height:" , rect.getHeight())  # --each time it is called.
    print("Area:" , rect.getArea() , "| Perimeter:" , rect.getPerimeter())

r1 = Rectangle(4,40)  # Construct 2 rectangles with unique height and widths
r2 = Rectangle(3.5,35.9)
testRect(r1)  # Pass rectangles through tester function
testRect(r2)