import inputdata
import mergesorted
import insertionsorted
from keycomp import KeyComparisons

data = inputdata.generateData()
myObj = KeyComparisons()

#Use an arbitrary S as place holder for now to set as a threshold for when algorithm swaps
#When  <= S, use insertion
#else >S, use merge

def hybridSort(arr, S, myObj):
    #This is the base case since we are recursively calling merge
    if len(arr) <= 1:
        return arr

    #Merge sort
    if len(arr) > S:
        m = len(arr)//2

        arr[:m] = hybridSort(arr[:m], S, myObj)
        arr[m:] = hybridSort(arr[m:], S, myObj)

        #mid = m-1 because it will result in an Off by 1 error if just m
        arr = mergesorted.merge(arr, 0, m-1, len(arr)-1, myObj)
        return arr

    else:
        arr = insertionsorted.insertion(arr, myObj)
        return arr


for s in data:
    #let the S threshold be 10
    hybridSort(s, 10, myObj)
    print(s)

#test on small sample size temporarily

# arr = [4,2,10,100,3,59,43,-1,-8,0,7,12,11,3,3,3]
# print(hybridSort(arr,3, myObj))



