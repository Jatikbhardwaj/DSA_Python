class AdjacencyMatrix:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matrix = [[0 for i in range(num_vertices)]for j in range(num_vertices)]
    def add_edge(self, u, v):
        if u >= self.num_vertices or v >= self.num_vertices:
            raise ValueError("Vertex index out of bounds")
        self.matrix[u][v] = 1 # For undirected graphs, also set self.matrix[v][u] = 1
    def remove_edge(self, u, v):
        if u >= self.num_vertices or v >= self.num_vertices:
            raise ValueError("Vertex index out of bounds")
        self.matrix[u][v] = 0 # For undirected graphs, also set self.matrix[v][u] = 0

    def find_neighbours(self, vertex):
        if vertex >= self.num_vertices:
            raise ValueError("Vertex index out of bounds")
        neighbours = []
        for i in range(self.num_vertices):
            if self.matrix[vertex][i] == 1:
                neighbours.append(i)
        return neighbours
    def display(self):
        for row in self.matrix:
            print(" ".join(map(str,row)))


graph = AdjacencyMatrix(3)
graph.add_edge(1,0)
graph.add_edge(1,2)
graph.add_edge(2,0)
graph.display()
print("Neighbours of vertex 1:", graph.find_neighbours(1))
graph.remove_edge(1,0)
graph.display()