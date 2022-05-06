
# Display graph edges

'''Finding the graph edges is little tricker than the vertices as we have to find each of the pairs of vertices which
have an edge in between them. So we create an empty list of edges then iterate through the edge values associated with
each of the vertices. A list is formed containing the distinct group of edges'''

class graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def edges(self):
        return self.findedges()

# Find the distinct list of edges
    def findedges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename

# Create the dictionary with the graph elements

graph_elements = {
    "a": ["b","c"],
    "b": ["a","d"],
    "c": ["a","d"],
    "d": ["e"],
    "e":["d"]
}

g = graph(graph_elements)
print(g.edges())