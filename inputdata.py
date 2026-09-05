import numpy as np

inputdata = []

for i in range(10):
    inputdata.append((i+1) * 1000) 
    inputdata.append((i+1) * 10000)
    inputdata.append((i+1) * 100000)
    inputdata.append((i+1) * 1000000) 
    inputdata.append((i+1) * 10000000)

# remove duplicates and sort them to ensure within specific range
inputdata = sorted(set(inputdata))

print(inputdata)

data = []
rng = np.random.default_rng(seed = 42)

for s in inputdata:
    temp = rng.integers(low=1, high=s+1, size= s)
    data.append(temp)

# for i in range(len(data)):
#     print("ArraySize =", len(data[i]))
#     print("Min of Array: ", min(data[i]))
#     print("Max of Array: ", max(data[i]))
#     print()


# verify if all data is printed correctly
print(data[0])





