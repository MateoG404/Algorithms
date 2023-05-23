import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = 1  # 1 para rojo, 0 para negro


class RedBlackTree:
    def __init__(self):
        self.NULL_NODE = Node(None)
        self.NULL_NODE.color = 0
        self.NULL_NODE.left = None
        self.NULL_NODE.right = None
        self.root = self.NULL_NODE

    def insert(self, key):
        new_node = Node(key)
        new_node.parent = None
        new_node.key = key
        new_node.left = self.NULL_NODE
        new_node.right = self.NULL_NODE
        new_node.color = 1

        current = self.root
        parent = None
        while current != self.NULL_NODE:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if parent == None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        if new_node.parent == None:
            new_node.color = 0
            return

        if new_node.parent.parent == None:
            return

        self.fix_insert(new_node)

    def fix_insert(self, node):
        while node.parent.color == 1:
            if node.parent == node.parent.parent.right:
                uncle = node.parent.parent.left
                if uncle.color == 1:
                    uncle.color = 0
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.left_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.right

                if uncle.color == 1:
                    uncle.color = 0
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.right_rotate(node.parent.parent)
            if node == self.root:
                break
        self.root.color = 0

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NULL_NODE:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NULL_NODE:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def inorder_traversal(self, node, G):
        if node != self.NULL_NODE:
            self.inorder_traversal(node.left, G)
            G.add_node(node.key, color='red' if node.color == 1 else 'black')
            if node.parent != None:
                G.add_edge(node.parent.key, node.key)
            self.inorder_traversal(node.right, G)

    def generate_graph(self):
        G = nx.Graph()
        self.inorder_traversal(self.root, G)
        return G


# Ejemplo de uso
rbt = RedBlackTree()
rbt.insert(10)
rbt.insert(20)
rbt.insert(30)
rbt.insert(40)
rbt.insert(50)

graph = rbt.generate_graph()

pos = nx.spring_layout(graph)
node_colors = [graph.nodes[n]['color'] for n in graph.nodes()]

nx.draw_networkx(graph, pos=pos, node_color=node_colors, with_labels=True)
plt.show()
