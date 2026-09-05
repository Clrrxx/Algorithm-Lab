import inputdata
from keycomp import KeyComparisons

def merge(arr, left, right, mid, myObj):
    n1 = mid - left + 1
    n2 = right - mid

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[left+i]

    for j in range(n2):
        R[j] = arr[mid+1+j]

    i, j = 0, 0
    k = left

    while i<n1 and j < n2:
        if L[i] <= R[j] and myObj.lessthanb(L[i], R[j]):
            arr[k] = L[i]
            i+=1
        elif R[j] <= L[i] and myObj.lessthanb(R[j], L[i]):
            arr[k] = R[j]
            j+=1
        k+=1

    while i < n1:
        arr[k] = L[i]
        i+=1
        k+=1

    while j < n2:
        arr[k] = R[j]
        j+=1
        k+=1

def mergesort(arr, right, left, myObj):
    if left < right:
        mid = (left + right) // 2 

        mergesort(arr, mid, left, myObj)
        mergesort(arr, right, mid+1, myObj)
        merge(arr, left, right, mid, myObj)

data = inputdata.generateData()
myObj = KeyComparisons()

for s in data:
    mergesort(s, len(s), 0, myObj)
    print(s)

    