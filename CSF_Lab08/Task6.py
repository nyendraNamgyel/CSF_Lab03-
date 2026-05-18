from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

def find_shortest_path(graph, start, target):
    queue = deque([[start]])
    visited = set()
    
    while queue:
        current_path = queue.popleft()
        last_node = current_path[-1]
        
        if last_node == target:
            return current_path
            
        if last_node not in visited:
            visited.add(last_node)
            for neighbor in graph[last_node]:
                new_path = list(current_path)
                new_path.append(neighbor)
                queue.append(new_path)
                
    return None

shortest_path = find_shortest_path(graph, 'A', 'F')
print("Shortest path from A to F:")
print(" -> ".join(shortest_path))