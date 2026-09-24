from collections import defaultdict
import random

def graph_generator(n, e):
    #generate our n by n matrix
    matrix = [[0 for i in range(n)] for j in range(n)]

    while(e!=0):
        a = random.randint(0, n-1)
        b = random.randint(0, n-1)

        if a != b and matrix[a][b] == 0:
            matrix[a][b] = 1
            e -= 1

        #generate the weights
        for i in range(n):
            for j in range(n):
                if (matrix[i][j] == 1):
                    matrix[i][j] = random.randint(1, 100)
    return matrix

# Complete Graph
# n = 10
# e = n*(n-1)  
# incom_adjMatrixTest = graph_generator(n, e)
# for i in incom_adjMatrixTest:
#     print(i)

#use the same adjacency matrix graph => convert to use adjacency lists

def convert_to_adjList(graph, n):
    adjList = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 1:
                adjList[i].append((j, graph[i][j]))
    return adjList


#Printing out adj_List
def print_adjList(adjList):
    for i in adjList:
        print(i, end="")
        for j in adjList[i]:
            print(" -> {}".format(j), end="")
        print()


#print_adjList(convert_to_adjList(incom_adjMatrixTest, n))
