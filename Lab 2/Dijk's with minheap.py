from collections import defaultdict

class Heap():
    def __init__(self):
        self.array = []
        self.size = 0
        self.pos = []

    def newMinHeapNode(self, v, dist):
        MinHeapNode = [v, dist]
        return MinHeapNode

    def swapMinHeapNode(self, a, b):
        t = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = t

    def minHeapify(self, index):
        smallest = index
        left = 2*index + 1
        right = 2*index + 2

        if left < self.size and self.array[left][1] < self.array[smallest][1]:
            smallest = left

        if right < self.size and self.array[right][1] < self.array[smallest][1]:
            smallest = right

        #nodes need to be swapped in min heap if index is not smallest
        if smallest != index:

            #swap positions
            self.pos[self.array[smallest][0]] = index
            self.pos[self.array[index][0]] = smallest

            #swap nodes
            self.swapMinHeapNode(index, smallest)

            self.minHeapify(smallest)

    def extractMin(self):
        if self.isEmpty() == True:
            return

        #store root
        root = self.array[0]

        #Replace the last node with root
        lastNode = self.array[self.size - 1]
        self.array[0] = lastNode

        #update the position of last node
        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1

        #reduce heap size and heapify
        self.size -= 1
        self.minHeapify(0)

    def isEmpty(self):
        return self.size == 0

    def decreaseKey(self, v, dist):

        #store index of v in heap array
        i = self.pos[v]

        #get the node and update the dist
        self.array[i][1] = dist

        #travel up the tree while it is not heapified
        while (i > 0 and self.array[i][1] < self.array[(i-1)//2][1]):

            #swap the node with its parent
            self.pos[self.array[i][0]] = (i-1)//2
            self.pos[self.array[(i-1)//2][0]] = i
            self.swapMinHeapNode(i, (i-1)//2)

            #move to parent index
            i = (i-1)//2

    def isInMinheap(self, v):
        if self.pos[v] < self.size:
            return True
        return False


class Graph():
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def dijkstra(self, source):
        V = self.V
        dist = []

        minHeap = Heap()

        for v in range(V):
            dist.append(float('inf'))
            minHeap.array.append(minHeap.newMinHeapNode(v, dist[v]))
            minHeap.pos.append(v)

        #source = 0, it is extracted first
        minHeap.pos[source] = source
        dist[source] = 0
        minHeap.decreaseKey(source, dist[source])

        minHeap.size = V

        while minHeap.isEmpty == False:

            #extract the vertex with min dist
            newHeapNode = minHeap.extractMin()
            u = newHeapNode[0]

            #traverse all adjacent vertices of u and update their position
            for pCrawl in self.graph[u]:
                v = pCrawl[0]

                #if shortest dist to v is not finalised, and dist to v thru u is less than its prev calc dist
                if (minHeap.isInMinheap(v) and dist[u] != float('inf') and pCrawl[1] + dist[u] < dist[v]):
                    dist[v] = dist[u] + pCrawl[1]

                    minHeap.decreaseKey(v, dist[v])
    


#temporarily for now not sure if can just use heapq 
