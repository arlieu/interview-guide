from data_structures.queues.FIFO import Queue


def BFS(start, end, graph):
    q = Queue()
    q.enqueue((start, [start]))
    while q:
        (vertex, path) = q.dequeue()

        for i in graph[vertex] - set(path):
            if i == end:
                res = str(path + [i])
                print(res)
                return res
            else:
                q.enqueue((i, path+[i]))


if __name__ == "__main__":
    graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

    BFS('A', 'F', graph)