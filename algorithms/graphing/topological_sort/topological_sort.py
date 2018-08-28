def topologicalSort(node, visited, stack, graph):
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            topologicalSort(i, visited, stack, graph)

    stack.append(node)


if __name__ == "__main__":
    graph = {
        40: [10, 20],
        10: [30],
        20: [10, 30, 60, 50],
        30: [60],
        60: [70],
        50: [70],
        70: []
    }

    visited = {}
    for node in graph.keys():
        visited[node] = False
    stack = []

    topologicalSort(40, visited, stack, graph)

    print(list(reversed(stack)))