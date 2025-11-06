class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)
        return root

    def search(self, root, data):
        if root is None or root.data == data:
            return root
        if data < root.data:
            return self.search(root.left, data)
        return self.search(root.right, data)

    def find_min(self, node):
        while node.left:
            node = node.left
        return node

    def delete(self, root, data):
        if root is None:
            return root
        if data < root.data:
            root.left = self.delete(root.left, data)
        elif data > root.data:
            root.right = self.delete(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.find_min(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

# Example
bst = BST()
root = None
for data in [50, 30, 70, 20, 40, 60, 80]:
    root = bst.insert(root, data)

print("Inorder Traversal:")
bst.inorder(root)

print("\n\nSearch 40:", "Found" if bst.search(root, 40) else "Not Found")

root = bst.delete(root, 20)
print("\nAfter deleting 20:")
bst.inorder(root)