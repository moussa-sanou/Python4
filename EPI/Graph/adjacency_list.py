
# Create a graph with adjacency list to access element

class Graph:
    def __init__(self, num_vrtx, edges):
        self.num_vrtx = num_vrtx
        self.data = [[] for _ in range(num_vrtx)]  # In python when declaring a variable that will not be used we can use an underscore(_) instead of a letter or word
        for v1, v2 in edges:
            self.data[v1].append(v2)
            self.data[v2].append(v1)
    # The following functions are use in making the output of the adjacency easily readable
    def __repr__(self):
        return "\n".join(["{}: {}".format(n, neighbors) for n, neighbors in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()

num_vrtx = 5
edges = [(0,1), (0,4), (1,2), (1,3), (1,4), (2,3), (3,4)]
graph1 = Graph(num_vrtx, edges)
print(graph1)


# Pros of adjacency list
''' An adjacency list is efficient in terms of storage because we only need to store the values for the edges. For a 
sparse graph with millions of vertices and edges, this can mean a lot of saved space
It also helps to find all vertices adjacent to a vertex easily.'''

# Cons of Adjacency list
'''Finding the adjacent list is not quicker than the adjacency matrix because all the connected nodes must be first 
explored to find them'''