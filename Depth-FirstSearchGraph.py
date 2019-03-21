"""
Using BFS or DFS can make a difference according to the way in which you
need to traverse a graph. 
From a programming point of view, the difference between the two algorithms is how each one stores the vertexes to explore the
following:
» A queue for BFS, a list that works according to the FIFO principle. Newly
discovered vertexes don’t wait long for processing.
» A stack for DFS, a list that works according to the last in/first out (LIFO)
principle.

When performing a DFS, the algorithm begins at the graph root and 
then explores every node from that root down a single path to the end. 
It then backtracks and begins exploring the paths not taken in the current search path
until it reaches the root again. 
At that point, if other paths to take from the root are available, the algorithm chooses one and begins the same search again. 
The idea is to explore each path completely before exploring any other path. 
To make this search technique work, the algorithm must mark each vertex it visits. 
In this way, it knows which vertexes require a visit and can determine which path to take next. 
"""

graph = {'A': ['B', 'C'],
 'B': ['A', 'C', 'D'],
 'C': ['A', 'B', 'D', 'E'],
 'D': ['B', 'C', 'E', 'F'],
 'E': ['C', 'D', 'F'],
 'F': ['D', 'E']}
def dfs(graph, start):
    stack = [start]
    parents = {start: start}
    path = list()
    while stack:
        print ('Stack is: %s' % stack)
        vertex = stack.pop(-1)
        print ('Processing %s' % vertex)
        for candidate in graph[vertex]:
            if candidate not in parents:
                parents[candidate] = vertex
                stack.append(candidate)
                print ('Adding %s to the stack'% candidate)
        path.append(parents[vertex]+'>'+vertex)
    return path[1:]
steps = dfs(graph, 'A')
print ('\nDFS:', steps)

"""
O/P:
----

Stack is: ['A']
Processing A
Adding B to the stack
Adding C to the stack
Stack is: ['B', 'C']
Processing C
Adding D to the stack
Adding E to the stack
Stack is: ['B', 'D', 'E']
Processing E
Adding F to the stack
Stack is: ['B', 'D', 'F']
Processing F
Stack is: ['B', 'D']
Processing D
Stack is: ['B']
Processing B

DFS: ['A>C', 'C>E', 'E>F', 'C>D', 'A>B']

Note that the output is not the same as for the BFS. 
In this case, the processing route begins with node A and moves to the opposite side of the graph, to node F.
The code then retraces back to look for overlooked paths. As discussed, this behavior
depends on the use of a stack structure in place of a queue. 
Reliance on a stack means that you could also implement this kind of search using recursion. 
The use of recursion would make the algorithm faster, so you could obtain results faster
than when using a BFS. 
The trade-off is that you use more memory when using recursion.
"""
