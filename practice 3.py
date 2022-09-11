x = int(input("Input first number: "))
y = int(input("Input second number: "))
z = int(input("Input third number: "))
if x<y and x<z:
    print("Minimum is: ", x)
if y<x and y<z:
    print("Minimum is: ", y)
if z<x and z<y:
    print("Minimum is: ", z)


