import math
import re

##Tasks fo independent work - Week 1

print("Task 1")

#Task_1
name = input("What are your last and first names? ")
age = input("How old are you? ")
num = input("What's your phone number? ")
print("Your name: ", name)
print("Your age: ", age)
print("Your phone number: ", num)

print("\nTask 2")

#Task_2
def calc_area(a):
    if a==1:
        a = int(input("Fisrt side: "))
        b = int(input("Second side: "))
        s = a*b
        print(s)
    elif a==2:
        a = int(input("Length of 1 side: "))
        b = int(input("Length of 2 side: "))
        c = int(input("Length of 3 side: "))
        p = a + b + c
        s = math.sqrt(p*(p-a)*(p-b)*(p-c))
        print("The area of a triangle is: ", s)
    elif a==3:
        r = int(input("Input the value of radius: "))
        s = (2 * math.pi * r)
        print("The area of a circle is: ", s)
    else: print("No offers for this number.")
a = int(input("What area do you want to calculate?\nRectangle(1), triangle(2), circle(3). "))
calc_area(a)

print("\nTask 3")

#Task_3
my_num = float(input("Enter the floating number: "))
result = math.modf(my_num)
print("Split the decimal and integer parts: ", result) 
dec, integer = result
new_dec = integer/100
new_int = dec*100
result = new_dec + new_int
print("And exchange them. Now we have a new number:", result)

print("\nTask 4")

#Task_4
a = int(input(("Enter the value of A: ")))
y = (a**2)/3 + (a**2 + 4)/6 + math.sqrt(a**2 + 4)/4 + math.sqrt((a**2 + 4)**3)/4
print("The answer is: ", y)

print("\nTask 5")

#Task_5
m = int(input("Multiply the planned number by 5.\nAdd 8 to it.\nMultiply the sum by 2.\nLet's see what we got!"))
answ1 = ((m / 2) - 8)/5
print("The computer guessed the number you intended! It is: ", answ1)

print("\n2 - Tasks for variables and cycles.")
print("\nTask 2.1")

#Task_2.1 - Smart Calculator
x = int(input("First number: "))
z = input("Choose the kind of calculation: ")
y = int(input("Second number: "))
if (z=="sum" or z=="+" or z=="addition"):
    a = x + y
    print(a)
if (z=="subtraction" or z=="-"):
    s = x - y
    print(s)
if (z=="*" or z=="multiplication"):
    m = x*y
    print(m)
if (z=="/" or z=="division"):
    d = x/y
    print(d)
if (z=="%" or z=="quotient"):
    q = x%y
    print(q)

print("\nTask 2.2")

#Task_2.2 - Checking for zero
x = int(input("First number: "))
z = input("Choose the kind of calculation: ")
y = int(input("Second number: "))
if (z=="sum" or z=="+" or z=="addition"):
    a = x + y
    print(a)
if (z=="subtraction" or z=="-"):
    s = x - y
    print(s)
if (z=="*" or z=="multiplication"):
    m = x*y
    print(m)
if (z=="/" or z=="division"):
    if y!=0:
        d = x/y
        print(d)
    if y==0:
        print("Can't divide by zero")
if (z=="%" or z=="quotient"):
    q = x%y
    print(q)

print("\nTask 2.3")

#Task_2.3
var = 14
def check(n):
    if n>10 and n!=12 and n>=15 or n==18:
        return True
    else:
        return False
print(check(var))

print("\nTask 2.4")

#Task_2.4
n = 34
while n < 67:
    if n % 2 != 1:
        print(n)
        n += 2

print("\nTask 2.5")

#Task_2.5
password = "molik"
count = 0
while True:
    word = input("Input the password: ").lower()
    count = count + 1
    if word == password:
        print("Right!")
        break
    if word != password and count > 7:
        print("Wrong! Try again next time!")
        break


print("\nTask 2.6")

#Task_2.6
i = 0
while (i<100):
    i += 1
    if i==50: continue
    if i==99: continue
    print(i)
    
print("\nAnother solution, with for loop: ")
num = list(range(1,101))
for n in num:
    if n==50: continue
    if n==99: continue 
    print(n)

print("\nTask 2.7")

#Task_2.7
import re
word = input("Enter any word: ")
repeat = int(input("Enter how many times each letter will repeat: "))
for c in word:
    result = re.sub('(.)', r'\1' * repeat, c)
    print(result)
#Last task does work in IDLE
