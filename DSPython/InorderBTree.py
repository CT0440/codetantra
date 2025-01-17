class Node:
    def __init__(self, value):  # Fixed constructor
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):  # Fixed constructor
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(current_node.right, value)

    def inorder_traversal(self, node, values=None):
        if values is None:  # Ensure a new list is created for each call
            values = []
        if node:
            self.inorder_traversal(node.left, values)
            values.append(node.value)
            self.inorder_traversal(node.right, values)
        return values


# Example usage
tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(7)

print("In-order Traversal:", tree.inorder_traversal(tree.root))
