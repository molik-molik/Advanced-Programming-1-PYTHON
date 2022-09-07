import math
print("Let's find the solutions for a quadratic equation!")
a = int(input("Input the value of a: "))
b = int(input("Input the value of b: "))
c = int(input("Input the value of c: "))
d = b**2 - 4*a*c;
if(d > 0):
    x1 = (-1*b) + math.sqrt(d)
    x2 = (-1*b) - math.sqrt(d)
    print("There are two real roots.", x1, x2)
elif(d == 0):
    x = (-1*b) / 2*a
    print("There is one real solution: ", x)
    
else:
    print("There no real roots!")
    
