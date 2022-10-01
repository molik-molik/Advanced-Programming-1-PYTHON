#Class constructor
import math
class Rectangle:
    def __init__(self, color="green", width=100, height=100):
        self.color = color
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perim(self): #I have added perim() method, which calculates the perimeter
        return (self.width+self.height)*2
    def diagonal_length(self):
         return math.sqrt(self.width**2 + self.height**2)
rect1 = Rectangle()
print(rect1.color)
print(rect1.area())
rect1 = Rectangle("yellow", 23, 34)
print(rect1.color)
print(rect1.area())
print(rect1.perim())
print(rect1.diagonal_length())
rect1 = Rectangle("light blue", 44, 14)
