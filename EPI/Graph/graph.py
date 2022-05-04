# Graph Implementation

# A graph can be represented using a dictionary

graph = {
    "a": ["b","c"],
    "b": ["a","d"],
    "c": ["a","d"],
    "d": ["e"],
    "e":["d"]
}

print(graph)