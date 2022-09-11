#Exersise_1
price = int(input("Input the price for 1 kg of sweets: "))
final_price = 0
kg = int(input("How many kilograms of sweets do you want to buy?\n"))
for i in range(0, kg):
    final_price += price
print("Total price for sweets: ", final_price)

print("\n\n")

#Exersise_2
s = 0
counter = 1
n = int(input("Input a sequence of integers ending in zero:\n"))
while n!=0:
    s += n
    n = int(input())
    counter += 1
print("Sum of numbers: ", s)
print("The number of all numbers: ", counter)
    



