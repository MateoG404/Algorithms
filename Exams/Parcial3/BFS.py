# BFS to find the shortest path from collections import defaultdict, deque
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add(self, a, b):
        self.graph[a].append(b)
    
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
            print(node)
            while node != s:
                path.append(node)
                node = parent[node]
                print(node)
            path.append(s)
            path.reverse()
            return path
        else:
            return None

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

value = 4

path = graph.bfs(0, 4)

if path:
    print(f"Ruta más rápida desde 0 hasta {value}: {' -> '.join(map(str, path))}")
else:
    print(f"No se encontró una ruta desde 0 hasta {value}.")
