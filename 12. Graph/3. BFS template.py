from collections import deque


class Graph:
    def __init__(self, n):
        self.adjacency_list = [[] for _ in range(n+1)]

    def add_edge(self, u , v):
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)

    def bfs(self, start):
        visited = [False] * (len(self.adjacency_list))
        queue = deque([start])
        visited[start] = True

        while queue:
            node = queue.popleft()
            print(node)

            for neighbor in self.adjacency_list[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

graph = Graph(7)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(2, 5)
graph.add_edge(3, 6)
graph.add_edge(3, 7)

print("BFS starting from vertex 1:")
graph.bfs(1)