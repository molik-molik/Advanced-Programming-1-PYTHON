#Task_1
print("Task 1")
import statistics
arr = []
n = int(input("Input the number of elements: "))
for c in range(0, n):
    c = int(input())
    arr.append(c)
reverse = arr[::-1]
print("Max element: ", max(arr))
print("Reversed: ", reverse)
mean = statistics.mean(arr)
for i in range(len(arr)):
    if arr[i]==0:
        arr[i]=mean
print("Arithmetic mean instead of zeros: ", arr, mean)

#Task_2
print("\nTask 2")
arr2 = []
n2 = int(input("Number of elements: "))
for num in range(0, n2):
    num = int(input())
    arr2.append(num)
print("The minimum element is: ", min(arr2))
print("Next part.")
arr_2 = []
arr2_1 = []
for num in arr2:
    if num>0:
        arr_2.append(num)
    if num<=0:
        arr2_1.append(num)
print("Array with only positive elements: ", arr_2)
print("Other elements array: ", arr2_1)

#Task_3
print("\nTask 3")
D = [3, 5, -9, 6, 99, -45, 57, 0]
x=0
for c in D:
    if c%2==0:
        continue
    if c%2!=0:
        x+=c
print(D, "\nThe sum of elements with odd indices: ", x)
for i in range(0, len(D)):
    if D[i]<15:
        D[i]=D[i]*2
print(D)

#Task_4
print("\nTask 4")
intarr = [2, 4, 66, 78, 96, 682, 528]
print("The array: ", intarr)
max_el = max(intarr)
new_arr = []
for i in range(0, len(intarr)):
    if intarr[i]==max_el:
        ind = intarr.index(max_el)
        ind+=1
    if intarr[i]%2==0:
        continue
    if intarr[i]%2!=0:
        new_arr.append(intarr[i])
print("Max element: ", max_el)
print("Its ordinal number: ", ind)
print("Odd numbers subarray: ", new_arr)
if new_arr==[]:
    print("There no any odd numbers!")
intarr.sort()
print("Sorted in descending order: ", intarr)

#Task_5
print("\nTask 5")
def pairs(arr, n):
    array = []
    for i in range(n):
         for j in range(i + 1, n):
            if (abs(arr[i]) == abs(arr[j])):
                array.append(abs(arr[i]))
    if (len(array) == 0):
        return
    for i in range(len(array)):
        print(-array[i], "", array[i], end=" ")
arr5 = [4, 8, 9, -4, 1, -1, -8, 5, 11, 11]
print("The actual array: ", arr5)
n = len(arr5)
pairs(arr5, n)
b = []
for i in arr5:
    if i not in b:
        b.append(i)
print("\n", "Array with no repeating elements: ", b)

#Task_6
print("\nTask 6")
arr6 = [2, 4, 66, 25, 41, 96, 682, 528, 3, 9]
print(arr6)
ma = max(arr6)
mi = min(arr6)
arr6.sort()
counter6=0
sum_of = 0
print("Numbers bigger than minimum number and smaller than maximun: ")
for n in arr6:
    if n>mi and n<ma:
        print(n)
        counter6+=1
    else:
        continue
for c in arr6:
    if c>5:
        sum_of+=c
print("The sum of numbers bigger than 5: ", sum_of)

#Task_7
nn = int(input("Input the number of elements: "))
arr7 = []
sum_e = 0
prod_odd = 1
for i in range(nn):
    print('Input the element: ',i)
    arr7.append(int(input()))
    if arr7[i]%2==0:
        sum_e+=arr7[i]
    if arr7[i]%2!=0:
        prod_odd*=arr7[i]
max_numb = max(arr7)
min_numb = min(arr7)
for i in range(len(arr7)):
    if arr7[i]==max_numb: arr7[i]=min_numb
    elif arr7[i]==min_numb: arr7[i]=max_numb
print('Result: ', arr7)
print("The sum of even elements: ", sum_e, "\nThe product of odd: ", prod_odd)

#Task_8
print("\nTask 8")
arr8 = [1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 0, 2]
print("Array: ", arr8)
sum_a, pr = 0, 1
ar_mean = sum(arr8)/len(arr8)
for a in range(0,len(arr8)):
    pr*=arr8[a]
    sum_a+=arr8[a]
    if arr8[a]==0:
        arr8[a]=ar_mean
print("Zeros to mean: ", arr8)
print("Sum:", sum(arr8), "\nProduct: ", pr)

#Task_9
print("\nTask 9")
arr9 = []
y = int(input("Num of elements: "))
for i in range(0,y):
    ele = int(input("Enter the element number: "))
    arr9.append(ele)
print(arr9)
print('Minimum modulo number:', min(arr9, key = abs))
revers = arr9[::-1]
print("The reversed array: ", revers, "\nNext part.")
arr99 = [3, 12, 30, 20, 6, -15, 23, 45, -9, 7]
arr_9 = [1, 5, 6, 0, 9, -8, 4, 2, -7, 3]
print("Array arr99: ", arr99, "\nArray arr_9: ", arr_9)
arr_9, arr99 = arr99, arr_9
print("Result: \n", "Array arr_9: ", arr_9, "\nArray arr99: ", arr99)

#Task_10
print("\nTask 10")
mylist = []
num = int(input("Number of elements: "))
for i in range(0,num):
    ele = int(input("Element: "))
    mylist.append(ele)
newlist = [] 
replist = []
for i in mylist:
    if i not in newlist:
        newlist.append(i)
    else:
        replist.append(i)
if replist==[]:
    print("No duplicates!")
print("Duplicates: ", replist)
print("Unique Item List: ", newlist)
print("Next part: ")
arr10 = [1, 5, 9, 39, 14, -8, 25, 6, -15, 4, 11, 12, 17, -20, 21]
print("Original: ", arr10)
for i in range(0,len(arr10)):
    if arr10[i]<10:
        arr10[i]=0
    if arr10[i]>20:
        arr10[i]=1
print("Result: values less than 10 are assigned to zero, more than 20 assagned to 1:\n", arr10)


#Task_11
print("\nTask 11")
arr11 = [1, 4, -9, 39, 14, 8, 28, 6, -15, 14, 11, 12, 17, -20, 100, 102, 109]
ar = []
print("Original array: ", arr11)
for c in arr11:
    if c<10:
        ar.append(c)
if ar==[]:
    print("No elements less than 10!")
ar.sort()
print("List of elements less than 10: ", ar)
def max_even(arr):
    even = [x for x in arr if x % 2 == 0]
    odd = [x for x in arr if x % 2 == 1]
    print("Largest even number is: ", max(even))
max_even(arr11)

#Task_12
print("\nTask_12")
arr12 = [2, 4, -9, 41, 14, 8, 23, 6, 18, 12]
arr_12 = [22, -13, 5, 7, -8, 1, 16, 35, 19, 24]
print("Array, from which we will find the smallest odd element: ", arr12)
def min_odd(arr):
    even = [x for x in arr if x % 2 == 0]
    odd = [x for x in arr if x % 2 == 1]
    print("Smallest odd number is: ", min(odd))
min_odd(arr12)
print("Original arrays: arr12\n", arr12, "\narr_12\n", arr_12)
arr12, arr_12 = arr_12, arr12
print("Swapping the arrays: ")
print("Result: arr12\n", arr12, "\narr_12\n", arr_12)

#Task_13
print("\nTask 13")
arr13 = [2, 4, -9, 16, 8, 4, 18, -9]
newlst = [] 
replst = []
print(arr13)
for i in arr13:
    if i not in newlst:
        newlst.append(i)
    else:
        replst.append(i)
        print("Same elements: ", i, "\nFirst appearing indices: ", arr13.index(i))
if replst==[]:
    print("No duplicates!")
for c in range(0,len(arr13)):
    if arr13[c]<15:
        arr13[c]*=2
print("Result: double elements less than 15:\n", arr13)

#Task_14
print("\nTask 14")
ele_num = int(input("Array length:\n"))
arr14 = []
for i in range(0,ele_num):
    arr14.append(int(input("Enter the element: ")))
max_numb=max(arr14)
min_numb=min(arr14)
arr_mean = sum(arr14)/len(arr14)
print("The array: ", arr14, "Arithmetic mean: ", arr_mean)
for i in range(len(arr14)):
    if arr14[i]==max_numb:
        arr14[i]=min_numb
    elif arr14[i]==min_numb:
        arr14[i]=max_numb
print("The array with replaced max and min elements: ", arr14)
for c in range(ele_num):
    if arr14[c]>arr_mean:
        arr14[c]=1
    if arr14[c]==0:
        continue
print("Result: replaced elements greater than arithmetic mean with 1: \n", arr14)


#Task_15
print("\nTask 15")
def arr_odd(arr):
    narr = []
    for c in arr:
        if c%2!=0:
            narr.append(c)
    if narr==[]:
        print("No odd elements!")
    print(narr)
    narr.sort()
    print("Sorted subarray with odd nums: ", narr)
arr15 = [14, 8, -5, 16, 8, 7, 18, 7, -9]
print("Original array: ", arr15)
arr15.sort(reverse = True)
print("Descending ordered array: ", arr15)
print("Subarray with odd elements:")
arr_odd(arr15)
newlst = [] 
replst = []
for i in arr15:
    if i not in newlst:
        newlst.append(i)
    else:
        replst.append(i)
        print("Same elements: ", i, "\nFirst appearing indices: ", arr15.index(i))
if replst==[]:
    print("No duplicates!")






        

    






        


        




