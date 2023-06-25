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
g = Graph()



g.add(1, 0)
g.add(0, 2)
g.add(2, 1)
g.add(0, 3)
g.add(3, 4)


g.DFS(0)
