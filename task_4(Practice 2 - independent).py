import math
x = int(input("What area do you want to calculate? Rectangle, triangle, or circle(1,2,3 - respectively)"))
if(x == 1):
    a = int(input("Input the value of the first side: "))
    b = int(input("Input the value of the second side: "))
    s = a * b
    print("The area of a rectangle is: ", s)
elif(x == 2):
    a = int(input("Length of 1 side: "))
    b = int(input("Length of 2 side: "))
    c = int(input("Length of 3 side: "))
    p = a + b + c
    s = sqrt(p*(p-a)*(p-b)*(p-c))
    print("The area of a triangle is: ", s)
elif(x == 3):
    r = int(input("Input the value of radius: "))
    s = (2 * math.pi * r)
    print("The area of a circle is: ", s)
else:
    print("Wrong Number! Error!")
