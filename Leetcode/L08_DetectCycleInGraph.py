"""
Detect cycle in a graph
"""

from tkinter import E

def has_cycle(graph: dict, visited: list, node: int, path: list) -> bool:
    if node in visited:
        return True
    
    visited.append(node)
    # print(visited)

    for pt in path:
        if has_cycle(graph, visited, pt, graph[pt]):
            return True
    
    visited.remove(node)

    return False


def solution(nodes, edges):
    # if there are no edges, there is no cycle
    if not edges or len(edges) == 0:
        return False

    # if the length of edges is not even, there is no cycle
    if len(edges) % 2 != 0:
        return False

    # if there are no nodes, there is no cycle
    if nodes == 0:
        return False
    
    # define a dictionary to store the graph
    visited = []

    # define a dictionary with the given number of nodes
    graph = {i: [] for i in range(nodes)}

    # build the graph
    for i in range(0, len(edges), 2):
        if edges[i] not in graph:
            graph[edges[i]] = []
        graph[edges[i]].append(edges[i + 1])

    # check if there is a cycle
    for node, path in graph.items():
        if has_cycle(graph, visited, node, path):
            return True

    return False


def main():
    print(solution(4, [0, 1, 1, 2, 2, 3, 3, 0]))
    print(solution(4, [0, 1, 1, 2, 1, 3, 1, 3]))
    print(solution(4, [0, 1, 1, 2, 2, 3, 1, 3, 0, 3]))

if __name__ == "__main__":
    main()