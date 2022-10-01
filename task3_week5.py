#Task_3
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num1 - self.num2
    def multiply(self):
        return self.num1 * self.num2
    def divide(self):
        return self.num1 / self.num2
obj01 = Calculator(30,10)
obj02 = Calculator(49, 7)
print("Object 1: ")
print(obj01.add())
print(obj01.subtract())
print(obj01.multiply())
print(obj01.divide())
print("Object 2: ")
print(obj02.add())
print(obj02.subtract())
print(obj02.multiply())
print(obj02.divide())