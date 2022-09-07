import math
a = int(input("Input the first leg: "))
b = int(input("Input the second leg: "))
c = math.sqrt(a**2 + b**2)
print("The length of a hypotenuse is: ", c)
print("Finally, we can find a perimeter of a triangle")
p = a + b + c
print("The perimeter is: ", p)
