class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if node.left:
                self._insert(node.left, data)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self._insert(node.right, data)
            else:
                node.right = Node(data)

    def search(self, data):
        return self._search(self.root, data)

    def _search(self, node, data):
        if node is None:
            return False
        if data == node.data:
            return True
        elif data < node.data:
            return self._search(node.left, data)
        else:
            return self._search(node.right, data)

    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, node, data):
        if node is None:
            return node
        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:
            # Node found
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Replace with inorder successor
            min_larger_node = self._min_value_node(node.right)
            node.data = min_larger_node.data
            node.right = self._delete(node.right, min_larger_node.data)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def inorder_traversal(self):
        if self.root is None:
            print("Tree is empty.")
            return
        print("Inorder Traversal:", end=" ")
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.data, end=" ")
            self._inorder(node.right)

def main():
    print("=== Binary Search Tree (BST) Implementation ===")
    bst = BST()

    n = int(input("Enter number of elements to insert: "))
    for i in range(n):
        val = int(input(f"Enter value {i + 1}: "))
        bst.insert(val)

    print("\nCurrent BST (Inorder Traversal):")
    bst.inorder_traversal()

    search_val = int(input("\nEnter value to search: "))
    if bst.search(search_val):
        print(f"{search_val} found in BST.")
    else:
        print(f"{search_val} not found in BST.")

    del_val = int(input("\nEnter value to delete: "))
    bst.delete(del_val)
    print(f"After deleting {del_val}:")
    bst.inorder_traversal()

if __name__ == "__main__":
    main()
print("Tejaswini-24303")
