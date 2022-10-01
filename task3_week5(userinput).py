class Calculator():
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
a = int(input("Input first number: "))
b = int(input("Input second number: "))
obj = Calculator(a, b)
choice = 1
print("0. Exit")
print("1. Add")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Enter choice: "))
if choice == 1:
    print("Result: ", obj.add())
elif choice == 2:
    print("Result: ", obj.subtract())
elif choice == 3:
    print("Result: ", obj.multiply())
elif choice == 4:
    print("Result: ", round(obj.divide(), 2))
elif choice == 0:
    print("See you next time!")
else:
    print("Error! Choose from given numbers!")