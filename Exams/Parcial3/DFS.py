from collections import defaultdict, deque


class Graph : 
    
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add(self, a, b):
        self.graph[a].append(b)
    
    # A function used by DFS
    def DFSUtil(self, v, visited):
 
        # Mark the current node as visited
        # and print it
        visited.add(v)
        print(v, end=' ')
 
        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
 
     
    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v):
 
        # Create a set to store visited vertices
        visited = set()
 
        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited)

# Ejemplo de uso
graph = Graph()

graph.add(0, 1)
graph.add(0, 2)
graph.add(1, 0)
graph.add(1, 4)
graph.add(1, 5)
graph.add(2, 0)
graph.add(2, 3)
graph.add(2, 5)
graph.add(2, 4)
graph.add(3, 2)
graph.add(3, 5)
graph.add(4, 2)
graph.add(4, 1)
graph.add(4, 5)
graph.add(5, 1)
graph.add(5, 4)
graph.add(5, 2)
graph.add(5, 3)

graph.DFS(3)
