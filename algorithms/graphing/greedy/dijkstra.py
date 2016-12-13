'''This code is largely based on K Hong's "DIJKSTRA'S SHORTEST PATH ALGORITHM",
http://www.bogotobogo.com/python/python_Dijkstras_Shortest_Path_Algorithm.php'''


import heapq, math


class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.distance = math.inf
        self.visited = False
        self.previous = None

    def __lt__(self, vertex2):
        return self.id < vertex2.id

    def __le__(self, vertex2):
        return self.id <= vertex2.id

    def __gt__(self, vertex2):
        return self.id > vertex2.id

    def __ge__(self, vertex2):
        return self.id >= vertex2.id

    def addNeighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def getNeighbors(self):
        return self.adjacent.keys()

    def getId(self):
        return self.id

    def getWeight(self, neighbor):
        return self.adjacent[neighbor]

    def setDistance(self, dist):
        self.distance = dist

    def getDistance(self):
        return self.distance

    def setPrevious(self, prev):
        self.previous = prev

    def setVisited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])


class Graph:
    def __init__(self):
        self.vertices = {}
        self.nVertices = 0

    def __iter__(self):
        return iter(self.vertices.values())

    def addVertex(self, node):
        self.nVertices += 1
        newVertex = Vertex(node)
        self.vertices[node] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertices:
            return self.vertices[n]

        return None

    def addEdge(self, source, dest, cost=0):
        if source not in self.vertices:
            self.addVertex(source)

        if dest not in self.vertices:
            self.addVertex(dest)

        self.vertices[source].addNeighbor(self.vertices[dest], cost)
        self.vertices[dest].addNeighbor(self.vertices[source], cost)

    def getVertices(self):
        return self.vertices.keys()

    def setPrevious(self, current):
        self.previous = current

    def getPrevious(self, current):
        return self.previous


def dijkstra(aGraph, start, target):
    # Set the distance for the start node to zero
    start.setDistance(0)

    # Put tuple pair into the priority queue
    unvisited = [(v.getDistance(),v) for v in aGraph]
    heapq.heapify(unvisited)

    while len(unvisited):
        # Pops a vertex with the smallest distance
        uv = heapq.heappop(unvisited)
        current = uv[1]
        current.setVisited()

        #for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue

            newDist = current.getDistance() + current.getWeight(next)

            if newDist < next.getDistance():
                next.setDistance(newDist)
                next.setPrevious(current)
                print('updated : current = %s next = %s new_dist = %s' \
                        %(current.getId(), next.getId(), next.getDistance()))
            else:
                print('not updated : current = %s next = %s new_dist = %s' \
                        %(current.getId(), next.getId(), next.getDistance()))

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited):
            heapq.heappop(unvisited)
        # 2. Put all vertices not visited into the queue
        unvisited = [(v.getDistance(),v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited)


def shortest(v, path):
    if v.previous:
        path.append(v.previous.getId())
        shortest(v.previous, path)

    return

test = Graph()

