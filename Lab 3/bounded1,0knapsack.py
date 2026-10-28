def dp(n, m, V, profit, weight):
   
    for i in range(1, n+1):
        for j in range(1, m+1):
            if weight[i-1] <= j:
                V[i][j] = max((V[i-1][j-weight[i-1]] + profit[i-1]), V[i-1][j])
            else:
                V[i][j] = V[i-1][j]
    return V[n][m]

n = 3
m = 17
V = [[0 for _ in range(m+1)] for _ in range(n+1)]
profit = [7, 6, 9]
weight = [4, 5, 8]
max = dp(n, m, V, profit, weight)


print(max)
for i in range(n+1):
    print(V[i])
    









