from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def prim_mst(self):
        key = [float('inf')] * self.V
        parent = [None] * self.V
        mst_set = [False] * self.V

        key[0] = 0
        parent[0] = -1

        for _ in range(self.V):
            u = self._min_key(key, mst_set)
            mst_set[u] = True

            for v, weight in self.graph[u]:
                if not mst_set[v] and weight < key[v]:
                    key[v] = weight
                    parent[v] = u

        self._print_mst(parent)

    def _min_key(self, key, mst_set):
        min_val = float('inf')
        min_index = -1

        for v in range(self.V):
            if not mst_set[v] and key[v] < min_val:
                min_val = key[v]
                min_index = v

        return min_index

    def _print_mst(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(f"{parent[i]} - {i}\t{self._get_weight(parent[i], i)}")

    def _get_weight(self, u, v):
        for vertex, weight in self.graph[u]:
            if vertex == v:
                return weight

# Ejemplo de uso

g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 2, 3)
g.add_edge(1, 2, 4)
g.add_edge(1, 3, 1)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 6)
g.add_edge(3, 4, 3)

g.prim_mst()
