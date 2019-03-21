"""
Using BFS or DFS can make a difference according to the way in which you
need to traverse a graph. 
From a programming point of view, the difference between the two algorithms is how each one stores the vertexes to explore the
following:

» A queue for BFS, a list that works according to the FIFO principle. Newly
discovered vertexes don’t wait long for processing.
» A stack for DFS, a list that works according to the last in/first out (LIFO)
principle.

A breadth-first search (BFS) begins at the graph root and explores every node that
attaches to the root. 
It then searches the next level — exploring each level in turn until it reaches the end. 
Consequently, in the example graph, the search explores from A to B and C before it moves on to explore D. 
BFS explores the graph in a systematic way, exploring vertexes all around the starting vertex in a circular
fashion. 
It begins by visiting all the vertexes a single step from the starting vertex;
it then moves two steps out, then three steps out, and so on. 

The following code demonstrates how to perform a breadth-first search.
The output shows how the algorithm searches. 
It’s in the order that you expect — one level at a time. 
The biggest advantage of using BFS is that it’s guaranteed
to return the shortest path between two points as the first output when used to
find paths.

The example code uses a simple list as a queue. 
For this purpose, Python provides an even better data structure called a deque (pronounced deck). 
"""
graph = {'A': ['B', 'C'],
 'B': ['A', 'C', 'D'],
 'C': ['A', 'B', 'D', 'E'],
 'D': ['B', 'C', 'E', 'F'],
 'E': ['C', 'D', 'F'],
 'F': ['D', 'E']}
def bfs(graph, start):
    queue = [start]
    queued = list()
    path = list()
    while queue:
        print ('Queue is: %s' % queue)
        vertex = queue.pop(0)
        print ('Processing %s' % vertex)
        for candidate in graph[vertex]:
            if candidate not in queued:
                queued.append(candidate)
                queue.append(candidate)
                path.append(vertex+'>'+candidate)
                print ('Adding %s to the queue'% candidate)
    return path

steps = bfs(graph, 'A')
print ('\nBFS:', steps)

"""
O/P:
----
Queue is: ['A']
Processing A
Adding B to the queue
Adding C to the queue
Queue is: ['B', 'C']
Processing B
Adding A to the queue
Adding D to the queue
Queue is: ['C', 'A', 'D']
Processing C
Adding E to the queue
Queue is: ['A', 'D', 'E']
Processing A
Queue is: ['D', 'E']
Processing D
Adding F to the queue
Queue is: ['E', 'F']
Processing E
Queue is: ['F']
Processing F

BFS: ['A>B', 'A>C', 'B>A', 'B>D', 'C>E', 'D>F']
"""
