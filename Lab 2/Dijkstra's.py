# Dijkstra's algorithm: 
# Find the shortest path distances from the source vertex to all other vertices in the graph
import heapq
import sys


def dijkstra(adj, source):
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
    
    adj = [
        [(1, 4), (2, 8)],
        [(0, 4), (4, 6), (2, 3)],
        [(0, 8), (3, 2), (1, 3)],
        [(2, 2), (4, 10)],
        [(1, 6), (3, 10)]
    ]
    
    result = dijkstra(adj, src)
    print(*result)


