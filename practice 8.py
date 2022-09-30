#Task_1
print("\nTask 1.1")
n = 4
arr = [[1, 2, 3, -6], [5,6,7,0], [9,10,-4,12], [13,14,15,16]]
count = 0
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j]>0:
            count+=1
    print(arr[i])
def sum(arr):
    sum = 0
    for i in range(n):
        for j in range(n):
            if i<j:
                sum = sum + arr[i][j]
    return sum
print("The number of positive numbers is: ", count)
print(arr, "\nThe sum of elements: ", sum(arr))
print("\nTask 1.2")
def find(arr):
    n_rows = len(arr)
    n_col = len(arr[0])
    for i in range(n_rows):
        maxx = 0
        minn = 999999
        for j in range(n_col):
            if arr[i][j] > maxx:
                maxx = arr[i][j]
        print("Maximum in a row: ", maxx)
        for j in range(n_col):
            if arr[i][j] < minn:
                minn = arr[i][j]
        print("Minimum in a row: ", minn)
def swap(l):
    max_value = max(l)
    min_value = min(l)
    idx_min = [i for i,e in enumerate(l) if e==min_value]
    idx_max = [i for i,e in enumerate(l) if e==max_value]
    for idx in idx_min:
        l[idx] = max_value
    for idx in idx_max:
        l[idx] = min_value
    return l
arr = [[0, 7, 0, 1],
       [2, 0, 0, 4],
       [77, 13, 12, 3],
       [1, 4, 8, 45]]
print(arr)
find(arr)
print(swap(arr))

#Task_2
print("\nTask 2.1")
def rows(square, magic_num):
    n = len(square)
    for i in range(n):
        sum_row = 0
        for j in range(n):
            sum_row += square[i][j]
        if sum_row != magic_num:
            return False
    return True
def columns(square, magic_num):
    n = len(square)
    for i in range(n):
        sum_col = 0
        for j in range(n):
            sum_col += square[j][i]
        if sum_col != magic_num:
            return False
    return True
def diagonals(square, magic_num):
    n = len(square)
    sum_diag = 0
    for i in range(n):
        sum_diag += square[i][i]
    if sum_diag != magic_num:
        return False
    sum_diag = 0
    for i in range(n):
        sum_diag += square[i][-(i+1)]
    return sum_diag == magic_num
def magic_square(square):
    magic_constant = 0
    for n in square[0]:
        magic_constant += n
    return ( rows(square, magic_constant) and columns(square, magic_constant) and diagonals(square, magic_constant) )
aray = [[0,2,4,6], 
[6,6,0,1], 
[1,1,5,5], 
[5,3,3,1]]
array = [[1,2,6,-7],
         [3,6,9,12],
         [11,13,17,23],
         [14,7,21,28]]
print(magic_square(aray))
print(array)
print("\nTask 2.2")
def swapp(mat, n, m):
    rows = n
    for i in range(n):
        t = mat[i][0]
        mat[i][0] = mat[i][n-1]
        mat[i][n-1] = t
mat = [[7, 77, 17, 27],
        [71, 57, 47, 37],
        [73, 72, 75, 70],
        [79, 76, 74, 7]]
n = 4
m = 4
swapp(mat, n, m)
for i in range(n):
    for j in range(m):
        print(mat[i][j], end=" ")
    print("\n")


#Task_3
print("\nTask 3.1")
def m_transpose(mat, tr, N):
    for i in range(N):
        for j in range(N):
            tr[i][j] = mat[j][i]
def sym(mat, N):
    tr = [ [0 for j in range(len(mat[0])) ] for i in range(len(mat)) ]
    m_transpose(mat, tr, N)
    for i in range(N):
        for j in range(N):
            if (mat[i][j] != tr[i][j]):
                return False
    return True
a = [ [ 1, 3, 5 ], [ 3, 2, 4 ], [ 5, 4, 1 ] ]
print("Matrix: ", a)
if (sym(a, 3)):
    print("It is symmetric.")
else:
    print("Not symmetric.")
print("\nTask 3.2")
arr = [[23,56,67,78],
       [90,12,15,37],
       [17,9,-45,-14],
       [32,55,77,-67]]
print("Array: ", arr)
print("MAX ELEMENTS FROM EVERY ROW ARE: ", list(map(max,arr)))
print("MAX ELEMENT IS: ", max(map(max, arr)))
print(map(max,arr), arr)
def maxx(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if arr[i][j]==max(map(max, arr)):
                arr[i][j], arr[0][0] = arr[0][0],arr[i][j]
    return arr
print("RESULT BY REARRANGING: ", maxx(arr))


#Task_4
print("\nTask 4.1")
arr = [[23,56,67,78],
       [90,12,15,37],
       [17,9,-45,-14],
       [32,55,77,-67]]
def sum_row(arr):
    r = len(arr)
    c = len(arr[0])
    sum_arr = []
    for i in range(0, r):  
        sumRow = 0;  
        for j in range(0, c): 
            sumRow = sumRow + arr[i][j]
            sum_arr.append(sumRow)
        print("The row: ", arr[i])
        print("Sum of " + str(i+1) +" row: " + str(sumRow))
    print("The maximum row sum: ", max(sum_arr))
    print("The minimum row sum: ", min(sum_arr))    
sum_row(arr)
print("\nTask 4.2")
arr = [[23,-56,67],
       [90,12,37],
       [17,-45,-14]]
def write(arr):
    for c in arr:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i][j] > 0:
                    arr[i][j] = 1
                if arr[i][j] < 0:
                    arr[i][j] = 0
        return arr
def lower(arr):
    l = len(arr)
    for i in range(0, l):
        for j in range(0, l):
            if (i < j):
                print("0", end = " ");
            else:
                print(arr[i][j], end = " " );
        print(" ");
lower(arr)
print("Write 0 instead of negative, 1 instead of positive numbers: ", write(arr))


#Task_5
print("\nTask 5.1")
arr = [[23,-56,67],
       [90,12,37],
       [17,-45,-14]]
l = len(arr)
def sortByRow(arr, n, ascending):
	for i in range(l):
		if (ascending == True):
			arr[i].sort(reverse = True)
		else:
			arr[i].sort()
def transpose(arr, l):
	for i in range(l):
		for j in range(i - 1, l):
			arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
def sortMatRowAndColWise(arr, l):
	sortByRow(arr, l, True)
	transpose(arr, l)
	sortByRow(arr, l, False)
	transpose(arr, l)
print("Original matrix: \n", arr)
sortMatRowAndColWise(arr, l)
print("Sorted rows in ascending order: \n", arr)
print("\nTask 5.2")
arr = [[23,-56,67],
       [90,12,37],
       [17,-45,-14]]
def minn(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if arr[i][j]==map(min, arr):
                if arr[i][j]%2==0:
                    arr[i][j]=0
                if arr[i][j]%2!=0:
                    arr[i][j]=1
    return arr
print(minn(arr))
def mini(a):
    result2 = [min(column) for column in zip(*arr)]
    print(result2)
mini(arr)


#Task_6
print("\nTask 6.1")
def maxrow(arr):
	rows = len(arr)
	col = len(arr[0])
	for i in range(rows):
		maxm = 0
		for j in range(col):
			if arr[i][j] > maxm :
				maxm = arr[i][j]
		print("Max element of row ", i+1, ": ", maxm)
arr = [[23,-56,67],
       [90,12,37],
       [17,-45,-14]]
maxrow(arr)
def mincol(arr):
    c = 0
    l = len(arr)
    for i in range(l):
        minm = arr[0][i]
        for j in range(1, l, 1):
            if (arr[j][i] < minm):
                minm = arr[j][i]
        print("Min element of column ", i+1, ": ", minm)
mincol(arr)
print("\nTask 6.2")
def minmaxDia(arr):
    n = len(arr)
    if (n == 0): return
    mmax = arr[0][0]
    smax = arr[n - 1][0]
    for i in range(n):
        if (arr[i][i] > mmax):
            mmax = arr[i][i]
        if (arr[n - 1 - i][i] > smax):
            smax = arr[n - 1 - i][i]
    maximum = max(mmax, smax)
    print("Main Diagonal Greatest Element : ", mmax)
    print("Secondary Diagonal Greatest Element: ", smax)
    print("Maximum element: ", maximum)
    def swap(arr):
        for i in range(n):
            for j in range(n):
                if arr[i][j]==maximum:
                    m = arr[2][2]
                    arr[i][j] = m
                    arr[2][2] = maximum
        print("Result: \n", arr, end=" ")
    swap(arr)
arr = [[ -5, 2, 7, 4, -10 ],
        [ 5, 15, 7, 8, 6 ],
        [ 16, 2, 11, 3, 4 ],
        [ 8, 99, 70, 5, 8 ],
        [ 7, 66, 7, 1, 17 ]]
print("Original array: ", arr)
minmaxDia(arr)

#Task_7
print("\nTask 7.1")

print("\nTask 7.2")

#Task_8
print("\nTask 8.2")
arr = [[44,56],
    [7 ,81],
    [17 ,77]]

result = [[0,0,0],
         [0,0,0]]
for i in range(len(arr)):
   for j in range(len(arr[0])):
       result[j][i] = arr[i][j]
for r in result:
   print(r)

#Task_15
print("\nTask 15.1")
def ifif(arr):
    lr = len(arr)
    lc = len(arr[0])
    c = 10
    d = 4
    for i in range(0,lr):
        for j in range(0,lc):
            if arr[i][j]==10:
                arr[i][j]*=d
            j+=1
    print(arr)
arr = [[ -5, 2, 7, 4, 10 ],
        [ 5, 15, 7, 8, 6 ],
        [ 16, 2, 11, 3, 4 ],
        [ 8, 99, 70, 10, 8 ],
        [ 7, 66, 7, 1, 17 ]]
ifif(arr)





