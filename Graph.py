"""
A graph is a sort of a tree extension. As with trees, you have nodes that connect to
each other to create relationships. However, unlike binary trees, a graph can
have more than one or two connections. In fact, graph nodes often have a multitude
of connections. 

Graphs also add a few new twists that you might not have thought about before.
For example, a graph can include the concept of directionality. Unlike a tree,
which has parent/child relationships, a graph node can connect to any other
node with a specific direction in mind. Think about streets in a city. Most streets
are bidirectional, but some are one-way streets that allow movement in only one
direction.

The presentation of a graph connection might not actually reflect the realities of
the graph. A graph can designate a weight to a particular connection. The weight
could define the distance between two points, define the time required to traverse
the route, or provide other sorts of information.
"""

graph = {
        'A': ['B', 'F'],
        'B': ['A', 'C'],
        'C': ['B', 'D'],
        'D': ['C', 'E'],
        'E': ['D', 'F'],
        'F': ['E', 'A']
        }
# Note: 
    # Node checking in this simple graph is done in graph Dictionary values listing
    
def find_path(graph, start, end, path=[]):
    path = path + [start]
    
    if start == end:
        print("Ending")
        return path
    
    for node in graph[start]: # get start key values list in for loop
        print("Checking Node ",node)
        
        if node not in path:
            print("Path so far ", path)
            
            newp = find_path(graph, node, end, path)
            
            if newp:
                return newp

find_path(graph, 'B', 'E')
"""
O/P
---

Checking Node  A
Path so far  ['B']
Checking Node  B
Checking Node  F
Path so far  ['B', 'A']
Checking Node  E
Path so far  ['B', 'A', 'F']
Ending

"""
find_path(graph, 'C', 'E')
"""
O/P
---

Checking Node  B
Path so far  ['C']
Checking Node  A
Path so far  ['C', 'B']
Checking Node  B
Checking Node  F
Path so far  ['C', 'B', 'A']
Checking Node  E
Path so far  ['C', 'B', 'A', 'F']
    
"""
