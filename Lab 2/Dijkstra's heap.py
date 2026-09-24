# Dijkstra's algorithm: 
# Find the shortest path distances from the source vertex to all other vertices in the graph
import heapq
import sys
import GraphFns


def dijkstra_list_heap(adj, source):
    V = len(adj)

    #min heap priority queue, stores pairs of (distance, node)
    pq = []

    #set the distance to infinite
    dist = [sys.maxsize] * V

    #distance from source to itself is 0
    dist[source] = 0

    heapq.heappush(pq, (0, source))

    #process queue until all reacheable vertices are reached
    while pq:
        d, u = heapq.heappop(pq)

        #if distance is not shortest skip
        if d > dist[u]:
            continue

        #explore all neighbours of the current vertex
        for v, w in adj[u]:

            #if we found a shorter path to v through u, update it 
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    #return final shortest
    return dist


#testing
if __name__ == "__main__":
    src = 0

    #test 
    n = 10
    e = n*(n-1)
    adjMatrix = GraphFns.graph_generator(n, e)
    adjList = GraphFns.convert_to_adjList(adjMatrix, n)
    
    result = dijkstra_list_heap(adjList, src)
    print(*result)


