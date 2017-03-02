from data_structures.graphs.adjacency_matrix import AdjacencyMatrix
import operator
import sys


def gridToGraph(matrix):
    '''Converts 2D array to adjacency matrix'''
    n = len(matrix)
    graph = AdjacencyMatrix(n)

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == "O":
                graph.addEdge(i, j)

    return graph


def heuristic(start, end):
    '''Manhattan Distance heuristic'''
    return abs(start[0]-end[0]) + abs(start[1]-end[1])


def path(cameFrom, current):
    '''Recreates path'''
    totalPath = [current]
    while current in cameFrom.keys():
        current = cameFrom[current]
        totalPath.append(current)

    return totalPath


def aStar(start, end, graph):
    '''A* Search Algorithm'''

    # Evaluated nodes
    closedSet = set()

    # Unevaluated nodes
    openSet = set()
    openSet.add(start)

    # Most efficient way to reach node
    cameFrom = {}

    # Cost of getting to each node from start node
    # Initially cost of getting to any node is infinite, except for start
    gScore = {}
    for i in range(len(graph)):
        for j in range(len(graph)):
            gScore[(i, j)] = sys.maxsize

    # Cost of getting to goal node from start node
    fScore = gScore

    gScore[start] = 0
    fScore[start] = heuristic(start, end)
    while openSet is not None:
        current = None
        tmp = sorted(fScore.items(), key=operator.itemgetter(1))
        for i in tmp:
            if i[0] in openSet:
                current = i[0]
                break
        #current = min(key for key, value in fScore.items() if key in openSet)

        if current == end:
            return path(cameFrom, current)

        openSet.remove(current)
        closedSet.add(current)

        currentNeighbors = [(current[0]+1, current[1]), (current[0], current[1]+1),(current[0]-1, current[1]), \
                            (current[0], current[1]-1),]
        for neighbor in currentNeighbors:
            if neighbor in closedSet:
                continue        #  Ignore evaluated neighbors
            if not graph.hasEdge(neighbor[0], neighbor[1]):
                continue
            if neighbor[0] < 0 or neighbor[1] < 0 or neighbor[0] > len(graph)-1 or neighbor[1] > len(graph)-1:
                continue

            tmp_gScore = gScore[current]+1          #  Assumption is that graph is unweighted
                                                    #  If graph is weighted, adjust tmp_gScore to variable cost

            if neighbor not in openSet:             #  New node discovered
                openSet.add(neighbor)
            elif tmp_gScore >= gScore[neighbor]:    #  Ignore more expensive paths
                continue

            # Running best path
            cameFrom[neighbor] = current
            gScore[neighbor] = tmp_gScore
            fScore[neighbor] = gScore[neighbor] + heuristic(neighbor, end)

    return -1