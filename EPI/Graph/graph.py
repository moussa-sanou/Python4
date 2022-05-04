# Graph Implementation

# A graph can be represented using a dictionary

graph = {
    "a": ["b","c"],
    "b": ["a","d"],
    "c": ["a","d"],
    "d": ["e"],
    "e":["d"]
}

# print(graph)

# Display graph vertices
'''To display the graph vertices we simply find the keys of graph dictionary. We use the key() method'''

class graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict
    # Get the keys in the dictionary representing the vertices
    def getVertices(self):
        return list(self.gdict.keys())

# Create a dictionary with graph element
graph_elements = {
    "a": ["b","c"],
    "b": ["a","d"],
    "c": ["a","d"],
    "d": ["e"],
    "e":["d"]
}

g = graph(graph_elements)
print(g.getVertices())
