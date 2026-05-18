from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

def bfs(graph, start):
    visited, queue, order = {start}, deque([start]), []
    while queue:
        curr = queue.popleft()
        order.append(curr)
        for n in graph[curr]:
            if n not in visited:
                visited.add(n)
                queue.append(n)
    return "".join(order)

def dfs(graph, curr, visited=None, order=None):
    if visited is None: visited = set()
    if order is None: order = []
    visited.add(curr)
    order.append(curr)
    for n in graph[curr]:
        if n not in visited:
            dfs(graph, n, visited, order)
    return "".join(order)

print(f"BFS Traversal Order: {bfs(graph, 'A')}")
print(f"DFS Traversal Order: {dfs(graph, 'A')}")