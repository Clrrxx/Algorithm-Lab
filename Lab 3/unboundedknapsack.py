n = 3
m = 16
profit = [7, 6, 9]
weight = [4, 5, 8]
array = [0 for _ in range(m+1)]

def dp(n, m, array, profit, weight):

    for j in range(m+1):
        for i in range(n):
            if weight[i] <= j:
                array[j] = max((array[j-weight[i]]+profit[i]), array[j])
    return array[m]

max = dp(n, m, array, profit, weight)
print(max)
print(array)