#Task_1
print("\nTask 1")
list = []
n = int(input("Enter list length: "))
for i in range(n):
    elem = int(input("Enter element: "))
    list.append(elem)
reverse = list[::-1]
print("Reversed array: ", reverse)

#Task_2
print("\nTask 2")
def change(list):
    index1 = 0
    index2 = len(list)-1
    list[0],list[len(list)-1] = list[len(list)-1],list[0]
    print(list)
arr = []
el = int(input("How many elements? "))
for i in range(0,el):
    ele = int(input("Element: "))
    arr.append(ele)
print("Swapping last and first elements: ")
change(arr)

#Task_3
print("\nTask 3")
def to_list(*par):
    return list(par)
print("Molik", 'Malika', 1, -109, 56, "Milk", "Coconut", "Nutella")

#Task_4
print("\nTask 4")
def useless(s):
    n = len(s)
    return max(s)/n
print('The "useless" number is: ', useless([14, 34, -8]))

#Task_5
print("\nTask 5")
def lstsort(list):
    list.sort(key = lambda l: abs(l), reverse = True)
    return list
print("Sorted by their absolute values: ", lstsort([23, 3.5, 62, 13.1, -99, 77, -108.7]))

#Task_6
print("\nTask 6")
def all_eq(ls):
    max_el = max(ls, key = lambda l: len(l))
    m_len = len(max_el)
    return [elem.ljust(m_len, "_") for elem in ls]
print("Result:\n", all_eq(["Molik", "Baklazhan", "Melon", "Bird", "Leonardo Da Vinci"]))
    

    
