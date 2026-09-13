import inputdata
from keycomp import KeyComparisons

data = inputdata.generateData()
myObj = KeyComparisons()

def insertion(data, myObj):
    for i in range(1, len(data)):
        key = data[i]
        j = i-1

        while j >= 0 and myObj.lessthanb(key, data[j]):
            data[j+1] = data[j]
            j -= 1
        
        data[j+1] = key
    return data


# for arr in data:
#     insertionsort(arr, myObj)
#     print(arr)







