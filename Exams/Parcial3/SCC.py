# Python implementation of Kosaraju's algorithm to print all SCCs

from collections import defaultdict

#This class represents a directed graph using adjacency list representation
class Graph:
    def __init__(self,vertices):
            self.V= vertices #No. of vertices
            self.graph = defaultdict(list) # default dictionary to store graph

        # function to add an edge to graph
    def addEdge(self,u,v):
            self.graph[u].append(v)

        # A function used by DFS
    def DFSUtil(self,v,visited):
            # Mark the current node as visited and print it
            visited[v]= True
            print (mapeo2[v],end = " ")
            #Recur for all the vertices adjacent to this vertex
            for i in self.graph[v]:
                if visited[i]==False:
                    self.DFSUtil(i,visited)


    def fillOrder(self,v,visited, stack):
            # Mark the current node as visited
            visited[v]= True
            #Recur for all the vertices adjacent to this vertex
            for i in self.graph[v]:
                if visited[i]==False:
                    self.fillOrder(i, visited, stack)
            stack = stack.append(v)
        

        # Function that returns reverse (or transpose) of this graph
    def getTranspose(self):
            g = Graph(self.V)

            # Recur for all the vertices adjacent to this vertex
            for i in self.graph:
                for j in self.graph[i]:
                    g.addEdge(j,i)
            return g

    def DFS(self, v):
 
        # Create a set to store visited vertices
        visited = set()
 
        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited)

        # The main function that finds and prints all strongly
        # connected components
    def printSCCs(self):
            
        stack = []
            # Mark all the vertices as not visited (For first DFS)
        visited =[False]*(self.V)
            # Fill vertices in stack according to their finishing
            # times
        for i in range(self.V):
                if visited[i]==False:
                    self.fillOrder(i, visited, stack)

            # Create a reversed graph
        gr = self.getTranspose()
            
            # Mark all the vertices as not visited (For second DFS)
        visited =[False]*(self.V)

            # Now process all vertices in order defined by Stack
        while stack:
            i = stack.pop()
            if visited[i]==False:
                gr.DFSUtil(i, visited)
                print("")

global mapeo2
mapeo2 = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J'}

# Create a graph given in the above diagram
g = Graph(10)

letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
mapeo = {}

for indice, letra in enumerate(letras):
    mapeo[letra] = indice

g.addEdge(mapeo['A'],mapeo['B'])
g.addEdge(mapeo['A'],mapeo['C'])
g.addEdge(mapeo['A'],mapeo['D'])
g.addEdge(mapeo['B'],mapeo['E'])
g.addEdge(mapeo['C'],mapeo['I'])
g.addEdge(mapeo['D'],mapeo['B'])
g.addEdge(mapeo['E'],mapeo['B'])
g.addEdge(mapeo['E'],mapeo['G'])
g.addEdge(mapeo['F'],mapeo['B'])
g.addEdge(mapeo['F'],mapeo['D'])
g.addEdge(mapeo['F'],mapeo['G'])
g.addEdge(mapeo['G'],mapeo['D'])
g.addEdge(mapeo['H'],mapeo['A'])
g.addEdge(mapeo['H'],mapeo['B'])
g.addEdge(mapeo['H'],mapeo['C'])
g.addEdge(mapeo['H'],mapeo['I'])
g.addEdge(mapeo['I'],mapeo['B'])
g.addEdge(mapeo['I'],mapeo['E'])
g.addEdge(mapeo['I'],mapeo['G'])
g.addEdge(mapeo['J'],mapeo['C'])
g.addEdge(mapeo['J'],mapeo['I'])
g.addEdge(mapeo['J'],mapeo['G'])






print ("Following are strongly connected components " +
						"in given graph")
g.printSCCs()

#This code is contributed by Neelam Yadav
