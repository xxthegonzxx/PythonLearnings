# Write a Python program to add 'ing' at the end
# of a given string (length should be at least 3).
# If the given string already ends with 'ing' then add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchanged.


# def string_func(str1):

# Graph Traversal

class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

# Get the keys of the dictionary
    def getVertices(self):
        return list(self.gdict.keys())

graph_elements = {
    'a': ['b'],
    'b': ['c', 'd'],
    'c': [],
    'd': ['e'],
    'e': []
    }

g = graph(graph_elements)
print(g.getVertices())
