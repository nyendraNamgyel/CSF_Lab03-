graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['B', 'C']
}

print("Graph Representation:")
for vertex in sorted(graph.keys()):
    print(f"{vertex} -> {graph[vertex]}")