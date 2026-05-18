graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

def dfs_traversal(graph, current_node, visited=None, traversal_order=None):
    if visited is None:
        visited = set()
    if traversal_order is None:
        traversal_order = []
        
    visited.add(current_node)
    traversal_order.append(current_node)
    
    for neighbor in graph[current_node]:
        if neighbor not in visited:
            dfs_traversal(graph, neighbor, visited, traversal_order)
            
    return "".join(traversal_order)

output = dfs_traversal(graph, 'A')
print(f"DFS Traversal starting from A:\n{output}")