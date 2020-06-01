from array import *
elements = array('i',[])
numberOfElements = int(input("Enter number of elements: "))
for i in range(numberOfElements):
    e = int(input("Enter Elements: "))
    elements.append(e)
requiredSum = int(input("Enter required sum: "))
def checkArray(elements, sum):
    length = len(elements)
    quickSort(elements, 0, length-1)
    l = 0
    r = length -1
    while l<r:
        if (elements[l]+elements[r] == sum):
            return True
        elif (elements[l]+elements[r] < sum):
            l += 1
        else:
            r -= 1
    return False
def quickSort(A, si, ei): 
    if si < ei: 
        pi = partition(A, si, ei) 
        quickSort(A, si, pi-1) 
        quickSort(A, pi + 1, ei) 
def partition(A, si, ei): 
    x = A[ei] 
    i = (si-1) 
    for j in range(si, ei): 
        if A[j] <= x: 
            i += 1
            A[i], A[j] = A[j], A[i] 
        A[i + 1], A[ei] = A[ei], A[i + 1] 
    return i + 1
result = checkArray(elements,requiredSum)
if result:
    print("Yes")
else:
    print("No")