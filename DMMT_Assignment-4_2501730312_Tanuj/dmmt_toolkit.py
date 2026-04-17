# DMMT: BST + Graph + HashTable

# ---------------- BST ----------------

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return BSTNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # node to delete found
            # case 1: no child
            if node.left is None and node.right is None:
                return None
            # case 2: one child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # case 3: two children
            # find inorder successor (smallest in right subtree)
            succ = node.right
            while succ.left is not None:
                succ = succ.left
            node.key = succ.key
            node.right = self._delete(node.right, succ.key)

        return node

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node is None:
            return
        self._inorder(node.left, result)
        result.append(node.key)
        self._inorder(node.right, result)


def test_bst():
    print("=== TASK 1: BST TESTS ===")
    bst = BST()
    values = [50, 30, 70, 20, 40, 60, 80]
    print("Inserting:", values)
    for v in values:
        bst.insert(v)
    print("Inorder after insertion:", bst.inorder())

    # search
    print("Search 20:", bst.search(20))
    print("Search 90:", bst.search(90))

    # delete leaf node 20
    print("\nDelete leaf node 20")
    bst.delete(20)
    print("Inorder after deleting 20:", bst.inorder())

    # create one-child node: insert 65 then delete 60
    print("\nInsert 65 to make 60 a one-child node")
    bst.insert(65)
    print("Inorder after inserting 65:", bst.inorder())

    print("\nDelete node 60 (one child)")
    bst.delete(60)
    print("Inorder after deleting 60:", bst.inorder())

    # delete node with two children: delete 30
    print("\nDelete node 30 (two children)")
    bst.delete(30)
    print("Inorder after deleting 30:", bst.inorder())
    print("=== END BST TESTS ===\n")


# ---------------- Graph (Adjacency List + BFS + DFS) ----------------

from collections import deque


class Graph:
    def __init__(self):
        # adjacency list: node -> list of (neighbor, weight)
        self.adj = {}

    def add_edge(self, u, v, w):
        if u not in self.adj:
            self.adj[u] = []
        self.adj[u].append((v, w))

    def print_adj_list(self):
        print("Adjacency List:")
        for node in self.adj:
            edges = ", ".join([f"{node}->{v}({w})" for v, w in self.adj[node]])
            print(node, ":", edges)

    def bfs(self, start):
        print("\nBFS from", start)
        visited = set()
        order = []
        q = deque()
        q.append(start)
        visited.add(start)

        while q:
            u = q.popleft()
            order.append(u)
            for v, _ in self.adj.get(u, []):
                if v not in visited:
                    visited.add(v)
                    q.append(v)

        print("BFS order:", order)

    def dfs(self, start):
        print("\nDFS from", start)
        visited = set()
        order = []

        def _dfs(u):
            visited.add(u)
            order.append(u)
            for v, _ in self.adj.get(u, []):
                if v not in visited:
                    _dfs(v)

        _dfs(start)
        print("DFS order:", order)


def test_graph():
    print("=== TASK 2: GRAPH TESTS ===")
    g = Graph()
    # Suggested graph
    g.add_edge("A", "B", 2)
    g.add_edge("A", "C", 4)
    g.add_edge("B", "D", 7)
    g.add_edge("B", "E", 3)
    g.add_edge("C", "E", 1)
    g.add_edge("D", "F", 5)
    g.add_edge("E", "D", 2)
    g.add_edge("E", "F", 6)
    g.add_edge("C", "F", 8)

    g.print_adj_list()
    g.bfs("A")
    g.dfs("A")
    print("=== END GRAPH TESTS ===\n")


# ---------------- Hash Table (Separate Chaining) ----------------

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # each bucket is a list (chain)

    def _hash(self, key):
        return key % self.size

    def insert(self, key, value):
        idx = self._hash(key)
        # update if key already exists
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, value)
                return
        # else append new pair
        self.table[idx].append((key, value))

    def get(self, key):
        idx = self._hash(key)
        for k, v in self.table[idx]:
            if k == key:
                return v
        return None

    def delete(self, key):
        idx = self._hash(key)
        bucket = self.table[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False

    def print_table(self):
        print("Hash Table (index: chain):")
        for i, bucket in enumerate(self.table):
            print(i, ":", bucket)


def test_hash_table():
    print("=== TASK 3: HASH TABLE TESTS ===")
    ht = HashTable(5)
    keys = [10, 15, 20, 7, 12]
    print("Inserting (key, value) where value = key*10")
    for k in keys:
        ht.insert(k, k * 10)
    ht.print_table()

    print("\nGet some keys:")
    for k in [10, 15, 20]:
        print(f"get({k}) =", ht.get(k))

    print("\nDelete key 15 (from a collided bucket)")
    ht.delete(15)
    ht.print_table()
    print("=== END HASH TABLE TESTS ===\n")


# ---------------- Main runner ----------------

if __name__ == "__main__":
    print("=== DMMT TOOLKIT START ===\n")
    test_bst()
    test_graph()
    test_hash_table()
    print("=== DMMT TOOLKIT END ===")