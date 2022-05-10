
# Create a graph with adjacency list to access element

class Graph:
    def __init__(self, num_vrtx, edges):
        self.num_vrtx = num_vrtx
        self.data = [[] for _ in range(num_vrtx)]  # In python when declaring a variable that will not be used we can use an underscore(_) instead of a letter or word
        for v1, v2 in edges:
            self.data[v1].append(v2)
            self.data[v2].append(v1)

num_vrtx = 5
edges = [(0,1), (0,4), (1,2), (1,3), (1,4), (2,3), (3,4)]
graph1 = Graph(num_vrtx, edges)
print(graph1.data)