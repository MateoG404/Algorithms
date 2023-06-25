# BFS to find the shortest path from collections import defaultdict, deque
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)
            
    def bfs(self, s, value):

        visited = [False] * (max(self.graph) + 1)
        queue = deque()
        parent = {}
        
        path_found = False
        
        queue.append(s)
        
        visited[s] = True

        while queue:
            current_node = queue.popleft()
            
            if current_node == value:
                path_found = True
                break
            
            for neighbor in self.graph[current_node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    parent[neighbor] = current_node
                
        if path_found:
            path = []
            node = value
            while node != s:
                path.append(node)
                node = parent[node]
            path.append(s)
            path.reverse()
            return path
        else:
            return None

    def print_bfs(self, s, value):
        path = self.bfs(s, value)
        
        if path:
            print(f"Ruta más rápida desde {s} hasta {value}: {' -> '.join(map(str, path))}")
        else:
            print(f"No se encontró una ruta desde {s} hasta {value}.")

    def BFS(self, s):
 
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)
        
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
 
        while queue:
 
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print(s, end=" ")
 
            # Get all adjacent vertices of the
            # dequeued vertex s.
            # If an adjacent has not been visited,
            # then mark it visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

# Ejemplo de uso
graph = Graph()

graph.add(0,1)
graph.add(0,2)
graph.add(1,3)
graph.add(2,4)
graph.add(4,5)
graph.add(3,5)


graph.BFS(0)
