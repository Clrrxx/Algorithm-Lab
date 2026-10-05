import GraphFns
import sys

def dijkstra_matrix_array(graph, source):
    V = len(graph)

    dist = [sys.maxsize] * V

    #initialise visited list
    visited = [False] * V

    dist[source] = 0

    for _ in range(V):

        #find dist with min dist
        u = -1
        min_dist = sys.maxsize

        for cand in range(V):
            if not visited[cand] and dist[cand] < min_dist:
                min_dist = dist[cand]
                u = cand

        #if no reachable unvisted => break
        if u == -1:
            break

        visited[u] = True

        #adj matrix relaxation steps
        for v in range(V):
            weight = graph[u][v]

            if weight != 0 and not visited[v]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

    return dist

if __name__ == "__main__":
    src = 0

    #test 
    n = 10
    e = n*(n-1)
    adjMatrix = GraphFns.graph_generator(n, e)
    
    result = dijkstra_matrix_array(adjMatrix, src)
    print(*result)



# what is the difference here?
# note senior's implmentation is using priority queue implementation whereas this implementation
# uses purely an array, no priority queue. This is a very naive implementation and is better for dense graphs
    


