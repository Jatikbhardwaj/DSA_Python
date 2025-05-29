class AdjacencyList:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self,u,v):
        if u not in self.adjacency_list:
            self.adjacency_list[u] =[]
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []
        self.adjacency_list[u].append(v)  # For undirected graphs, also append v to u's list

    def remove_edge(self,u,v):
        #  checks whether the vertex u exists as a key in the adjacency_list dictionary. and checks whether the vertex v is in the list of neighbors for vertex u
        if u in self.adjacency_list and v in self.adjacency_list[u]:
            self.adjacency_list[u].remove(v) # For undirected graphs, also remove v from u's list

    def find_neighbors(self,vertex):
        return self.adjacency_list.get(vertex,[])

    def display(self):
        for vertex, neighbours in self.adjacency_list.items():
            print(f"{vertex} -> {','.join(map(str,neighbours))}")

graph = AdjacencyList()
graph.add_edge(1,0)
graph.add_edge(1,2)
graph.add_edge(2,0)
graph.display()
print("Neighbors of vertex 1:", graph.find_neighbors(1))
graph.remove_edge(1,2)
graph.display()

