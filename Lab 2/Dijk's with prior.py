import GraphFns
import sys

def dijkstra_priorq(graph, source):
    dist = []
    prev = []
    seen = []
    pq = []

    inf = sys.maxsize
    graphLen = len(graph)


    #prior queue and graph initialisation
    for i in range(graphLen):   #for each vertex v
        dist.append(inf)    #set all dist to inf
        prev.append(-1)     #set prev to null
        seen.append(0)      #set seen to empty
        pq.append(i)        #put all vertices into pq according to d[v]'s increasing order

    #set source to 0
    dist[source] = 0

    while len(pq) != 0:
        cheap = 0
        for i in range(len(pq)):
            if (dist[pq[i]] < dist[pq[cheap]]):
                cheap = i
        u = pq.pop(cheap)

        seen[u] = 1     #add u to seen 

        for i in range(graphLen):
            vertex = i
            weight = graph[u][i]

            if weight > 0:
                #if vertex is not in seen and dist[vertex] > source node + weighted edge => update
                if ((seen[vertex] != 1) and (dist[vertex] > dist[u] + weight)):
                    dist[vertex] = dist[u] + weight
                    prev[vertex] = u

    return dist, prev


if __name__ == "__main__":
    src = 0

    #test 
    n = 10
    e = n*(n-1)
    adjMatrix = GraphFns.graph_generator(n, e)
    
    result, another = dijkstra_priorq(adjMatrix, src)
    print(*result)


