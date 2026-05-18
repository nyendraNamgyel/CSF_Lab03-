class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, u, v):
        if u in self.adj_list and v in self.adj_list:
            if v not in self.adj_list[u]:
                self.adj_list[u].append(v)
            if u not in self.adj_list[v]:
                self.adj_list[v].append(u)

    def display(self):
        print("Graph Representation:")
        for vertex in sorted(self.adj_list.keys()):
            print(f"{vertex} -> {self.adj_list[vertex]}")

g = Graph()

# 1. Add vertices
for vertex in ['A', 'B', 'C', 'D']:
    g.add_vertex(vertex)

# 2. Add edges
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')

# 3. Display the graph
g.display()