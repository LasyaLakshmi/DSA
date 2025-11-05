class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # Minimum degree (defines the range for number of keys)
        self.keys = []
        self.children = []
        self.leaf = leaf

    def search(self, k):
        i = 0
        while i < len(self.keys) and k > self.keys[i]:
            i += 1

        if i < len(self.keys) and self.keys[i] == k:
            return self

        if self.leaf:
            return None

        return self.children[i].search(k)

    def insert_non_full(self, k):
        i = len(self.keys) - 1

        if self.leaf:
            # Insert the new key at the correct position
            self.keys.append(0)
            while i >= 0 and k < self.keys[i]:
                self.keys[i + 1] = self.keys[i]
                i -= 1
            self.keys[i + 1] = k
        else:
            # Find the child which will have the new key
            while i >= 0 and k < self.keys[i]:
                i -= 1
            i += 1
            # If the child is full, split it first
            if len(self.children[i].keys) == 2 * self.t - 1:
                self.split_child(i)
                if k > self.keys[i]:
                    i += 1
            self.children[i].insert_non_full(k)

    def split_child(self, i):
        t = self.t
        y = self.children[i]
        z = BTreeNode(t, y.leaf)
        self.children.insert(i + 1, z)
        self.keys.insert(i, y.keys[t - 1])

        z.keys = y.keys[t:(2 * t - 1)]
        y.keys = y.keys[0:t - 1]

        if not y.leaf:
            z.children = y.children[t:(2 * t)]
            y.children = y.children[0:t]

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t, True)
        self.t = t

    def search(self, k):
        return self.root.search(k)

    def insert(self, k):
        root = self.root
        if len(root.keys) == 2 * self.t - 1:
            s = BTreeNode(self.t)
            self.root = s
            s.children.insert(0, root)
            s.leaf = False
            s.split_child(0)
            s.insert_non_full(k)
        else:
            root.insert_non_full(k)

    def traverse(self, node=None):
        if node is None:
            node = self.root	
        i = 0
        for i in range(len(node.keys)):
            if not node.leaf:
                self.traverse(node.children[i])
            print(node.keys[i], end=" ")
        if not node.leaf:
            self.traverse(node.children[i + 1])

# Taking input from user to insert keys into the B-tree
b_tree_order = 3
btree = BTree(b_tree_order)

user_input = input("Enter keys to insert (space separated): ")
keys_to_insert = list(map(int, user_input.split()))

for key in keys_to_insert:
    btree.insert(key)

print("B-tree traversal after insertions:")
btree.traverse()
print()

# Search key input
search_key = int(input("Enter key to search: "))
result = btree.search(search_key)

print(f"Key {search_key} {'found' if result else 'not found'} in B-tree.")
print("Tejaswini-24303")
