from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

def bfs_traversal(graph, start_node):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    traversal_order = []

    while queue:
        current = queue.popleft()
        traversal_order.append(current)
        
        # Traverse neighbors
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return "".join(traversal_order)

output = bfs_traversal(graph, 'A')
print(f"BFS Traversal starting from A:\n{output}")