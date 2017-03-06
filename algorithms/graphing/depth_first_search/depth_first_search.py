def DFS(start, end, graph, path=[]):
    if start not in path:
        path.append(start)
    for i in graph[start]:
        if i not in path:
            path.append(i)
            if i == end:
                return path
            return DFS(i, end, graph, path)


if __name__ == "__main__":
    graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

    print(DFS('A', 'F', graph))